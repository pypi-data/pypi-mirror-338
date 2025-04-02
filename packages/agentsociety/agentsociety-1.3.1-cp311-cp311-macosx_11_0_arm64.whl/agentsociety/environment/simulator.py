"""Simulator: Urban Simulator"""

import asyncio
import logging
import os
import time
from datetime import datetime, timedelta
from typing import Any, Optional, Union, cast

import ray
from mosstool.type import TripMode
from mosstool.util.format_converter import dict2pb
from pycitydata.map import Map as SimMap
from pycityproto.city.map.v2 import map_pb2 as map_pb2
from pycityproto.city.person.v2 import person_pb2 as person_pb2
from pycityproto.city.person.v2 import person_service_pb2 as person_service
from shapely.geometry import Point

from ..configs import SimConfig
from ..utils.decorators import log_execution_time
from .sidecar import OnlyClientSidecar
from .sim import CityClient, ControlSimEnv
from .utils.const import *

logger = logging.getLogger("agentsociety")

__all__ = [
    "Simulator",
]


@ray.remote
class CityMap:
    def __init__(self, map_cache_path: str):
        self.map = SimMap(
            pb_path=map_cache_path,
        )
        self.poi_cate = POI_CATG_DICT

    def get_aoi(self, aoi_id: Optional[int] = None):
        if aoi_id is None:
            return list(self.map.aois.values())
        else:
            return self.map.aois[aoi_id]

    def get_poi(self, poi_id: Optional[int] = None):
        if poi_id is None:
            return list(self.map.pois.values())
        else:
            return self.map.pois[poi_id]

    def query_pois(
        self,
        center: Union[tuple[float, float], Point],
        radius: Optional[float] = None,
        category_prefix: Optional[str] = None,
        limit: Optional[int] = None,
        return_distance: bool = True,
    ):
        return self.map.query_pois(
            center=center,
            radius=radius,
            category_prefix=category_prefix,
            limit=limit,
            return_distance=return_distance,
        )

    def get_poi_cate(self):
        return self.poi_cate

    def get_map(self):
        return self.map

    def get_map_header(self):
        return self.map.header

    def get_projector(self):
        return self.map.header["projection"]


