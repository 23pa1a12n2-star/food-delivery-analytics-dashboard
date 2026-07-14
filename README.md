<div align="center">
  
# 🍔 Food Ordering Behaviour & Consumer Trends
### *A Structured Analysis of Choices, Logistics, and Revenue Optimization*

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458.svg?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-31A8FF.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Viz-4EACB8.svg)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard_Ready-E97627.svg?logo=tableau&logoColor=white)

</div>

---

## 📖 Project Overview
The **Food Ordering Behaviour & Consumer Trends** project is a comprehensive end-to-end data analytics and business strategy pipeline. Processing a scale of 50,000 localized orders yielding ~₹35 million in aggregate revenue, this project bridges the gap between raw data engineering, programmatic visualization, and high-level executive decision-making. 

The analysis specifically targets three distinct business personas:
- **Business Analyst (Revenue Growth):** Trends, cuisine preferences, demographic slices.
- **Operations Manager (Efficiency):** Logistics timelines, SLA optimization, fleet surging.
- **Customer (Experience):** Pricing sensitivity and platform satisfaction.

---

## ✨ Features
- **Synthetic Data Engineering:** Dynamically calculates advanced metrics (e.g., Company Type bounding, time-inversed Customer Ratings) directly via Pandas pipelines.
- **Programmatic Visual Architecture:** Computes 9 distinct visual distributions and KPI graphics mapped to stakeholder pain points via `matplotlib`/`seaborn`.
- **Actionable Strategic Synthesis:** Translates graphical skew into business bottlenecks (e.g., identifying a 40-60 min delivery SLA failure driving a 2.6/5 org-wide rating).
- **BI/Tableau Translation Playbook:** Outputs detailed CSV instructions rendering exact click-paths to reconstruct the visualizations interactively in Tableau.

---

## 📂 Folder Structure

```text
📁 
├── 📊 Data Files
│   ├── food_delivery_data.csv                 # Raw dataset (50,000 orders, 7 cols)
│   └── final_enriched_data.csv                # Final engineered dataset (12 cols)
│
├── 🐍 Pipeline Scripts
│   ├── phase2_data_preparation.py             # Feature engineering & KPI algorithms
│   ├── verify_phase2.py                       # CLI KPI & schema verification toolkit
│   ├── phase3_visualizations.py               # Generates KPI charts to /visualizations
│   └── generate_documentation_csvs.py         # Automates CSV methodology / playbook export
│
├── 📈 Outputs
│   └── visualizations/                        # 9 generated high-resolution PNG charts
│
└── 📑 Documentation & Deliverables
    ├── PROJECT_LOG.md                         # Executive Summary & Strategy Report
    ├── PHASE3_INSIGHTS.md                     # 1-Sentence analytic insight breakdown
    ├── DASHBOARD_PREVIEW.md                   # Markdown render of output charts
    ├── dashboard_logic_and_layout.txt         # Tableau implementation guide & layouts
    ├── project_methodology_phases_1_to_4.csv  # Step-by-step Python execution footprint
    └── tableau_dashboard_instructions.csv     # Tableau manual step-by-step wireframe guide
```

---

## ⚙️ Technologies Used
* **Data Processing:** General Python stacked with `pandas` and `numpy`.
* **Programmatic Data Visualization:** `matplotlib`, `seaborn`.
* **Business Intelligence (BI) Planning:** F-Pattern visual hierarchy modeling targeted for `Tableau`.
* **Strategy Frameworks:** Data-driven KPI reporting, bottleneck analysis, and tiered recommendations.

---

## 🔄 Project Workflow
The system executes via an atomic 5-Phase pipeline:
1. **Phase 1: Data Collection & Strategy** — Loaded the initial footprint and aligned metrics with specific stakeholder OKRs.
2. **Phase 2: Data Preparation & KPI Definition** — Filled tracking gaps via deterministic dimension engineering (`Age Group`, `Company Segment`, `Satisfaction Score`). 
3. **Phase 3: Visualization Architecture** — Rendered 9 critical views testing market symmetry, delivery performance, and revenue aggregation.
4. **Phase 4: Analysis & Recommendations** — Generated the 'Executive Strategy Report' prescribing actionable fixes to the discovered bottlenecks.
5. **Phase 5: Agent-Led Closure** — Handoff of cleanly architected Tableau UI/UX implementation files and data blocks.

---

## 📊 Dashboard Overview
The data is designed to be injected directly into a BI tool (like Tableau). The recommended layout follows a strict **F-Pattern hierarchy**:
* **Top Banner (The "What"):** Global filters alongside high-level KPI cards (Total Revenue, AOV, Overall Order Count).
* **Middle Section (The "Where/When"):** Horizontal matrices showing 70% of absolute platform revenue is completely isolated within Lunch & Dinner timeframes across perfectly distributed metros.
* **Bottom Section (The "Why"):** Performance Diagnosis linking the Delivery Time distributions (40-60m bottlenecks) directly to adjacent Boxplots showing failing 2.6/5 customer satisfaction correlations.

*(See `dashboard_logic_and_layout.txt` for exact configuration instructions).*

---

## 💡 Key Executive Insights
1. **Perfect Geographic & Demographic Symmetry:** Demand is uniformly distributed across all 5 metro cities (~10,000 orders each) and perfectly flat across all age demographics. Scale is easily replicable.
2. **Heavy Chronological Aggregation:** Despite demographic flatness, 70% of total commercial valuation is strictly generated via Lunch and Dinner rushes.
3. **Severe Operational Bottleneck:** The platform is plagued by a systemic logistics breakdown. Delivery times heavily stack into a 40–60 minute cluster, crashing the average platform customer rating to a dismal **2.6 / 5.0**.

---

## 🏆 Results & Conclusion
**Ultimate Recommendation: NO-GO ON EXPANSION.** 
While the company demonstrates incredibly strong, identical product-market fit across multiple metros yielding heavy ~₹35M transaction volumes, scaling currently means replicating a deeply flawed 2.6-star experience.

**Action Plan:** Hyper-surge driver fleets specifically dedicated to the dominant Lunch & Dinner blocks to crush the 40-60 minute dispatch times down to a strict `<30 minute SLA`. Restore customer ratings in existing environments effectively before launching into new operational territories.

---
