from typing import List, Dict, Any, Optional
from app.models.vessel import Vessel
from app.models.optimization import OptimizationResult
from app.services.tlc_optimizer import solve_tlc_optimization
from app.services.data_store import db

class PrescriptiveReroutingEngine:
    @staticmethod
    def evaluate_vessel(vessel_id: str) -> Optional[OptimizationResult]:
        vessel = db.get_vessel(vessel_id)
        if not vessel:
            return None
        
        plant = db.get_plant(vessel.destination_plant)
        if not plant:
            # Fallback to SAIL Rourkela
            plant = db.get_plant("PLT_SAIL_ROURKELA")
            
        candidate_ports = db.get_all_ports()
        result = solve_tlc_optimization(
            vessel=vessel,
            destination_plant=plant,
            candidate_ports=candidate_ports,
            fois_matrix=db.fois_matrix
        )
        
        # Update vessel status in-memory
        if result.prescriptive_action == "DIVERT_RECOMMENDED":
            vessel.status = "DIVERT_RECOMMENDED"
        else:
            vessel.status = "ON_SCHEDULE"
            
        return result

    @staticmethod
    def evaluate_all_active_vessels() -> List[OptimizationResult]:
        results = []
        for vessel in db.get_all_vessels():
            res = PrescriptiveReroutingEngine.evaluate_vessel(vessel.id)
            if res:
                results.append(res)
        return results

rerouting_engine = PrescriptiveReroutingEngine()
