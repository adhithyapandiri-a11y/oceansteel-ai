# Smart India Hackathon 2026 (SIH 2026) — Complete Project Deck Context

**Hackathon Round:** Internal Hackathon  
**Problem Statement ID:** `SIH262006`  
**Problem Statement Title:** Model for Optimized Vessel Chartering and Bulk Cargo Procurement from overseas to East Coast of India  
**Theme:** Logistics / Supply Chain / Smart Automation / Maritime & Railways  
**Category:** Software  

### Team Members
- **Sai**
- **Aryan Sirohi**
- **Adhithya Pandiri**
- **Shreeya C**
- **Hrishant Malviya**
- **Umair Shaikh**

---

## Slide 1: Title & Administrative Metadata
* **Project Name:** OceanSteel AI
* **Objective:** Autonomous decision support system and analytical command center to optimize bulk raw material chartering (coking coal, PCI coal, iron ore, flux) imported across the Indian Ocean / Bay of Bengal to the East Coast of India for inland and coastal steel manufacturing plants.

---

## Slide 2: Proposed Solutions & Core Innovations

### Proposed Solution
**OceanSteel AI** is an intelligent web-based decision support system and analytical dashboard that combines machine learning freight forecasting with real-time port optimization to dramatically reduce raw material import costs for Indian steel plants.

### 4 Groundbreaking Innovations
1. **First-of-its-Kind Maritime-to-Inland Telemetry Bridge:**  
   Unifies real-time maritime vessel positioning (AIS) with Indian Railways freight wagon availability (FOIS/CRIS) into a single command dashboard.
2. **Dynamic Total Landed Cost (TLC) Optimization:**  
   Replaces static port selection with a real-time linear programming decision solver (PuLP / OR-Tools).
3. **Prescriptive Rerouting Engine (Not Just Descriptive Tracking):**  
   Automatically triggers automated **"DIVERT"** signals 10–14 days in advance while the vessel is still in open water (Indian Ocean / Malacca Strait / Bay of Bengal), bypassing anchorage queues entirely.  
   *Condition:* $\text{Demurrage Saved} > \text{Extra Sea Fuel} + \text{Inland Rail Freight Differential} + \text{Port Handling Delta}$.
4. **Machine Learning Freight Rate Forecasting:**  
   Uses predictive ML ensemble models (XGBoost / LSTM / LightGBM) trained on Baltic Dry Index (BDI) and Baltic Capesize Index (BCI) trends for 14–30 day forward spot rate predictions.
5. **Unified Geospatial Dashboard:**  
   Full-stack FastAPI + Leaflet GIS + Tailwind CSS interface integrating live AIS tracking, port queue telemetry, and rail freight tariffs into a single pane of glass.

---

## Slide 3: Technical Approach

1. **Open & Standard Protocols:**  
   Integrates with established enterprise data streams using standard REST/WebSocket protocols (AISStream / NMEA 0183 for maritime positioning and CRIS REST APIs for Indian Railways FOIS telemetry).
2. **Lightweight Stack & Scalability:**  
   Built on a high-throughput Python FastAPI backend and modern frontend, capable of handling low-latency geospatial rendering and real-time mixed-integer linear programming calculations (PuLP / SciPy / COIN-OR CBC).
3. **Modular Data Fallback:**  
   Includes high-fidelity offline mock telemetry seeds to ensure 100% continuous decision support even during external API rate limits or network downtime during live hackathon demonstrations.

---

## Slide 4: Feasibility, Viability & Operational Strategy

### Critical Industry Challenges Solved
- Logistics managers at steel plants must log into 4–5 unlinked platforms daily (MarineTraffic, CRIS FOIS, port trust portals, ERP spreadsheets).
- **No single platform in India connects sea freight data to rail freight data.**
- Tools like MarineTraffic, Kpler, or VesselFinder are strictly descriptive — they tell you *where* a ship is, but never *what to do about it*.
- Existing maritime software evaluates port congestion in isolation from landside realities (e.g. railway wagon shortages, plant stockpile buffers).
- Legacy ERP systems (like SAP SCM) store static contract rates and lack predictive market intelligence.

