from app.models.port import Port
from app.models.plant import SteelPlant
from app.models.vessel import Vessel
from typing import Dict, List, Tuple

def get_initial_ports() -> List[Port]:
    return [
        Port(
            id="PRT_PARADIP",
            name="Paradip Port",
            code="PPT",
            state="Odisha",
            lat=20.2644,
            lon=86.6740,
            max_permissible_draft_m=18.0,
            capesize_capable=True,
            anchorage_queue_vessels=14,
            avg_anchorage_wait_days=7.8,
            discharge_rate_mt_day=38000.0,
            port_handling_charge_usd_mt=4.20,
            demurrage_standard_usd_day=25000.0,
            free_storage_days=5,
            ground_rent_usd_mt_day=0.18,
            status="CONGESTED",
            status_details="Severe outer anchorage backlog due to mechanized coal berth mechanical outage."
        ),
        Port(
            id="PRT_DHAMRA",
            name="Dhamra Port (Adani)",
            code="DHAMRA",
            state="Odisha",
            lat=20.8290,
            lon=86.9630,
            max_permissible_draft_m=18.5,
            capesize_capable=True,
            anchorage_queue_vessels=3,
            avg_anchorage_wait_days=1.1,
            discharge_rate_mt_day=65000.0,
            port_handling_charge_usd_mt=4.45,
            demurrage_standard_usd_day=25000.0,
            free_storage_days=6,
            ground_rent_usd_mt_day=0.15,
            status="NORMAL",
            status_details="Deep-draft berths operational. Fast turnaround conveyor discharge active."
        ),
        Port(
            id="PRT_VIZAG",
            name="Visakhapatnam (Vizag) Port",
            code="VPT",
            state="Andhra Pradesh",
            lat=17.6868,
            lon=83.2185,
            max_permissible_draft_m=18.1,
            capesize_capable=True,
            anchorage_queue_vessels=6,
            avg_anchorage_wait_days=3.2,
            discharge_rate_mt_day=45000.0,
            port_handling_charge_usd_mt=4.15,
            demurrage_standard_usd_day=25000.0,
            free_storage_days=5,
            ground_rent_usd_mt_day=0.17,
            status="MONITOR",
            status_details="Outer harbor berths clear. Moderate inner channel congestion."
        ),
        Port(
            id="PRT_GANGAVARAM",
            name="Gangavaram Port (Adani)",
            code="GPL",
            state="Andhra Pradesh",
            lat=17.6180,
            lon=83.2390,
            max_permissible_draft_m=19.5,
            capesize_capable=True,
            anchorage_queue_vessels=4,
            avg_anchorage_wait_days=1.8,
            discharge_rate_mt_day=58000.0,
            port_handling_charge_usd_mt=4.35,
            demurrage_standard_usd_day=25000.0,
            free_storage_days=5,
            ground_rent_usd_mt_day=0.16,
            status="NORMAL",
            status_details="Deep-draft multipurpose bulk terminal active."
        ),
        Port(
            id="PRT_HALDIA",
            name="Haldia Dock Complex (SMP Kolkata)",
            code="HDC",
            state="West Bengal",
            lat=22.0250,
            lon=88.0680,
            max_permissible_draft_m=8.5,
            capesize_capable=False,
            anchorage_queue_vessels=9,
            avg_anchorage_wait_days=4.5,
            discharge_rate_mt_day=22000.0,
            port_handling_charge_usd_mt=4.80,
            demurrage_standard_usd_day=22000.0,
            free_storage_days=4,
            ground_rent_usd_mt_day=0.22,
            status="CONGESTED",
            status_details="Riverine draft constraint (<9.0m). Capesize vessels require offshore lighterage at Sandheads."
        ),
        Port(
            id="PRT_KRISHNAPATNAM",
            name="Krishnapatnam Port",
            code="KPCL",
            state="Andhra Pradesh",
            lat=14.2500,
            lon=80.1200,
            max_permissible_draft_m=18.5,
            capesize_capable=True,
            anchorage_queue_vessels=2,
            avg_anchorage_wait_days=1.4,
            discharge_rate_mt_day=52000.0,
            port_handling_charge_usd_mt=4.25,
            demurrage_standard_usd_day=25000.0,
            free_storage_days=6,
            ground_rent_usd_mt_day=0.16,
            status="NORMAL",
            status_details="Berths clear. Automated high-speed grab ship unloaders operating."
        )
    ]