class Simulator:
    """
    Main class of the simulator.

    - **Description**:
        - This class is the core of the simulator, responsible for initializing and managing the simulation environment.
        - It reads parameters from a configuration dictionary, initializes map data, and starts or connects to a simulation server as needed.
    """

    def __init__(self, sim_config: SimConfig, create_map: bool = False) -> None:
        self.sim_config = sim_config
        """
        - 模拟器配置
        - simulator config
        """
        _map_pb_path = sim_config.prop_map_request.file_path
        config = sim_config.prop_simulator_request
        if not sim_config.prop_status.simulator_activated:
            self._sim_env = sim_env = ControlSimEnv(
                task_name=config.task_name,
                map_file=_map_pb_path,
                max_day=config.max_day,
                start_step=config.start_step,
                total_step=config.total_step,
                log_dir=config.log_dir,
                primary_node_ip=config.primary_node_ip,
                sim_addr=sim_config.simulator_server_address,
            )
            self.server_addr = sim_env.sim_addr
            sim_config.SetServerAddress(self.server_addr)
            sim_config.prop_status.simulator_activated = True
            # using local client
            self._client = CityClient(
                sim_env.sim_addr, self.server_addr.startswith("https")
            )
            for retry in range(60):
                try:
                    self._syncer = OnlyClientSidecar.remote(
                        syncer_address=sim_env.syncer_addr,  # type:ignore
                        name="within-syncer",
                        secure=self.server_addr.startswith("https"),
                    )
                    time.sleep(5)
                    ray.get(self._syncer.init.remote())
                    break
                except:
                    logging.warning(
                        f"Failed to connect to syncer {sim_env.syncer_addr}, retrying..."
                    )
                    time.sleep(1)
                    continue
            else:
                raise ValueError(
                    f"Failed to connect to syncer {sim_env.syncer_addr} after 60 retries!"
                )
            """
            - 模拟器grpc客户端
            - grpc client of simulator
            """
        else:
            self.server_addr: str = sim_config.simulator_server_address  # type:ignore
            self._client = CityClient(
                self.server_addr, secure=self.server_addr.startswith("https")
            )
            # syncer只能由主节点控制
            self._syncer = None
        self._map = None
        """
        - 模拟器地图对象
        - Simulator map object
        """
        if create_map:
            self._map = CityMap.remote(
                _map_pb_path,
            )
            self._create_poi_id_2_aoi_id()

        self.time: int = 0
        """
        - 模拟城市当前时间
        - The current time of simulator
        """
        self.poi_cate = POI_CATG_DICT
        self.map_x_gap = None
        self.map_y_gap = None
        self._bbox: tuple[float, float, float, float] = (-1, -1, -1, -1)
        self._lock = asyncio.Lock()
        self._environment_prompt: dict[str, Any] = {}
        self._log_list = []

    def set_map(self, map: ray.ObjectRef):
        self._map = map
        self._create_poi_id_2_aoi_id()

    def _create_poi_id_2_aoi_id(self):
        pois = ray.get(self._map.get_poi.remote())  # type:ignore
        self.poi_id_2_aoi_id: dict[int, int] = {
            poi["id"]: poi["aoi_id"] for poi in pois
        }

    @property
    def map(self):
        return self._map

    def get_log_list(self):
        return self._log_list

    def clear_log_list(self):
        self._log_list = []

    def get_poi_cate(self):
        return self.poi_cate

    @property
    def environment(self) -> dict[str, str]:
        """
        Get the current state of environment variables.
        """
        return self._environment_prompt

    def get_server_addr(self) -> str:
        return self.server_addr  # type:ignore

    def set_environment(self, environment: dict[str, str]):
        """
        Set the entire dictionary of environment variables.

        - **Args**:
            - `environment` (`Dict[str, str]`): Key-value pairs of environment variables.
        """
        self._environment_prompt = environment

    def sense(self, key: str) -> Any:
        """
        Retrieve the value of an environment variable by its key.

        - **Args**:
            - `key` (`str`): The key of the environment variable.

        - **Returns**:
            - `Any`: The value of the corresponding key, or an empty string if not found.
        """
        return self._environment_prompt.get(key, "")

    def update_environment(self, key: str, value: Any):
        """
        Update the value of a single environment variable.

        - **Args**:
            - `key` (`str`): The key of the environment variable.
            - `value` (`Any`): The new value to set.
        """
        self._environment_prompt[key] = value

    def get_environment(self) -> str:
        global_prompt = ""
        for key in self._environment_prompt:
            value = self._environment_prompt[key]
            if isinstance(value, str):
                global_prompt += f"{key}: {value}\n"
            elif isinstance(value, dict):
                for k, v in value.items():
                    global_prompt += f"{key}.{k}: {v}\n"
            elif isinstance(value, bool):
                global_prompt += f"Is it {key}: {value}\n"
            elif isinstance(value, list):
                global_prompt += f"{key} elements: {value}\n"
            else:
                global_prompt += f"{key}: {value}\n"
        return global_prompt

    @log_execution_time
    def get_poi_categories(
        self,
        center: Optional[Union[tuple[float, float], Point]] = None,
        radius: Optional[float] = None,
    ) -> list[str]:
        """
        Retrieve unique categories of Points of Interest (POIs) around a central point.

        - **Args**:
            - `center` (`Optional[Union[Tuple[float, float], Point]]`): The central point as a tuple or Point object.
              Defaults to (0, 0) if not provided.
            - `radius` (`Optional[float]`): The search radius in meters. If not provided, all POIs are considered.

        - **Returns**:
            - `List[str]`: A list of unique POI category names.
        """
        categories: list[str] = []
        if center is None:
            center = (0, 0)
        _pois: list[dict] = ray.get(
            self.map.query_pois.remote(  # type:ignore
                center=center,
                radius=radius,
                return_distance=False,
            )
        )
        for poi in _pois:
            catg = poi["category"]
            categories.append(catg.split("|")[-1])
        return list(set(categories))

    @log_execution_time
    async def get_time(
        self, format_time: bool = False, format: str = "%H:%M:%S"
    ) -> Union[int, str]:
        """
        Get the current time of the simulator.

        By default, returns the number of seconds since midnight. Supports formatted output.

        - **Args**:
            - `format_time` (`bool`): Whether to return the time in a formatted string. Defaults to `False`.
            - `format` (`str`): The format string for formatting the time. Defaults to "%H:%M:%S".

        - **Returns**:
            - `Union[int, str]`: The current simulation time either as an integer representing seconds since midnight or as a formatted string.
        """
        now = await self._client.clock_service.Now({})
        now = cast(dict[str, int], now)
        self.time = now["t"]
        if format_time:
            current_date = datetime.now().date()
            start_of_day = datetime.combine(current_date, datetime.min.time())
            current_time = start_of_day + timedelta(seconds=now["t"])
            formatted_time = current_time.strftime(format)
            return formatted_time
        else:
            return int(now["t"])

    @log_execution_time
    async def get_simulator_day(self) -> int:
        """
        Get the current day of the simulation.

        - **Returns**:
            - `int`: The day number since the start of the simulation.
        """
        now = await self._client.clock_service.Now({})
        now = cast(dict[str, int], now)
        day = int(now["t"] // (24 * 60 * 60))
        return day

    @log_execution_time
    async def get_simulator_second_from_start_of_day(self) -> int:
        """
        Get the number of seconds elapsed from the start of the current day in the simulation.

        - **Returns**:
            - `int`: The number of seconds from 00:00:00 of the current day.
        """
        now = await self._client.clock_service.Now({})
        now = cast(dict[str, int], now)
        return now["t"] % (24 * 60 * 60)

    @log_execution_time
    async def get_person(self, person_id: int) -> dict:
        """
        Retrieve information about a specific person by ID.

        - **Args**:
            - `person_id` (`int`): The ID of the person to retrieve information for.

        - **Returns**:
            - `Dict`: Information about the specified person.
        """
        person: dict = await self._client.person_service.GetPerson(
            req={"person_id": person_id}
        )  # type:ignore
        return person

    @log_execution_time
    async def add_person(self, dict_person: dict) -> dict:
        """
        Add a new person to the simulation.

        - **Args**:
            - `dict_person` (`dict`): The person object to add.

        - **Returns**:
            - `Dict`: Response from adding the person.
        """
        person = dict2pb(dict_person, person_pb2.Person())
        if isinstance(person, person_pb2.Person):
            req = person_service.AddPersonRequest(person=person)
        else:
            req = person
        resp: dict = await self._client.person_service.AddPerson(req)  # type:ignore
        return resp

    @log_execution_time
    async def set_aoi_schedules(
        self,
        person_id: int,
        target_positions: Union[
            list[Union[int, tuple[int, int]]], Union[int, tuple[int, int]]
        ],
        departure_times: Optional[list[float]] = None,
        modes: Optional[list[TripMode]] = None,
    ):
        """
        Set schedules for a person to visit Areas of Interest (AOIs).

        - **Args**:
            - `person_id` (`int`): The ID of the person whose schedule is being set.
            - `target_positions` (`Union[List[Union[int, Tuple[int, int]]], Union[int, Tuple[int, int]]]`):
              A list of AOI or POI IDs or tuples of (AOI ID, POI ID) that the person will visit.
            - `departure_times` (`Optional[List[float]]`): Departure times for each trip in the schedule.
              If not provided, current time will be used for all trips.
            - `modes` (`Optional[List[int]]`): Travel modes for each trip.
              Defaults to `TRIP_MODE_DRIVE_ONLY` if not specified.
        """
        cur_time = float(await self.get_time())
        if not isinstance(target_positions, list):
            target_positions = [target_positions]
        if departure_times is None:
            departure_times = [cur_time for _ in range(len(target_positions))]
        else:
            for _ in range(len(target_positions) - len(departure_times)):
                departure_times.append(cur_time)
        if modes is None:
            modes = [
                TripMode.TRIP_MODE_DRIVE_ONLY for _ in range(len(target_positions))
            ]
        else:
            for _ in range(len(target_positions) - len(modes)):
                modes.append(TripMode.TRIP_MODE_DRIVE_ONLY)
        _schedules = []
        for target_pos, _time, _mode in zip(target_positions, departure_times, modes):
            if isinstance(target_pos, int):
                if target_pos >= POI_START_ID:
                    poi_id = target_pos
                    end = {
                        "aoi_position": {
                            "aoi_id": self.poi_id_2_aoi_id[poi_id],
                            "poi_id": poi_id,
                        }
                    }
                else:
                    aoi_id = target_pos
                    end = {
                        "aoi_position": {
                            "aoi_id": aoi_id,
                        }
                    }
            else:
                aoi_id, poi_id = target_pos
                end = {"aoi_position": {"aoi_id": aoi_id, "poi_id": poi_id}}
                # activity = ""
            trips = [
                {
                    "mode": _mode,
                    "end": end,
                    "departure_time": _time,
                },
            ]
            _schedules.append(
                {"trips": trips, "loop_count": 1, "departure_time": _time}
            )
        req = {"person_id": person_id, "schedules": _schedules}
        await self._client.person_service.SetSchedule(req)

    @log_execution_time
    async def reset_person_position(
        self,
        person_id: int,
        aoi_id: Optional[int] = None,
        poi_id: Optional[int] = None,
        lane_id: Optional[int] = None,
        s: Optional[float] = None,
    ):
        """
        Reset the position of a person within the simulation.

        - **Args**:
            - `person_id` (`int`): The ID of the person whose position is being reset.
            - `aoi_id` (`Optional[int]`): The ID of the Area of Interest (AOI) where the person should be placed.
            - `poi_id` (`Optional[int]`): The ID of the Point of Interest (POI) within the AOI.
            - `lane_id` (`Optional[int]`): The ID of the lane on which the person should be placed.
            - `s` (`Optional[float]`): The longitudinal position along the lane.
        """
        reset_position = {}
        if aoi_id is not None:
            reset_position["aoi_position"] = {"aoi_id": aoi_id}
            if poi_id is not None:
                reset_position["aoi_position"]["poi_id"] = poi_id
            logger.debug(
                f"Setting person {person_id} pos to AoiPosition {reset_position}"
            )
            await self._client.person_service.ResetPersonPosition(
                {"person_id": person_id, "position": reset_position}
            )
        elif lane_id is not None:
            reset_position["lane_position"] = {
                "lane_id": lane_id,
                "s": 0.0,
            }
            if s is not None:
                reset_position["lane_position"]["s"] = s
            logger.debug(
                f"Setting person {person_id} pos to LanePosition {reset_position}"
            )
            await self._client.person_service.ResetPersonPosition(
                {"person_id": person_id, "position": reset_position}
            )
        else:
            logger.debug(
                f"Neither aoi or lane pos provided for person {person_id} position reset!!"
            )

    @log_execution_time
    def get_around_poi(
        self,
        center: Union[tuple[float, float], Point],
        radius: float,
        poi_type: Union[str, list[str]],
    ) -> list[dict]:
        """
        Get Points of Interest (POIs) around a central point based on type.

        - **Args**:
            - `center` (`Union[Tuple[float, float], Point]`): The central point as a tuple or Point object.
            - `radius` (`float`): The search radius in meters.
            - `poi_type` (`Union[str, List[str]]`): The category or categories of POIs to filter by.

        - **Returns**:
            - `List[Dict]`: A list of dictionaries containing information about the POIs found.
        """
        if isinstance(poi_type, str):
            poi_type = [poi_type]
        transformed_poi_type: list[str] = []
        for t in poi_type:
            if t not in self.poi_cate:
                transformed_poi_type.append(t)
            else:
                transformed_poi_type += self.poi_cate[t]
        poi_type_set = set(transformed_poi_type)
        # query pois within the radius
        _pois: list[dict] = ray.get(
            self.map.query_pois.remote(  # type:ignore
                center=center,
                radius=radius,
                return_distance=False,
            )
        )
        # Filter out POIs that do not meet the category prefix
        pois = []
        for poi in _pois:
            catg = poi["category"]
            if catg.split("|")[-1] not in poi_type_set:
                continue
            pois.append(poi)
        return pois

    def step(self, n: int = 1):
        syncer = self._syncer
        if syncer is None:
            raise ValueError("Step can only be called in primary node!")
        if n <= 0:
            raise ValueError("`n` must >=1!")
        for _ in range(n):
            ray.get(syncer.step.remote())
