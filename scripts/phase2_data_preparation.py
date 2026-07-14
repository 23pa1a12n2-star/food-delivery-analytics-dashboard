
"""
Phase 2: Data Preparation & KPI Definition
============================================
Project: Food Ordering Behaviour & Consumer Trends
Stakeholder Alignment:
  - Rahul Sharma (Analyst): Age Group & Restaurant Segment enable demographic/segment analysis
  - Priya Mehta (Ops): Customer Rating tied to delivery time reveals operational impact
  - Neha Reddy (Customer): Rating system reflects customer satisfaction perspective
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
print("=" * 70)
print("  PHASE 2: DATA PREPARATION & KPI DEFINITION")
print("=" * 70)

df = pd.read_csv("food_delivery_data.csv")
print(f"\n✅ Loaded dataset: {df.shape[0]:,} rows × {df.shape[1]} columns")

# ─────────────────────────────────────────────
# 2. DATA ENRICHMENT — Synthetic Columns
# ─────────────────────────────────────────────
print("\n" + "─" * 70)
print("  STEP 1: DATA ENRICHMENT (Adding Synthetic Columns)")
print("─" * 70)

# Set seed for reproducibility
np.random.seed(42)

# 2a. Age Group — random distribution across 4 demographic bands
age_groups = ['18-25', '26-35', '36-50', '50+']
df['Age Group'] = np.random.choice(age_groups, size=len(df))
print(f"\n✅ Added 'Age Group' column with values: {age_groups}")
print(f"   Distribution:")
for ag, count in df['Age Group'].value_counts().sort_index().items():
    print(f"     {ag:>8s}: {count:>6,} ({count/len(df)*100:.1f}%)")

# 2b. Restaurant Segment — random distribution across 3 segments
restaurant_segments = ['Casual', 'Premium', 'Fast-Food']
df['Restaurant Segment'] = np.random.choice(restaurant_segments, size=len(df))
print(f"\n✅ Added 'Restaurant Segment' column with values: {restaurant_segments}")
print(f"   Distribution:")
for rs, count in df['Restaurant Segment'].value_counts().sort_index().items():
    print(f"     {rs:>10s}: {count:>6,} ({count/len(df)*100:.1f}%)")

# 2c. Company Type — derived from Order Value (median split)
median_order_value = df['Order Value'].median()
df['Company Type'] = df['Order Value'].apply(
    lambda x: 'Corporate' if x >= median_order_value else 'Individual'
)
print(f"\n✅ Added 'Company Type' column (median threshold: ₹{median_order_value:.2f})")
print(f"   Distribution:")
for ct, count in df['Company Type'].value_counts().items():
    print(f"     {ct:>12s}: {count:>6,} ({count/len(df)*100:.1f}%)")

# 2d. Customer Rating — inversely mapped from delivery time
def assign_rating(time_taken):
    """
    Maps delivery time (minutes) to a 1-5 rating scale.
    Lower delivery time = higher satisfaction rating.
    
    Rating Logic:
      5 ★★★★★  — < 20 min  (Exceptional)
      4 ★★★★☆  — 20-30 min (Good)
      3 ★★★☆☆  — 30-40 min (Average)
      2 ★★☆☆☆  — 40-50 min (Below Average)
      1 ★☆☆☆☆  — > 50 min  (Poor)
    """
    if time_taken < 20:
        return 5
    elif time_taken <= 30:
        return 4
    elif time_taken <= 40:
        return 3
    elif time_taken <= 50:
        return 2
    else:
        return 1

df['Customer Rating'] = df['Time Taken for Delivery'].apply(assign_rating)
print(f"\n✅ Added 'Customer Rating' column (1-5 scale, derived from delivery time)")
print(f"   Distribution:")
for rating in sorted(df['Customer Rating'].unique(), reverse=True):
    count = (df['Customer Rating'] == rating).sum()
    stars = "★" * rating + "☆" * (5 - rating)
    print(f"     {stars} ({rating}): {count:>6,} ({count/len(df)*100:.1f}%)")

# ─────────────────────────────────────────────
# 3. KPI CALCULATIONS
# ─────────────────────────────────────────────
print("\n" + "─" * 70)
print("  STEP 2: KPI CALCULATIONS")
print("─" * 70)

# 3a. Total Revenue = Sum of (Order Value + Delivery Fee)
df['Total Revenue'] = df['Order Value'] + df['Delivery Fee']
total_revenue = df['Total Revenue'].sum()
print(f"\n📊 KPI 1 — Total Revenue:")
print(f"   ₹{total_revenue:,.2f}")

# 3b. Average Order Value (AOV)
aov = df['Order Value'].mean()
print(f"\n📊 KPI 2 — Average Order Value (AOV):")
print(f"   ₹{aov:,.2f}")

# 3c. Average Delivery Time by City
print(f"\n📊 KPI 3 — Average Delivery Time by City:")
avg_delivery_by_city = df.groupby('City')['Time Taken for Delivery'].mean().sort_values()
for city, avg_time in avg_delivery_by_city.items():
    bar = "█" * int(avg_time)
    print(f"   {city:>12s}: {avg_time:>6.2f} min  {bar}")

# 3d. Order Volume by City
print(f"\n📊 KPI 4 — Order Volume by City:")
order_volume_by_city = df.groupby('City')['Order ID'].count().sort_values(ascending=False)
for city, volume in order_volume_by_city.items():
    bar = "█" * (volume // 500)
    print(f"   {city:>12s}: {volume:>6,} orders  {bar}")

# ─────────────────────────────────────────────
# 4. ADDITIONAL KPIs (Stakeholder-Specific)
# ─────────────────────────────────────────────
print("\n" + "─" * 70)
print("  STEP 3: STAKEHOLDER-SPECIFIC INSIGHTS")
print("─" * 70)

# For Rahul (Analyst) — Top cuisine by revenue
print(f"\n🔎 For Rahul (Analyst) — Revenue by Cuisine:")
rev_by_cuisine = df.groupby('Cuisine')['Total Revenue'].sum().sort_values(ascending=False)
for cuisine, rev in rev_by_cuisine.items():
    print(f"   {cuisine:>14s}: ₹{rev:>12,.2f}")

# For Priya (Ops) — Avg delivery time by meal type
print(f"\n🔎 For Priya (Ops) — Avg Delivery Time by Meal Type:")
avg_del_by_meal = df.groupby('Meal Type')['Time Taken for Delivery'].mean().sort_values()
for meal, avg_t in avg_del_by_meal.items():
    print(f"   {meal:>15s}: {avg_t:.2f} min")

# For Neha (Customer) — Avg rating by meal type
print(f"\n🔎 For Neha (Customer) — Avg Customer Rating by Meal Type:")
avg_rating_by_meal = df.groupby('Meal Type')['Customer Rating'].mean().sort_values(ascending=False)
for meal, avg_r in avg_rating_by_meal.items():
    print(f"   {meal:>15s}: {avg_r:.2f} / 5.00")

# ─────────────────────────────────────────────
# 5. PREVIEW & SAVE
# ─────────────────────────────────────────────
print("\n" + "─" * 70)
print("  STEP 4: ENRICHED DATASET PREVIEW")
print("─" * 70)

# Show updated schema
print(f"\n📋 Updated Schema: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"   Columns: {list(df.columns)}")

# Preview first 5 rows
print(f"\n📋 First 5 rows of enriched dataset:\n")
preview_cols = ['Order ID', 'Order Value', 'Delivery Fee', 'Cuisine', 'Meal Type',
                'City', 'Time Taken for Delivery', 'Age Group', 'Restaurant Segment',
                'Company Type', 'Customer Rating', 'Total Revenue']
print(df[preview_cols].head().to_string(index=False))

# Save enriched dataset
output_file = "food_delivery_enriched.csv"
df.to_csv(output_file, index=False)
print(f"\n✅ Enriched dataset saved to: {output_file}")
print(f"   Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

print("\n" + "=" * 70)
print("  ✅ PHASE 2 COMPLETE — Data is ready for Phase 3 (Visualization)")
print("=" * 70)
