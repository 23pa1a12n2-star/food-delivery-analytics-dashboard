import pandas as pd
import csv

# =====================================================================
# CSV 1: Phase 1 to Phase 4 Step-by-Step Methodology
# =====================================================================
methodology_data = [
    {
        "Phase": "Phase 1: Data Collection & Strategy",
        "Step_Name": "1.1 Initial Data Load & Inspection",
        "Objective": "Understand the raw dataset structure and identify missing fields.",
        "Action_Taken": "Loaded 'food_delivery_data.csv' using Python (pandas). Computed row count, column types, null values, and summary statistics.",
        "Technical_Details": "df.shape, df.isnull().sum(), df.describe(). Identified 0 nulls, 7 raw columns. Noticed missing demographic/rating data required by stakeholders.",
        "Result_Outcome": "Established the foundation. Documented missing fields inside PROJECT_LOG.md to address in Phase 2."
    },
    {
        "Phase": "Phase 1: Data Collection & Strategy",
        "Step_Name": "1.2 Stakeholder Alignment",
        "Objective": "Ensure the analysis targets specific business goals.",
        "Action_Taken": "Mapped out goals for Rahul (Trends), Priya (Efficiency), and Neha (Experience).",
        "Technical_Details": "Created a Stakeholder Alignment Matrix mapping columns to personas.",
        "Result_Outcome": "Project direction focused purely on actionable business insights rather than random data plotting."
    },
    {
        "Phase": "Phase 2: Data Preparation & KPI Definition",
        "Step_Name": "2.1 Demographic Data Simulation",
        "Objective": "Fill gaps in user demographics for requested visual analysis.",
        "Action_Taken": "Generated synthetic columns for 'Age Group' and 'Restaurant Segment'.",
        "Technical_Details": "Used np.random.choice() with a fixed seed (42) to randomly distribute values like '18-25', 'Casual', 'Premium' across the 50k rows.",
        "Result_Outcome": "df enriched with 'Age Group' and 'Restaurant Segment' for Rahul's demographic charts."
    },
    {
        "Phase": "Phase 2: Data Preparation & KPI Definition",
        "Step_Name": "2.2 Business Rules Application",
        "Objective": "Create logical dimensions based on existing quantifiable data.",
        "Action_Taken": "Derived 'Company Type' (Corporate vs Individual) and 'Customer Rating' (1-5 stars) and computed 'Total Revenue'.",
        "Technical_Details": "Company Type created by splitting 'Order Value' at the median (Rs 673). Ratings derived via inverse-mapping: Delivery <20 min = 5 stars, >50 min = 1 star. Total Revenue = Order Value + Delivery Fee.",
        "Result_Outcome": "Generated the final 'final_enriched_data.csv' containing all 12 necessary columns."
    },
    {
        "Phase": "Phase 3: Visualization Architecture",
        "Step_Name": "3.1 Programmatic Chart Generation",
        "Objective": "Visualize the enriched dataset across 9 required dimensions.",
        "Action_Taken": "Wrote a Python script using matplotlib and seaborn to render bar charts, histograms, and boxplots.",
        "Technical_Details": "Used sns.countplot(), sns.boxplot(), and sns.histplot(). Added titles, labels, and formatted text directly onto the plots.",
        "Result_Outcome": "Outputted 9 high-resolution PNG files into the '/visualizations/' folder."
    },
    {
        "Phase": "Phase 3: Visualization Architecture",
        "Step_Name": "3.2 Insight Extraction",
        "Objective": "Translate visual patterns into 1-sentence business contexts.",
        "Action_Taken": "Analyzed the shape of the charts (e.g., flat cuisine distribution, heavily skewed delivery times) to write focused insights.",
        "Technical_Details": "Summarized visual skews into qualitative statements (e.g., '40-60 min delivery bottleneck').",
        "Result_Outcome": "Created 'PHASE3_INSIGHTS.md' to bridge the gap between technical charts and business logic."
    },
    {
        "Phase": "Phase 4: Analysis & Recommendations",
        "Step_Name": "4.1 Stakeholder Strategy Synthesis",
        "Objective": "Draft actionable recommendations to fix identified problems.",
        "Action_Taken": "Addressed each persona: Marketing combos for Rahul, Logistics overhaul for Priya, Compensation tiers for Neha.",
        "Technical_Details": "Combined KPI numbers with insights to formulate the 'Stakeholder Strategy Report'.",
        "Result_Outcome": "Delivered 9 data-backed strategic recommendations."
    },
    {
        "Phase": "Phase 4: Analysis & Recommendations",
        "Step_Name": "4.2 Executive Summary Construction",
        "Objective": "Condense the entire project finding into a 200-word brief for leadership.",
        "Action_Taken": "Summarized top 3 findings, isolated the #1 impact lever (logistics overhaul), and delivered a hard 'NO-GO' on rapid expansion.",
        "Technical_Details": "Focused entirely on bottom-line impact (saving the 2.6/5 customer rating before scaling).",
        "Result_Outcome": "Finalized PROJECT_LOG.md with the concluding strategic narrative."
    }
]

