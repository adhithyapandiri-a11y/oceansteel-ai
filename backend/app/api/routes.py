from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

from app.services.data_store import db
from app.services.tlc_optimizer import solve_tlc_optimization
from app.services.rerouting_engine import rerouting_engine
from app.services.ml_forecaster import ml_forecaster
from app.services.document_generator import document_generator
from app.services.fois_service import fois_service
from app.core.config import settings

router = APIRouter()

class ScenarioRequest(BaseModel):
    scenario: str  # "paradip_congestion", "cyclone_alert", "rail_shortage", "reset"

class OptimizeRequest(BaseModel):
    vessel_id: str
    destination_plant_id: Optional[str] = None

class DocumentRequest(BaseModel):
    vessel_id: str
    target_port_id: str
    destination_plant_id: Optional[str] = None

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "system": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "problem_statement": settings.SIH_PROBLEM_ID
    }

@router.get("/summary")
def get_executive_summary():
    vessels = db.get_all_vessels()
    ports = db.get_all_ports()
    plants = db.get_all_plants()
    
    # Calculate aggregate savings across all active vessels
    total_savings_usd = 0.0
    total_days_saved = 0.0
    divert_count = 0
    
    for v in vessels:
        res = rerouting_engine.evaluate_vessel(v.id)
        if res:
            if res.prescriptive_action == "DIVERT_RECOMMENDED":
                total_savings_usd += res.net_savings_usd
                total_days_saved += res.days_saved
                divert_count += 1
                
    total_savings_inr_crore = round((total_savings_usd * settings.USD_TO_INR_RATE) / 10000000.0, 2)
    
    return {
        "active_vessels_tracked": len(vessels),
        "divert_alerts_active": divert_count,
        "total_forex_saved_usd": round(total_savings_usd, 2),
        "total_savings_inr_crore": total_savings_inr_crore,
        "total_demurrage_days_avoided": round(total_days_saved, 1),
        "active_ports_monitored": len(ports),
        "steel_plants_connected": len(plants),
        "current_scenario": db.active_scenario,
        "scenario_description": db.scenario_description
    }

@router.get("/vessels")
def get_vessels():
    vessels = db.get_all_vessels()
    results = []
    for v in vessels:
        opt = rerouting_engine.evaluate_vessel(v.id)
        v_dict = v.model_dump()
        v_dict["prescriptive_evaluation"] = opt.model_dump() if opt else None
        results.append(v_dict)
    return results

@router.get("/ports")
def get_ports():
    return db.get_all_ports()

@router.get("/plants")
def get_plants():
    return db.get_all_plants()

@router.get("/rail")
def get_rail_telemetry():
    return fois_service.get_rail_status_overview()

@router.post("/optimize")
def run_optimization(req: OptimizeRequest):
    vessel = db.get_vessel(req.vessel_id)
    if not vessel:
        raise HTTPException(status_code=404, detail="Vessel not found")
    
    plant_id = req.destination_plant_id or vessel.destination_plant
    plant = db.get_plant(plant_id)
    if not plant:
        plant = db.get_plant("PLT_SAIL_ROURKELA")
        
    ports = db.get_all_ports()
    result = solve_tlc_optimization(
        vessel=vessel,
        destination_plant=plant,
        candidate_ports=ports,
        fois_matrix=db.fois_matrix
    )
    return result

@router.get("/forecast")
def get_freight_forecast():
    return ml_forecaster.get_bdi_bci_forecast()

@router.post("/simulate")
def apply_simulation(req: ScenarioRequest):
    result = db.apply_scenario(req.scenario)
    # Re-evaluate vessels
    rerouting_engine.evaluate_all_active_vessels()
    return result

@router.post("/documents/generate")
def generate_maritime_documents(req: DocumentRequest):
    vessel = db.get_vessel(req.vessel_id)
    if not vessel:
        raise HTTPException(status_code=404, detail="Vessel not found")
        
    target_port = db.get_port(req.target_port_id)
    if not target_port:
        raise HTTPException(status_code=404, detail="Target port not found")
        
    original_port = db.get_port(vessel.destination_port)
    if not original_port:
        original_port = db.get_port("PRT_PARADIP")
        
    plant_id = req.destination_plant_id or vessel.destination_plant
    plant = db.get_plant(plant_id)
    if not plant:
        plant = db.get_plant("PLT_SAIL_ROURKELA")
        
    opt_result = solve_tlc_optimization(
        vessel=vessel,
        destination_plant=plant,
        candidate_ports=db.get_all_ports(),
        fois_matrix=db.fois_matrix
    )
    
    docs = document_generator.generate_all_documents(
        vessel=vessel,
        original_port=original_port,
        new_port=target_port,
        plant=plant,
        opt_result=opt_result
    )
    return docs
