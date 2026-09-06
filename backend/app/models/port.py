from pydantic import BaseModel
from typing import Optional

class Port(BaseModel):
    id: str
    name: str
    code: str
    state: str
    lat: float
    lon: float
    max_permissible_draft_m: float  # In meters (e.g. 18.5m for Dhamra, 17.5m for Paradip, 8.5m for Haldia)
    capesize_capable: bool
    anchorage_queue_vessels: int  # Number of vessels waiting
    avg_anchorage_wait_days: float  # Current delay in days
    discharge_rate_mt_day: float  # MT per day unloading capacity
    port_handling_charge_usd_mt: float  # Port charges per MT
    demurrage_standard_usd_day: float  # Demurrage fine per day
    free_storage_days: int  # Standard free days before ground rent
    ground_rent_usd_mt_day: float  # Storage fine per MT per day after free days
    status: str  # "NORMAL", "CONGESTED", "CRITICAL", "WEATHER_ALERT"
    status_details: Optional[str] = None