# =====================================================================
# CSV 2: Phase 5 Tableau Dashboard Build Instructions
# =====================================================================
tableau_instructions = [
    {
        "Dashboard_Component": "1. Data Connection",
        "Tableau_Step": "Import Dataset",
        "Data_Fields_Used": "All",
        "Chart_Type": "N/A",
        "Instruction_Details": "1. Open Tableau. 2. Click 'Text file' under Connect. 3. Select 'final_enriched_data.csv'. 4. Go to 'Sheet 1'."
    },
    {
        "Dashboard_Component": "Chart 1: KPI Summary",
        "Tableau_Step": "Create Text KPIs",
        "Data_Fields_Used": "Order ID, Total Revenue",
        "Chart_Type": "Text Table",
        "Instruction_Details": "1. Drag 'Total Revenue' (Sum) to Text. 2. Drag 'Order Value' (Average) to Text. 3. Drag 'Order ID' (Count Distinct) to Text. 4. Click the 'Text' shelf to format the font size (make Revenue large and bold)."
    },
    {
        "Dashboard_Component": "Chart 2: Flavors Across Cities",
        "Tableau_Step": "Grouped Bar Chart",
        "Data_Fields_Used": "City, Cuisine, Order ID",
        "Chart_Type": "Bar Chart",
        "Instruction_Details": "1. Drag 'City' to Columns. 2. Drag 'Order ID' (Count) to Rows. 3. Drag 'Cuisine' to Color. 4. Ensure Bar chart is selected in Marks. 5. Set View to 'Entire View'."
    },
    {
        "Dashboard_Component": "Chart 3: Order Distribution",
        "Tableau_Step": "Segmented Bar Chart",
        "Data_Fields_Used": "Age Group, Rest. Segment, Order ID",
        "Chart_Type": "Bar Chart",
        "Instruction_Details": "1. Drag 'Age Group' to Columns. 2. Drag 'Order ID' (Count) to Rows. 3. Drag 'Restaurant Segment' to Color. 4. Turn on Mark Labels (click 'T' on toolbar)."
    },
    {
        "Dashboard_Component": "Chart 4: Cuisine Preferences",
        "Tableau_Step": "Pie Chart",
        "Data_Fields_Used": "Cuisine, Order ID",
        "Chart_Type": "Pie",
        "Instruction_Details": "1. Change Marks drop-down to 'Pie'. 2. Drag 'Cuisine' to Color. 3. Drag 'Order ID' (Count) to Angle. 4. Drag 'Order ID' (Count) & 'Cuisine' to Label. 5. Quick Table Calculation on Label -> Percent of Total."
    },
    {
        "Dashboard_Component": "Chart 5: Operational Analysis",
        "Tableau_Step": "Side-by-Side Bars",
        "Data_Fields_Used": "Meal Type, Company Type, Order ID",
        "Chart_Type": "Bar Chart",
        "Instruction_Details": "1. Drag 'Meal Type' to Columns. 2. Drag 'Company Type' to Columns (next to Meal Type). 3. Drag 'Order ID' (Count) to Rows. 4. Drag 'Company Type' to Color."
    },
    {
        "Dashboard_Component": "Chart 6: Customer Satisfaction",
        "Tableau_Step": "Box & Whisker Plot",
        "Data_Fields_Used": "Meal Type, Customer Rating",
        "Chart_Type": "Boxplot",
        "Instruction_Details": "1. Drag 'Meal Type' to Columns. 2. Drag 'Customer Rating' to Rows. 3. Crucial: Go to Analysis menu and uncheck 'Aggregate Measures'. 4. Use 'Show Me' panel and select Box-and-Whisker Plot."
    },
    {
        "Dashboard_Component": "Chart 7: City Demand",
        "Tableau_Step": "Sorted Bar Chart",
        "Data_Fields_Used": "City, Order ID",
        "Chart_Type": "Bar Chart",
        "Instruction_Details": "1. Drag 'City' to Columns. 2. Drag 'Order ID' (Count) to Rows. 3. Click the 'Sort Descending' icon on the toolbar. 4. Drag 'Order ID' (Count) to Label."
    },
    {
        "Dashboard_Component": "Chart 8: Revenue Contribution",
        "Tableau_Step": "Revenue Bar Chart",
        "Data_Fields_Used": "Meal Type, Total Revenue",
        "Chart_Type": "Bar Chart",
        "Instruction_Details": "1. Drag 'Meal Type' to Columns. 2. Drag 'Total Revenue' (Sum) to Rows. 3. Change format on Revenue axis to Currency (Custom) -> No decimal places."
    },
    {
        "Dashboard_Component": "Chart 9: Delivery Performance",
        "Tableau_Step": "Histogram View",
        "Data_Fields_Used": "Time Taken for Delivery",
        "Chart_Type": "Histogram",
        "Instruction_Details": "1. Right-click 'Time Taken for Delivery' -> Create -> Bins (set bin size to 5 mins). 2. Drag this new Bin field to Columns. 3. Drag 'Time Taken for Delivery' (Count) to Rows. 4. You will clearly see the 40-60 min spike."
    },
    {
        "Dashboard_Component": "Final: Dashboard Layout",
        "Tableau_Step": "Assemble Canvas",
        "Data_Fields_Used": "All Sheets",
        "Chart_Type": "Dashboard",
        "Instruction_Details": "1. Click 'New Dashboard' icon at the bottom. 2. Set 'Size' to Automatic. 3. Drag a 'Horizontal Container' to the top and place the KPI Text sheet here. 4. Drag charts 8 & 9 below to highlight Revenue & Delivery bottlenecks prominently. 5. Make all filters 'Apply to all using this data source'."
    }
]

df_methodology = pd.DataFrame(methodology_data)
df_tableau = pd.DataFrame(tableau_instructions)

df_methodology.to_csv("project_methodology_phases_1_to_4.csv", index=False, quoting=csv.QUOTE_ALL)
df_tableau.to_csv("tableau_dashboard_instructions_phase_5.csv", index=False, quoting=csv.QUOTE_ALL)

print("CSVs generated successfully.")
