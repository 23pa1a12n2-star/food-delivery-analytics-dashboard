import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create directory for saving visualisations
out_dir = "visualizations"
os.makedirs(out_dir, exist_ok=True)

print("Loading data...")
df = pd.read_csv("food_delivery_enriched.csv")

# Set visualization style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'figure.max_open_warning': 0})

print("Generating Visualizations...")

# 1. KPI Dashboard Summary
total_rev = df['Total Revenue'].sum()
aov = df['Order Value'].mean()
total_vol = len(df)

fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('off')
kpi_text = (
    "KPI DASHBOARD SUMMARY\n\n"
    f"Total Revenue: ₹ {total_rev:,.2f}\n"
    f"Total Order Volume: {total_vol:,}\n"
    f"Average Order Value (AOV): ₹ {aov:,.2f}"
)
ax.text(0.5, 0.5, kpi_text, fontsize=16, ha='center', va='center', weight='bold',
        bbox=dict(facecolor='#f4f4f4', edgecolor='#ccc', boxstyle='round,pad=1'))
plt.title("1. KPI Executive Summary", fontsize=14, pad=15)
plt.savefig(f"{out_dir}/01_KPI_Dashboard.png", bbox_inches='tight', dpi=150)
plt.close(fig)

# 2. Flavors Across Cities
fig = plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='City', hue='Cuisine')
plt.title("2. Flavors Across Cities (Cuisine by City)", fontsize=14)
plt.xlabel("City")
plt.ylabel("Order Count")
plt.legend(title="Cuisine", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(f"{out_dir}/02_Flavors_Across_Cities.png", dpi=150)
plt.close(fig)

# 3. Order Distribution (Age Group & Restaurant Segment)
fig = plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Age Group', hue='Restaurant Segment', order=['18-25', '26-35', '36-50', '50+'])
plt.title("3. Order Distribution by Age Group and Restaurant Segment", fontsize=14)
plt.xlabel("Age Group")
plt.ylabel("Orders")
plt.legend(title="Segment", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(f"{out_dir}/03_Order_Distribution.png", dpi=150)
plt.close(fig)

# 4. Cuisine Preferences
fig = plt.figure(figsize=(8, 8))
cuisine_counts = df['Cuisine'].value_counts()
plt.pie(cuisine_counts, labels=cuisine_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("muted"))
plt.title("4. Customer Preferences Across Cuisines", fontsize=14)
plt.savefig(f"{out_dir}/04_Cuisine_Preferences.png", dpi=150)
plt.close(fig)

# 5. Operational Analysis (Company Type vs Meal Type)
fig = plt.figure(figsize=(9, 5))
sns.countplot(data=df, x='Meal Type', hue='Company Type', order=['Breakfast', 'Lunch', 'Evening Snack', 'Dinner'])
plt.title("5. Orders Across Company Type and Meal Type", fontsize=14)
plt.xlabel("Meal Type")
plt.ylabel("Number of Orders")
plt.legend(title="Company Type")
plt.tight_layout()
plt.savefig(f"{out_dir}/05_Operational_Analysis.png", dpi=150)
plt.close(fig)

# 6. Customer Satisfaction (Ratings by Meal Type)
fig = plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Meal Type', y='Customer Rating', order=['Breakfast', 'Lunch', 'Evening Snack', 'Dinner'], palette="Set2")
plt.title("6. Customer Rating Analysis by Meal Type", fontsize=14)
plt.xlabel("Meal Type")
plt.ylabel("Customer Rating (1-5)")
plt.tight_layout()
plt.savefig(f"{out_dir}/06_Customer_Satisfaction.png", dpi=150)
plt.close(fig)

# 7. City Demand (Orders by City)
fig = plt.figure(figsize=(9, 5))
city_counts = df['City'].value_counts()
sns.barplot(x=city_counts.index, y=city_counts.values, palette="viridis")
plt.title("7. Cities by Order Volume", fontsize=14)
plt.xlabel("City")
plt.ylabel("Total Orders")
for i, v in enumerate(city_counts.values):
    plt.text(i, v + 100, str(v), ha='center')
plt.tight_layout()
plt.savefig(f"{out_dir}/07_City_Demand.png", dpi=150)
plt.close(fig)

# 8. Revenue Contribution by Meal Type
fig = plt.figure(figsize=(9, 5))
rev_by_meal = df.groupby('Meal Type')['Order Value'].sum().reindex(['Breakfast', 'Lunch', 'Evening Snack', 'Dinner'])
sns.barplot(x=rev_by_meal.index, y=rev_by_meal.values, palette="rocket")
plt.title("8. Total Order Value (Revenue) by Meal Type", fontsize=14)
plt.xlabel("Meal Type")
plt.ylabel("Total Order Value (₹)")
for i, v in enumerate(rev_by_meal.values):
    plt.text(i, v + 200000, f"₹{v:,.0f}", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig(f"{out_dir}/08_Revenue_Contribution.png", dpi=150)
plt.close(fig)

# 9. Delivery Performance
fig = plt.figure(figsize=(9, 5))
sns.histplot(data=df, x='Time Taken for Delivery', bins=sorted(df['Time Taken for Delivery'].unique()), kde=True, color='purple')
plt.title("9. Distribution of Delivery Time Across Orders", fontsize=14)
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{out_dir}/09_Delivery_Performance.png", dpi=150)
plt.close(fig)

print(f"✅ Successfully generated and saved all 9 visualizations to '{os.path.abspath(out_dir)}'")