### Commercial Feasibility & High ROI
- **Massive Cost Reduction:** A single avoided 5-day port demurrage delay saves **$75,000 to $150,000 USD** per Capesize voyage.
- **Immediate Payback:** The system pays for its entire annual implementation cost after optimizing just a single raw material shipment.

### Operational Strategy
1. **Real-Time Data Fusion:** Continuously stream vessel positions via AIS and inland rail wagon availability from Indian Railways FOIS.
2. **Queue & Delay Forecasting:** 14-day advance alerting before vessels cross outer port limits (OPL).
3. **Linear Programming Optimization Engine:**
   $$\min \text{Total Cost} = \text{Ocean Freight} + \text{Port Demurrage} + \text{Inland Rail Tariff (FOIS)} + \text{Port Storage Fines}$$
4. **Actionable Command Center:** Provide chartering officers with a single-click recommendation card.
5. **Automated Notice Generation:** Automatically generate standardized **Notice of Readiness (NOR)** and **BIMCO Charter Party Rerouting Documentation** to instantly communicate with ship captains and port authorities.

---

## Slide 5: National & Economic Impact

1. **National Logistics Policy (NLP) Alignment:**  
   India’s logistics cost currently stands at **~13–14% of GDP**, compared to **8–9% in developed economies**. This high cost reduces global competitiveness. OceanSteel AI directly lowers raw material supply chain costs per ton, accelerating the NLP goal to bring logistics costs down to single digits.
2. **Preserving India's Foreign Exchange (Forex) Reserves:**  
   Demurrage penalties on foreign-flagged Capesize bulk carriers must be settled in **US Dollars**. Preventing avoidable vessel delays saves millions of dollars annually, directly preserving national Forex reserves.
3. **National Steel Policy Target (300 MTPA):**  
   Supports India's vision to scale crude steel production capacity to **300 Million Tonnes Per Annum (MTPA)** by 2030 by preventing raw material stockouts and optimizing blast furnace feedstock deliveries.

---

## Slide 6: Legal Precedents & Research References

### Legal Precedents & Indian Port Incident References
1. **Calcutta High Court Ruling:**  
   *Steel Authority of India Ltd. (SAIL) vs. Vizag Seaport Private Ltd.* (2026)  
   [https://indiankanoon.org/doc/171502422/](https://indiankanoon.org/doc/171502422/)  
   *Key Takeaway:* Affirms the charterer’s legal right under charter party liberties clauses to re-nominate a discharge port to mitigate unreasonable berth delays.
2. **Supreme Court of India Landmark Ruling on Port Demurrage Liabilities:**  
   *Union of India & Anr. vs. Indian Inland Waterways & Ors.* (2020)  
   [https://main.sci.gov.in/supremecourt/2012/17957/17957_2012_33_1501_20697_Judg_12-Feb-2020.pdf](https://main.sci.gov.in/supremecourt/2012/17957/17957_2012_33_1501_20697_Judg_12-Feb-2020.pdf)  
   *Key Takeaway:* Sets precedent on mitigating demurrage liabilities through proactive diversion and inland intermodal coordination.
3. **Ministry of Ports, Shipping and Waterways:**  
   Directorate General of Shipping (DGS) Orders on Demurrage & Detention Waivers during extraordinary congestion and coastal congestion mitigation.

### Academic & Research Publications
1. **Analyzing Port Delays and Their Impact on Last-Mile Logistics:**  
   *International Advanced Research Journal in Science, Engineering and Technology (IARJSET, 2025)*  
   [https://iarjset.com/upload/2025/january-25/IARJSET-23.pdf](https://iarjset.com/upload/2025/january-25/IARJSET-23.pdf)
2. **Identifying Port Congestion and Evaluating Its Impact on Maritime Logistics:**  
   *ResearchGate / Sahu et al.*  
   [https://www.researchgate.net/publication/362849182_Port_Congestion_Analysis](https://www.researchgate.net/publication/362849182_Port_Congestion_Analysis)
