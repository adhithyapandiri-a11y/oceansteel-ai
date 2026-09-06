from pydantic import BaseModel, Field
from typing import Optional, List

class AISPosition(BaseModel):
    lat: float
    lon: float
    heading: float
    speed_knots: float
    timestamp: str

class Vessel(BaseModel):
    id: str
    name: str
    mmsi: str
    imo: str
    vessel_class: str
    deadweight_tonnage: float
    current_draft: float
    max_draft: float
    cargo_type: str
    cargo_quantity_mt: float
    origin_port: str
    destination_port: str
    destination_plant: str
    current_lat: float
    current_lon: float
    heading: float
    speed_knots: float
    open_ocean_days_out: float
    daily_charter_rate_usd: float
    demurrage_rate_usd_day: float
    fuel_consumption_sea_mt_day: float
    fuel_price_usd_mt: float
    status: str
    historical_trail: List[List[float]] = Field(default_factory=list)
