import unittest
import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.data_seed import get_initial_ports, get_initial_plants, get_initial_vessels, FOIS_MATRIX
from app.services.tlc_optimizer import solve_tlc_optimization
from app.services.ml_forecaster import ml_forecaster
from app.services.document_generator import document_generator
from app.services.rerouting_engine import rerouting_engine
from app.services.data_store import db

class TestOceanSteelAI(unittest.TestCase):
    def setUp(self):
        self.ports = get_initial_ports()
        self.plants = get_initial_plants()
        self.vessels = get_initial_vessels()
        self.fois = FOIS_MATRIX

    def test_tlc_optimization_paradip_to_dhamra(self):
        vessel = next(v for v in self.vessels if v.id == "VSL_STEEL_HORIZON")
        plant = next(p for p in self.plants if p.id == "PLT_SAIL_ROURKELA")
        
        result = solve_tlc_optimization(
            vessel=vessel,
            destination_plant=plant,
            candidate_ports=self.ports,
            fois_matrix=self.fois
        )
        
        # Verify result structure
        self.assertEqual(result.vessel_id, "VSL_STEEL_HORIZON")
        self.assertEqual(result.baseline_port_id, "PRT_PARADIP")
        # Dhamra should be recommended due to low queue (1.1 days vs 7.8 days)
        self.assertEqual(result.recommended_port_id, "PRT_DHAMRA")
        self.assertEqual(result.prescriptive_action, "DIVERT_RECOMMENDED")
        self.assertGreater(result.net_savings_usd, 50000.0)
        self.assertGreater(result.days_saved, 4.0)

    def test_draft_infeasibility_haldia(self):
        # Capesize vessel with 17.8m draft cannot dock at Haldia (8.5m max)
        vessel = next(v for v in self.vessels if v.id == "VSL_STEEL_HORIZON")
        plant = next(p for p in self.plants if p.id == "PLT_SAIL_ROURKELA")
        
        result = solve_tlc_optimization(
            vessel=vessel,
            destination_plant=plant,
            candidate_ports=self.ports,
            fois_matrix=self.fois
        )
        
        haldia_eval = next(p for p in result.port_evaluations if p.port_id == "PRT_HALDIA")
        self.assertFalse(haldia_eval.is_feasible)
        self.assertIn("Draft Violation", haldia_eval.infeasible_reason)

    def test_ml_forecaster(self):
        forecast_data = ml_forecaster.get_bdi_bci_forecast()
        self.assertIn("current_metrics", forecast_data)
        self.assertEqual(len(forecast_data["history"]), 30)
        self.assertEqual(len(forecast_data["forecast"]), 30)
        
        # Test confidence interval sanity: P90 >= P50 >= P10
        first_day = forecast_data["forecast"][0]
        self.assertGreaterEqual(first_day["bci_p90"], first_day["bci_p50"])
        self.assertGreaterEqual(first_day["bci_p50"], first_day["bci_p10"])

    def test_document_generation(self):
        vessel = self.vessels[0]
        orig_port = self.ports[0]
        target_port = self.ports[1]
        plant = self.plants[0]
        
        opt = solve_tlc_optimization(vessel, plant, self.ports, self.fois)
        docs = document_generator.generate_all_documents(vessel, orig_port, target_port, plant, opt)
        
        self.assertIn("bimco_reroute", docs)
        self.assertIn("pre_nor", docs)
        self.assertIn("fois_indent", docs)
        self.assertIn("Steel Authority of India Ltd. (SAIL)", docs["bimco_reroute"])
        self.assertIn(vessel.imo, docs["bimco_reroute"])

    def test_scenario_injection(self):
        # Test applying cyclone scenario
        db.apply_scenario("cyclone_alert")
        paradip = db.get_port("PRT_PARADIP")
        self.assertEqual(paradip.status, "WEATHER_ALERT")
        
        # Test reset
        db.apply_scenario("reset")
        paradip_reset = db.get_port("PRT_PARADIP")
        self.assertEqual(paradip_reset.status, "CONGESTED")

if __name__ == '__main__':
    unittest.main()
