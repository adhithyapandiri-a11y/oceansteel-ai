from typing import Dict, Any, List
from app.services.data_store import db
from app.core.config import settings

class FOISService:
    @staticmethod
    def get_rail_status_overview() -> Dict[str, Any]:
        """
        Returns real-time FOIS rake availability, siding status,
        and throughput metrics across East Coast ports.
        """
        ports = db.get_all_ports()
        plants = db.get_all_plants()
        
        rail_nodes = []
        for port in ports:
            port_matrix = db.fois_matrix.get(port.id, {})
            # Representative plant: SAIL Rourkela
            rourkela_info = port_matrix.get("PLT_SAIL_ROURKELA", {})
            rakes = rourkela_info.get("rakes_available", 6)
            
            rail_nodes.append({
                "port_id": port.id,
                "port_name": port.name,
                "rakes_available_today": rakes,
                "daily_evacuation_capacity_mt": rakes * 3850,
                "boxn_rakes_in_transit": max(1, rakes - 2),
                "avg_turnaround_hours": round(rourkela_info.get("transit_days", 2.0) * 24.0, 1),
                "freight_tariff_inr_mt": rourkela_info.get("tariff_inr_mt", 1300.0),
                "status": "NORMAL" if rakes >= 6 else ("LOW_CAPACITY" if rakes >= 3 else "CRITICAL_SHORTAGE")
            })
            
        return {
            "network": "Indian Railways (FOIS / CRIS - SER & ECoR Zones)",
            "telemetry_source": "Live CRIS REST API Feed Simulator",
            "standard_rake_type": "BOXN / BOXNHL (59 wagons, ~3,850 MT payload)",
            "nodes": rail_nodes
        }

fois_service = FOISService()
