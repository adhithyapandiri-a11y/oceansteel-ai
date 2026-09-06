# OceanSteel AI: Mathematical Formulation & Optimization Model

**Problem Statement ID:** `SIH262006`  
**System:** Dynamic Total Landed Cost (TLC) Optimizer for Raw Material Imports

---

## 1. Problem Definition & Notation

Let:
* $\mathcal{V}$ be the set of active incoming bulk carrier vessels (Capesize, Panamax, Supramax).
* $\mathcal{P}$ be the set of candidate discharge ports along the East Coast of India:
  $$\mathcal{P} = \{\text{Paradip (PPT)}, \text{Dhamra}, \text{Visakhapatnam (VPT)}, \text{Gangavaram (GPL)}, \text{Haldia (HDC)}, \text{Krishnapatnam (KPCL)}\}$$
* $\mathcal{S}$ be the set of inland/coastal destination steel plants:
  $$\mathcal{S} = \{\text{SAIL Rourkela (RSP)}, \text{SAIL Bokaro (BSL)}, \text{SAIL Bhilai (BSP)}, \text{RINL Vizag (VSP)}, \text{Tata Steel Kalinganagar}\}$$

For a given vessel $v \in \mathcal{V}$ carrying cargo quantity $Q_v$ (in metric tonnes) destined for steel plant $s \in \mathcal{S}$, let $p_0 \in \mathcal{P}$ denote the initial nominated baseline discharge port.

---

## 2. Decision Variables

For each candidate port $p \in \mathcal{P}$:
$$x_p \in \{0, 1\} \quad \text{where } x_p = 1 \text{ if port } p \text{ is selected for cargo discharge, } 0 \text{ otherwise.}$$

---

## 3. Cost Components of Total Landed Cost (TLC)

For any candidate port $p \in \mathcal{P}$, the Total Landed Cost $\text{TLC}(p)$ in USD is formulated as:

$$\text{TLC}(p) = C_{\text{ocean}} + C_{\text{bunker}}(p) + C_{\text{demurrage}}(p) + C_{\text{port\_handling}}(p) + C_{\text{rail\_freight}}(p) + C_{\text{storage\_fines}}(p)$$

### Component Breakdown:

1. **Baseline Ocean Freight ($C_{\text{ocean}}$):**
   $$C_{\text{ocean}} = Q_v \times R_{\text{ocean}}$$
   *(e.g., ~$12.50 USD/MT for Capesize from Australia to East Coast India)*

2. **Extra Open-Ocean Steaming / Bunker Fuel ($C_{\text{bunker}}(p)$):**
   $$C_{\text{bunker}}(p) = \Delta t_{\text{sea}}(p, p_0) \times F_v \times P_{\text{VLSFO}}$$
   * $\Delta t_{\text{sea}}(p, p_0)$: Delta steaming days from current open-water waypoint to port $p$ relative to baseline $p_0$.
   * $F_v$: Vessel daily fuel burn rate (e.g. 38.5 MT/day for Capesize at 12.6 knots).
   * $P_{\text{VLSFO}}$: Spot price of Very Low Sulphur Fuel Oil (~$620 USD/MT).

3. **Port Anchorage Demurrage Penalty ($C_{\text{demurrage}}(p)$):**
   $$C_{\text{demurrage}}(p) = W_p \times D_v$$
   * $W_p$: Current anchorage waiting queue in days at port $p$.
   * $D_v$: Daily charter demurrage rate specified in charter party (e.g., $25,000 USD/day).

4. **Port Handling & Stevedoring Dues ($C_{\text{port\_handling}}(p)$):**
   $$C_{\text{port\_handling}}(p) = Q_v \times H_p$$
   * $H_p$: Tariff per MT for mechanized grab unloading, wharfage, and harbor conservancy.

5. **Inland Railway Freight ($C_{\text{rail\_freight}}(p)$):**
   $$C_{\text{rail\_freight}}(p) = Q_v \times \left( \frac{T_{\text{FOIS}}(p, s)}{\text{FX}_{\text{USD/INR}}} \right)$$
   * $T_{\text{FOIS}}(p, s)$: Indian Railways Class 140/150 bulk tariff (₹/MT) for railway distance $d(p, s)$ km.
   * $\text{FX}_{\text{USD/INR}}$: Exchange rate (~83.20 ₹/$).

6. **Port Ground Rent & Evacuation Storage Penalties ($C_{\text{storage\_fines}}(p)$):**
   Let $R_p$ be the daily BOXN rakes available at port $p$. Standard BOXN rake payload is $\kappa_{\text{rake}} \approx 3,850\text{ MT}$ (59 wagons).
   $$\text{Days to Evacuate } \tau_p = \frac{Q_v}{R_p \times \kappa_{\text{rake}}}$$
   $$C_{\text{storage\_fines}}(p) = \max(0, \tau_p - \text{FreeDays}_p) \times \left(0.5 \times Q_v\right) \times G_p$$
   * $\text{FreeDays}_p$: Free port laytime before ground rent (typically 5–6 days).
   * $G_p$: Punitive port storage fine per MT per day ($0.15–$0.22 USD/MT/day).

---

## 4. Optimization Formulation (Mixed-Integer Linear Program)

$$\min_{\{x_p\}} \sum_{p \in \mathcal{P}} \text{TLC}(p) \cdot x_p$$

### Constraints:

1. **Uniqueness Constraint:** Exactly one discharge port must be selected:
   $$\sum_{p \in \mathcal{P}} x_p = 1$$

2. **Vessel Draft Permissibility Constraint:**
   $$x_p \cdot \text{Draft}_v \le \text{MaxDraft}_p \quad \forall p \in \mathcal{P}$$
   *Example:* For *MV Steel Horizon* with $17.5\text{m}$ draft:
   * $\text{MaxDraft}(\text{Dhamra}) = 18.5\text{m} \implies \text{Feasible}$
   * $\text{MaxDraft}(\text{Paradip}) = 18.0\text{m} \implies \text{Feasible}$
   * $\text{MaxDraft}(\text{Haldia}) = 8.5\text{m} \implies \text{INFEASIBLE } (x_{\text{Haldia}} = 0)$

3. **Steel Plant Stockout Runway Constraint:**
   Let $T_{\text{turnaround}}(p) = t_{\text{sea}} + \Delta t_{\text{sea}}(p) + W_p + \frac{Q_v}{\text{DischargeRate}_p} + t_{\text{rail}}(p, s)$.
   $$x_p \cdot T_{\text{turnaround}}(p) \le \text{StockpileRunway}_s + \epsilon \quad \forall p \in \mathcal{P}$$
   Guarantees that raw material arrives at the blast furnace before remaining plant inventory is exhausted.

---

## 5. Prescriptive Rerouting Trigger (Open-Water Decision Gate)

At $10 \le t_{\text{sea}} \le 14$ days before port arrival, OceanSteel AI executes the prescriptive diversion rule:

$$\text{Trigger DIVERT to Port } p^* \iff \text{Demurrage Saved}(p_0, p^*) > \Delta \text{Bunker Fuel} + \Delta \text{Rail Freight} + \Delta \text{Port Handling}$$

$$\text{Net Savings} = \text{TLC}(p_0) - \text{TLC}(p^*)$$

When $\text{Net Savings} > \$25,000\text{ USD}$, the system automatically issues:
1. BIMCO Charter Party Rerouting Directive to Ship Master.
2. Advance Master's Notice of Readiness (Pre-NOR).
3. Indian Railways FOIS Electronic Rake Indent (e-Indent).
