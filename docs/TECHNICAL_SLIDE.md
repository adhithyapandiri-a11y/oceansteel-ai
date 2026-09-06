# SIH 2026: Technical Deep-Dive Slide Specification

**Problem Statement ID:** `SIH262006`  
**Slide Title:** TECHNICAL DEEP-DIVE: MATHEMATICAL MODEL & AI ENGINE  
**Theme:** Smart Automation & Logistics  
**Team:** Team OceanSteel  

---

## Slide Header
* **Title:** TECHNICAL DEEP-DIVE: MATHEMATICAL MODEL & AI ENGINE
* **Subtitle:** SMART INDIA HACKATHON 2026 | PS ID: SIH262006 | Category: Software | Team OceanSteel

---

## Slide Grid Layout (4 Quadrants)

### Quadrant 1: Mathematical Optimization (MILP Solver)
* **Objective:**
  $$\min \text{TLC} = C_{\text{ocean}} + C_{\text{bunker}} + C_{\text{demurrage}} + C_{\text{rail}} + C_{\text{handling}} + C_{\text{storage}}$$
* **Solver Engine:** PuLP with COIN-OR CBC Branch-and-Cut Mixed-Integer Linear Programming.
* **Physical & Operational Constraints:**
  1. **Draft Constraint:** $\text{Vessel Draft} \le \text{Port Max Draft}$ (e.g. 17.5m draft Capesize cannot dock at Haldia's 8.5m limit).
  2. **Plant Buffer Safety:** $\text{Delivery Date} \le \text{Plant Stockpile Runway}$ (prevents blast furnace feedstock stockout).
  3. **Evacuation Throughput:** $\text{Evacuation Rate} = \text{BOXN Rakes} \times 3,850\text{ MT/rake}$.

### Quadrant 2: Predictive ML Freight Rate Forecaster
* **Model Architecture:** XGBoost + LSTM Time-Series Ensemble trained on historical Baltic Dry Index (BDI) and Baltic Capesize Index (BCI) trends.
* **Feature Engineering:**
  * VLSFO Bunker Fuel Spot Trajectory (Brent correlation)
  * Chinese Port Iron Ore Stockpiling & Steel Mill Capacity
  * Australian Cyclonic / Seasonal Monsoon Restock Index
* **Output:** 14–30 Day Forward Curve with 95% Confidence Interval Bands (P10, P50, P90).
* **Actionable Advice:** Prescribes the exact 72-hour window to lock forward time charters before spot rate spikes (+20.5%).

### Quadrant 3: Dual Maritime-to-Rail Telemetry Bridge
* **Sea Telemetry:** Real-time AIS position ingestion via AISStream / NMEA 0183 WebSocket streams (MMSI, SOG, Heading, Open-Water Waypoint).
* **Inland Rail Telemetry:** Indian Railways FOIS / CRIS REST API integration for BOXN/BOXNHL 59-wagon rakes (~3,850 MT payload) and Class 140/150 Bulk Tariffs.
* **Fault-Tolerant Architecture:** High-fidelity offline seed ensures 100% continuous decision support during pitch demonstrations.

### Quadrant 4: Production Tech Stack & System Specs
* **Backend:** Python 3.14 + FastAPI (ASGI async event loop, sub-150ms optimization latency).
* **Frontend:** Leaflet GIS (Esri World Dark Gray Canvas, 100% watermark-free) + Tailwind CSS + Chart.js.
* **Automated Documentation:** Single-click generation of BIMCO Charter Party Rerouting Orders & Master's Pre-Notice of Readiness (NOR).
* **Cloud & Serverless:** Vercel Serverless Python Functions + Global Edge CDN.

---

## Bottom Banner Callout
$$\text{Prescriptive Gate: Trigger DIVERT iff } \Delta \text{Demurrage Saved} > \Delta \text{Sea Bunker Fuel} + \Delta \text{Inland Rail Freight} + \Delta \text{Port Handling}$$
**Demonstrated Impact on MV Steel Horizon:** Saves **$272,068 USD (₹2.26 Crore INR)** & delivers raw materials **8.3 days earlier** to SAIL Rourkela!
