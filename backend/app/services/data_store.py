from app.core.data_seed import get_initial_ports, get_initial_plants, get_initial_vessels, FOIS_MATRIX
from app.models.port import Port
from app.models.plant import SteelPlant
from app.models.vessel import Vessel
from typing import Dict, List, Optional
import copy

class DataStore:
    def __init__(self):
        self.ports: Dict[str, Port] = {p.id: p for p in get_initial_ports()}
        self.plants: Dict[str, SteelPlant] = {pl.id: pl for pl in get_initial_plants()}
        self.vessels: Dict[str, Vessel] = {v.id: v for v in get_initial_vessels()}
        self.fois_matrix = copy.deepcopy(FOIS_MATRIX)
        self.active_scenario: str = "BASELINE"
        self.scenario_description: str = "Baseline operational conditions: Normal shipping channels, standard port operations."

    def get_all_ports(self) -> List[Port]:
        return list(self.ports.values())

    def get_port(self, port_id: str) -> Optional[Port]:
        return self.ports.get(port_id)

    def get_all_plants(self) -> List[SteelPlant]:
        return list(self.plants.values())

    def get_plant(self, plant_id: str) -> Optional[SteelPlant]:
        return self.plants.get(plant_id)

    def get_all_vessels(self) -> List[Vessel]:
        return list(self.vessels.values())

    def get_vessel(self, vessel_id: str) -> Optional[Vessel]:
        return self.vessels.get(vessel_id)

    def apply_scenario(self, scenario_type: str) -> Dict[str, str]:
        if scenario_type == "paradip_congestion":
            self.active_scenario = "PARADIP_CONGESTION"
            self.scenario_description = "Severe port congestion at Paradip: Berth mechanical breakdown + monsoon swell causes queue surge to 8.8 days."
            if "PRT_PARADIP" in self.ports:
                self.ports["PRT_PARADIP"].anchorage_queue_vessels = 18
                self.ports["PRT_PARADIP"].avg_anchorage_wait_days = 8.8
                self.ports["PRT_PARADIP"].status = "CRITICAL"
                self.ports["PRT_PARADIP"].status_details = "Coal unloading conveyor line 2 offline. 18 vessels anchored. Delay ~8.8 days."
            # Vessel status
            if "VSL_STEEL_HORIZON" in self.vessels:
                self.vessels["VSL_STEEL_HORIZON"].status = "DIVERT_RECOMMENDED"

        elif scenario_type == "cyclone_alert":
            self.active_scenario = "CYCLONE_ALERT"
            self.scenario_description = "Bay of Bengal Cyclone Warning: Paradip and Dhamra outer anchorages suspended by Port Conservator for 5 days."
            if "PRT_PARADIP" in self.ports:
                self.ports["PRT_PARADIP"].avg_anchorage_wait_days = 9.5
                self.ports["PRT_PARADIP"].status = "WEATHER_ALERT"
                self.ports["PRT_PARADIP"].status_details = "Cyclone Warning Stage 4. Outer anchorage suspended."
            if "PRT_DHAMRA" in self.ports:
                self.ports["PRT_DHAMRA"].avg_anchorage_wait_days = 7.0
                self.ports["PRT_DHAMRA"].status = "WEATHER_ALERT"
                self.ports["PRT_DHAMRA"].status_details = "Adani Dhamra port operations halted due to squall line."
            if "PRT_VIZAG" in self.ports:
                self.ports["PRT_VIZAG"].status = "NORMAL"
                self.ports["PRT_VIZAG"].avg_anchorage_wait_days = 2.0
            if "VSL_STEEL_HORIZON" in self.vessels:
                self.vessels["VSL_STEEL_HORIZON"].status = "DIVERT_RECOMMENDED"

        elif scenario_type == "rail_shortage":
            self.active_scenario = "RAIL_SHORTAGE"
            self.scenario_description = "South Eastern Railway (SER) Rake Shortage: Coal wagon supply reduced by 60% at Paradip railhead."
            if "PRT_PARADIP" in self.fois_matrix:
                for plt in self.fois_matrix["PRT_PARADIP"]:
                    self.fois_matrix["PRT_PARADIP"][plt]["rakes_available"] = 2

        elif scenario_type == "reset":
            self.ports = {p.id: p for p in get_initial_ports()}
            self.plants = {pl.id: pl for pl in get_initial_plants()}
            self.vessels = {v.id: v for v in get_initial_vessels()}
            self.fois_matrix = copy.deepcopy(FOIS_MATRIX)
            self.active_scenario = "BASELINE"
            self.scenario_description = "Baseline operational conditions: Standard port queues and normal railway rakes."

        return {
            "active_scenario": self.active_scenario,
            "description": self.scenario_description
        }

db = DataStore()
