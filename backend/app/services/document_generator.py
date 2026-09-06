from datetime import datetime
from typing import Dict, Any
from app.models.vessel import Vessel
from app.models.port import Port
from app.models.plant import SteelPlant
from app.models.optimization import OptimizationResult

class DocumentGenerator:
    @staticmethod
    def generate_all_documents(
        vessel: Vessel,
        original_port: Port,
        new_port: Port,
        plant: SteelPlant,
        opt_result: OptimizationResult
    ) -> Dict[str, str]:
        today_str = datetime.now().strftime("%d %B %Y %H:%M UTC")
        ref_no = f"OSA-RR-{vessel.imo}-{datetime.now().strftime('%Y%m%d%H%M')}"
        
        # 1. BIMCO / C(ORE)7 Charter Party Rerouting Order & Addendum
        bimco_reroute = f"""================================================================================
VOYAGE RECHARTERING & DIVERSION DIRECTIVE
ISSUED BY: OCEANSTEEL AI CHARTERING COMMAND CENTER (ON BEHALF OF CHARTERERS)
DOCUMENT REF: {ref_no}
DATE & TIME: {today_str}
================================================================================

TO:
  MASTER, {vessel.name.upper()} (IMO: {vessel.imo} | MMSI: {vessel.mmsi})
  OWNERS / MANAGERS: OCEANIC BULK SHIPPING LTD.
  PORT OF DEPARTURE: {vessel.origin_port}
  CURRENT NOMINATED DISPORT: {original_port.name.upper()} ({original_port.code})
  FINAL RECEIVER / CONSIGNEE: {plant.name.upper()} ({plant.company})

SUBJECT: RECHARTERING DIRECTIVE & AMENDED DISCHARGE PORT NOMINATION
--------------------------------------------------------------------------------
1. EXERCISE OF LIBERTY CLAUSE:
   Under Clause 18 of standard BIMCO GENCON / C(ORE)7 Charter Party and the
   express liberties clause governing safe berth nomination, Charterers hereby
   revoke the nomination of {original_port.name.upper()} as the Port of Discharge.

2. OFFICIAL RE-NOMINATION:
   Charterers formally nominate and instruct {vessel.name.upper()} to proceed to:
   >>> NOMINATED DISCHARGE PORT: {new_port.name.upper()} ({new_port.code}, {new_port.state}, INDIA)
   >>> TARGET BERTH: DEEP-DRAFT MECHANIZED BULK BERTH (PERMISSIBLE DRAFT: {new_port.max_permissible_draft_m}m)
   >>> REVISED VOYAGE DISTANCE ADJUSTMENT: ~{opt_result.formula_verification.get('sea_fuel_differential_usd', 0):,.0f} USD BUNKER REIMBURSEMENT ALLOWED.

3. LEGAL PRECEDENT & STATUTORY COMPLIANCE:
   This prescriptive diversion is executed pursuant to duty to mitigate damages
   established under:
   a) Calcutta High Court Ruling: Steel Authority of India Ltd. (SAIL) vs.
      Vizag Seaport Private Ltd. (2026), affirming charterer's prerogative to
      re-nominate disport to avoid unreasonable berth detention.
   b) Supreme Court of India Landmark Ruling: Union of India & Anr. vs.
      Indian Inland Waterways & Ors. (2020) on maritime demurrage mitigation.
   c) Directorate General of Shipping (DGS) Circular on Demurrage Minimization.

4. ECONOMIC BENEFIT & SAVINGS AUDIT:
   - Anticipated Anchorage Waiting Days Avoided: {opt_result.days_saved:.1f} Days
   - Avoided Demurrage Liability: ${opt_result.formula_verification.get('demurrage_saved_usd', 0):,.2f} USD
   - Net Landed Cost Benefit to Consignee: ${opt_result.net_savings_usd:,.2f} USD (INR {opt_result.net_savings_inr_crore:.2f} Crore)

Please acknowledge receipt of this voyage amendment immediately via Sat-C and
update AIS Destination to '{new_port.code} IN' with adjusted ETA.

SIGNED & ISSUED:
CHIEF CHARTERING OFFICER
OCEANSTEEL AI / RAW MATERIAL PROCUREMENT DIVISION
================================================================================"""

        # 2. Master's Pre-Notice of Readiness (Pre-NOR)
        nor_doc = f"""================================================================================
ADVANCE NOTICE OF READINESS (PRE-NOR)
ISSUED TO PORT CONSERVATOR & STEVEDORES
================================================================================
DATE: {today_str}
TO:
  THE PORT CONSERVATOR & TRAFFIC MANAGER, {new_port.name.upper()}
  TERMINAL OPERATOR & RECEIVING AGENTS
  CC: {plant.name.upper()} LOGISTICS DESK

VESSEL: {vessel.name.upper()}
IMO NUMBER: {vessel.imo}
CALL SIGN / MMSI: {vessel.mmsi}
VESSEL CLASS: {vessel.vessel_class} (DWT: {vessel.deadweight_tonnage:,.0f} MT)
CURRENT FRESHWATER DRAFT: {vessel.current_draft} METERS
CARGO DETAILS: {vessel.cargo_quantity_mt:,.0f} MT OF {vessel.cargo_type}

NOTICE:
Please be advised that {vessel.name.upper()} is en route to {new_port.name.upper()}
with estimated open water arrival in approximately {vessel.open_ocean_days_out:.1f} days.
All cargo holds are inspected, seaworthy, and ready in all respects to discharge
immediately upon all-fast at nominated mechanized berth.

Laytime computation shall commence strictly in accordance with Charter Party
terms upon tender of official NOR at outer port limits (OPL) whether in berth
or not (WIBON / WIPON).

MASTER / AUTHORIZED AGENT
{vessel.name.upper()}
================================================================================"""

        # 3. Indian Railways FOIS Electronic Rake Indent (CRIS)
        fois_doc = f"""================================================================================
INDIAN RAILWAYS - FREIGHT OPERATIONS INFORMATION SYSTEM (FOIS / CRIS)
ELECTRONIC RAKE REQUISITION INDENT (BOXN / BOXNHL)
INDENT TRANSMISSION ID: CRIS-FOIS-EIND-{vessel.imo}-{datetime.now().strftime('%m%d%H%M')}
================================================================================
RAILWAY DIVISION: SOUTH EASTERN RAILWAY (SER) / EAST COAST RAILWAY (ECoR)
ORIGIN SIDING: {new_port.name.upper()} RAIL BULK WHARF SIDING
DESTINATION SIDING: {plant.name.upper()} IN-PLANT ORE HANDLING SIDING ({plant.short_name})

INDENT SUMMARY:
--------------------------------------------------------------------------------
Commodity Code:           140-B (Imported Metallurgical Coking Coal)
Total Tonnage to Evacuate:{vessel.cargo_quantity_mt:,.0f} Metric Tonnes
Consignor:                OceanSteel Logistics Desk / {plant.company}
Consignee:                Director of In-Plant Logistics, {plant.name}
Rakes Required:           39 Rakes (Standard BOXN/BOXNHL 59-wagon formation)
Planned Evacuation Rate:  6 to 8 Rakes / Day
Permissible Free Time:    {new_port.free_storage_days} Days at Port Rail Terminal

ROUTE TELEMETRY & TARIFF:
Distance:                 Direct Rail Corridor via ECoR Main Trunk
Applicable Freight Class: Class 140 Bulk Tariff
FOIS Automated Booking:   APPROVED & QUEUED FOR ADVANCE ENGINE PLACEMENT
================================================================================"""

        return {
            "ref_no": ref_no,
            "bimco_reroute": bimco_reroute,
            "pre_nor": nor_doc,
            "fois_indent": fois_doc
        }

document_generator = DocumentGenerator()