def get_initial_plants() -> List[SteelPlant]:
    return [
        SteelPlant(
            id="PLT_SAIL_ROURKELA",
            name="SAIL Rourkela Steel Plant (RSP)",
            short_name="SAIL Rourkela",
            company="SAIL",
            state="Odisha",
            lat=22.2259,
            lon=84.8640,
            daily_coking_coal_consumption_mt=16000.0,
            current_stockpile_mt=176000.0,
            stockpile_runway_days=11.0,
            critical_buffer_threshold_days=12.0,
            status="CRITICAL"
        ),
        SteelPlant(
            id="PLT_SAIL_BOKARO",
            name="SAIL Bokaro Steel Plant (BSL)",
            short_name="SAIL Bokaro",
            company="SAIL",
            state="Jharkhand",
            lat=23.6693,
            lon=86.1511,
            daily_coking_coal_consumption_mt=18000.0,
            current_stockpile_mt=270000.0,
            stockpile_runway_days=15.0,
            critical_buffer_threshold_days=12.0,
            status="HEALTHY"
        ),
        SteelPlant(
            id="PLT_SAIL_BHILAI",
            name="SAIL Bhilai Steel Plant (BSP)",
            short_name="SAIL Bhilai",
            company="SAIL",
            state="Chhattisgarh",
            lat=21.1938,
            lon=81.3857,
            daily_coking_coal_consumption_mt=22000.0,
            current_stockpile_mt=352000.0,
            stockpile_runway_days=16.0,
            critical_buffer_threshold_days=12.0,
            status="HEALTHY"
        ),
        SteelPlant(
            id="PLT_TATA_KALINGANAGAR",
            name="Tata Steel Kalinganagar",
            short_name="Tata Kalinganagar",
            company="Tata Steel",
            state="Odisha",
            lat=20.9630,
            lon=86.0120,
            daily_coking_coal_consumption_mt=14000.0,
            current_stockpile_mt=196000.0,
            stockpile_runway_days=14.0,
            critical_buffer_threshold_days=12.0,
            status="HEALTHY"
        ),
        SteelPlant(
            id="PLT_RINL_VIZAG",
            name="Rashtriya Ispat Nigam Ltd (RINL - Vizag Steel)",
            short_name="RINL Vizag",
            company="RINL",
            state="Andhra Pradesh",
            lat=17.6320,
            lon=83.1850,
            daily_coking_coal_consumption_mt=17000.0,
            current_stockpile_mt=238000.0,
            stockpile_runway_days=14.0,
            critical_buffer_threshold_days=12.0,
            status="HEALTHY"
        )
    ]

