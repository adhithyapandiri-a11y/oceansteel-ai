from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class PortCostBreakdown(BaseModel):
    port_id: str
    port_name: str
    is_feasible: bool
    infeasible_reason: Optional[str] = None
    ocean_freight_usd: float
    sea_bunker_fuel_usd: float
    extra_sea_steaming_days: float
    port_demurrage_usd: float
    port_wait_days: float
    port_handling_charges_usd: float
    inland_rail_freight_usd: float
    rail_transit_days: float
    port_storage_fines_usd: float
    total_landed_cost_usd: float
    total_landed_cost_inr_crore: float
    total_turnaround_days: float
    co2_emissions_mt: float

class OptimizationResult(BaseModel):
    vessel_id: str
    vessel_name: str
    cargo_type: str
    cargo_quantity_mt: float
    destination_plant: str
    baseline_port_id: str
    baseline_port_name: str
    recommended_port_id: str
    recommended_port_name: str
    prescriptive_action: str  # "DIVERT_RECOMMENDED" or "MAINTAIN_COURSE"
    net_savings_usd: float
    net_savings_inr_crore: float
    days_saved: float
    decision_urgency: str  # "HIGH", "MEDIUM", "LOW"
    reasoning: str
    formula_verification: Dict[str, Any]
    port_evaluations: List[PortCostBreakdown]
