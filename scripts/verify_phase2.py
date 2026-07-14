
import pandas as pd

df = pd.read_csv('food_delivery_enriched.csv')
print('ENRICHED DATASET SHAPE:', df.shape)
print()
print('COLUMNS:', list(df.columns))
print()
print('FIRST 5 ROWS:')
print(df.head().to_string())
print()
print('=== NEW COLUMN DISTRIBUTIONS ===')
print()
print('--- Age Group ---')
for k, v in df['Age Group'].value_counts().sort_index().items():
    pct = v / len(df) * 100
    print(f'  {k}: {v} ({pct:.1f}%)')
print()
print('--- Restaurant Segment ---')
for k, v in df['Restaurant Segment'].value_counts().sort_index().items():
    pct = v / len(df) * 100
    print(f'  {k}: {v} ({pct:.1f}%)')
print()
print('--- Company Type ---')
for k, v in df['Company Type'].value_counts().items():
    pct = v / len(df) * 100
    print(f'  {k}: {v} ({pct:.1f}%)')
print()
print('--- Customer Rating ---')
for r in sorted(df['Customer Rating'].unique(), reverse=True):
    c = (df['Customer Rating'] == r).sum()
    pct = c / len(df) * 100
    print(f'  Rating {r}: {c} ({pct:.1f}%)')
print()
print('=== KPIs ===')
total_rev = df['Total Revenue'].sum()
aov = df['Order Value'].mean()
print(f'Total Revenue: Rs {total_rev:,.2f}')
print(f'Avg Order Value (AOV): Rs {aov:,.2f}')
print()
print('--- Avg Delivery Time by City ---')
for city, t in df.groupby('City')['Time Taken for Delivery'].mean().sort_values().items():
    print(f'  {city}: {t:.2f} min')
print()
print('--- Order Volume by City ---')
for city, v in df.groupby('City')['Order ID'].count().sort_values(ascending=False).items():
    print(f'  {city}: {v}')
print()
print('--- Avg Rating by Meal Type ---')
for m, r in df.groupby('Meal Type')['Customer Rating'].mean().sort_values(ascending=False).items():
    print(f'  {m}: {r:.2f}')
print()
print('--- Revenue by Cuisine ---')
for cu, r in df.groupby('Cuisine')['Total Revenue'].sum().sort_values(ascending=False).items():
    print(f'  {cu}: Rs {r:,.2f}')