def get_initial_vessels() -> List[Vessel]:
    return [
        Vessel(
            id="VSL_STEEL_HORIZON",
            name="MV Steel Horizon",
            mmsi="477283910",
            imo="9481234",
            vessel_class="Capesize",
            deadweight_tonnage=165000.0,
            current_draft=17.5,
            max_draft=18.2,
            cargo_type="Premium Hard Coking Coal (Peak Downs/Goonjella)",
            cargo_quantity_mt=150000.0,
            origin_port="Hay Point, Queensland, Australia",
            destination_port="PRT_PARADIP",
            destination_plant="PLT_SAIL_ROURKELA",
            current_lat=6.4500,
            current_lon=88.7500,
            heading=325.0,
            speed_knots=12.6,
            open_ocean_days_out=11.2,
            daily_charter_rate_usd=26500.0,
            demurrage_rate_usd_day=25000.0,
            fuel_consumption_sea_mt_day=38.5,
            fuel_price_usd_mt=620.0,
            status="DIVERT_RECOMMENDED",
            historical_trail=[
                [-15.0, 115.0],
                [-5.0, 100.0],
                [0.5, 94.0],
                [4.2, 90.5],
                [6.45, 88.75]
            ]
        ),
        Vessel(
            id="VSL_KALINGA_PIONEER",
            name="MV Kalinga Pioneer",
            mmsi="563019820",
            imo="9524589",
            vessel_class="Capesize",
            deadweight_tonnage=178000.0,
            current_draft=18.0,
            max_draft=18.4,
            cargo_type="Metallurgical Coking Coal",
            cargo_quantity_mt=160000.0,
            origin_port="Gladstone, Australia",
            destination_port="PRT_DHAMRA",
            destination_plant="PLT_TATA_KALINGANAGAR",
            current_lat=12.1500,
            current_lon=86.3500,
            heading=335.0,
            speed_knots=13.2,
            open_ocean_days_out=8.4,
            daily_charter_rate_usd=28000.0,
            demurrage_rate_usd_day=27000.0,
            fuel_consumption_sea_mt_day=41.0,
            fuel_price_usd_mt=620.0,
            status="ON_SCHEDULE",
            historical_trail=[
                [-10.0, 105.0],
                [2.0, 92.0],
                [8.0, 88.0],
                [12.15, 86.35]
            ]
        ),
        Vessel(
            id="VSL_BENGAL_FORTUNE",
            name="MV Bengal Fortune",
            mmsi="636015482",
            imo="9349812",
            vessel_class="Panamax",
            deadweight_tonnage=76000.0,
            current_draft=13.6,
            max_draft=14.2,
            cargo_type="PCI Coal (Pulverized Coal Injection)",
            cargo_quantity_mt=70000.0,
            origin_port="Richards Bay, South Africa",
            destination_port="PRT_VIZAG",
            destination_plant="PLT_RINL_VIZAG",
            current_lat=10.5000,
            current_lon=82.8000,
            heading=350.0,
            speed_knots=11.8,
            open_ocean_days_out=4.1,
            daily_charter_rate_usd=16500.0,
            demurrage_rate_usd_day=18000.0,
            fuel_consumption_sea_mt_day=26.0,
            fuel_price_usd_mt=620.0,
            status="ON_SCHEDULE",
            historical_trail=[
                [-20.0, 55.0],
                [-5.0, 70.0],
                [5.0, 78.0],
                [10.5, 82.8]
            ]
        )
    ]

