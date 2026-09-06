from pydantic import BaseModel

class SteelPlant(BaseModel):
    id: str
    name: str
    short_name: str
    company: str  # SAIL, RINL, Tata Steel, JSW
    state: str
    lat: float
    lon: float
    daily_coking_coal_consumption_mt: float  # Daily burn rate in MT
    current_stockpile_mt: float  # Current inventory on hand
    stockpile_runway_days: float  # Days until stockout
    critical_buffer_threshold_days: float  # Safety stock threshold (e.g. 12 days)
    status: str  # "HEALTHY", "MONITOR", "CRITICAL"