# Indian Railways FOIS Distance (km) and Freight Tariff (USD/MT and INR/MT)
# FOIS Class 140/150 Bulk Cargo Tariffs + Wagons Available
FOIS_MATRIX: Dict[str, Dict[str, Dict[str, float]]] = {
    "PRT_PARADIP": {
        "PLT_SAIL_ROURKELA": {"distance_km": 462.0, "tariff_inr_mt": 1280.0, "transit_days": 2.0, "rakes_available": 6},
        "PLT_SAIL_BOKARO": {"distance_km": 570.0, "tariff_inr_mt": 1460.0, "transit_days": 2.5, "rakes_available": 6},
        "PLT_SAIL_BHILAI": {"distance_km": 780.0, "tariff_inr_mt": 1890.0, "transit_days": 3.5, "rakes_available": 6},
        "PLT_TATA_KALINGANAGAR": {"distance_km": 135.0, "tariff_inr_mt": 540.0, "transit_days": 1.0, "rakes_available": 6},
        "PLT_RINL_VIZAG": {"distance_km": 590.0, "tariff_inr_mt": 1520.0, "transit_days": 2.8, "rakes_available": 6}
    },
    "PRT_DHAMRA": {
        "PLT_SAIL_ROURKELA": {"distance_km": 418.0, "tariff_inr_mt": 1210.0, "transit_days": 1.8, "rakes_available": 10},
        "PLT_SAIL_BOKARO": {"distance_km": 495.0, "tariff_inr_mt": 1350.0, "transit_days": 2.1, "rakes_available": 10},
        "PLT_SAIL_BHILAI": {"distance_km": 825.0, "tariff_inr_mt": 1940.0, "transit_days": 3.7, "rakes_available": 10},
        "PLT_TATA_KALINGANAGAR": {"distance_km": 122.0, "tariff_inr_mt": 510.0, "transit_days": 0.9, "rakes_available": 10},
        "PLT_RINL_VIZAG": {"distance_km": 660.0, "tariff_inr_mt": 1650.0, "transit_days": 3.0, "rakes_available": 10}
    },
    "PRT_VIZAG": {
        "PLT_SAIL_ROURKELA": {"distance_km": 815.0, "tariff_inr_mt": 1960.0, "transit_days": 3.6, "rakes_available": 8},
        "PLT_SAIL_BOKARO": {"distance_km": 940.0, "tariff_inr_mt": 2180.0, "transit_days": 4.0, "rakes_available": 8},
        "PLT_SAIL_BHILAI": {"distance_km": 560.0, "tariff_inr_mt": 1440.0, "transit_days": 2.4, "rakes_available": 8},
        "PLT_TATA_KALINGANAGAR": {"distance_km": 680.0, "tariff_inr_mt": 1720.0, "transit_days": 3.1, "rakes_available": 8},
        "PLT_RINL_VIZAG": {"distance_km": 28.0, "tariff_inr_mt": 190.0, "transit_days": 0.3, "rakes_available": 8}
    },
    "PRT_GANGAVARAM": {
        "PLT_SAIL_ROURKELA": {"distance_km": 835.0, "tariff_inr_mt": 1990.0, "transit_days": 3.7, "rakes_available": 7},
        "PLT_SAIL_BOKARO": {"distance_km": 960.0, "tariff_inr_mt": 2210.0, "transit_days": 4.1, "rakes_available": 7},
        "PLT_SAIL_BHILAI": {"distance_km": 575.0, "tariff_inr_mt": 1470.0, "transit_days": 2.5, "rakes_available": 7},
        "PLT_TATA_KALINGANAGAR": {"distance_km": 700.0, "tariff_inr_mt": 1750.0, "transit_days": 3.2, "rakes_available": 7},
        "PLT_RINL_VIZAG": {"distance_km": 18.0, "tariff_inr_mt": 160.0, "transit_days": 0.2, "rakes_available": 7}
    },
    "PRT_HALDIA": {
        "PLT_SAIL_ROURKELA": {"distance_km": 385.0, "tariff_inr_mt": 1140.0, "transit_days": 1.7, "rakes_available": 5},
        "PLT_SAIL_BOKARO": {"distance_km": 410.0, "tariff_inr_mt": 1190.0, "transit_days": 1.8, "rakes_available": 5},
        "PLT_SAIL_BHILAI": {"distance_km": 870.0, "tariff_inr_mt": 2050.0, "transit_days": 3.9, "rakes_available": 5},
        "PLT_TATA_KALINGANAGAR": {"distance_km": 290.0, "tariff_inr_mt": 920.0, "transit_days": 1.4, "rakes_available": 5},
        "PLT_RINL_VIZAG": {"distance_km": 890.0, "tariff_inr_mt": 2090.0, "transit_days": 4.0, "rakes_available": 5}
    },
    "PRT_KRISHNAPATNAM": {
        "PLT_SAIL_ROURKELA": {"distance_km": 1180.0, "tariff_inr_mt": 2580.0, "transit_days": 5.0, "rakes_available": 6},
        "PLT_SAIL_BOKARO": {"distance_km": 1310.0, "tariff_inr_mt": 2790.0, "transit_days": 5.4, "rakes_available": 6},
        "PLT_SAIL_BHILAI": {"distance_km": 880.0, "tariff_inr_mt": 2060.0, "transit_days": 3.8, "rakes_available": 6},
        "PLT_TATA_KALINGANAGAR": {"distance_km": 1050.0, "tariff_inr_mt": 2380.0, "transit_days": 4.5, "rakes_available": 6},
        "PLT_RINL_VIZAG": {"distance_km": 410.0, "tariff_inr_mt": 1180.0, "transit_days": 2.0, "rakes_available": 6}
    }
}
