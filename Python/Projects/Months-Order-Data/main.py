import os
import pandas as pd

# ==========================================
# Load CSV File
# ==========================================

current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "orders.csv")

df = pd.read_csv(csv_path)

# ==========================================
# PART 1 - Explore Data
# ==========================================

print("=" * 60)
print("📦 AMAZON SALES ANALYZER")
print("=" * 60)

print(f"Total Orders          : {len(df)}")
print(f"Number of Rows        : {df.shape[0]}")
print(f"Number of Columns     : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ==========================================
# PART 2 - Revenue
# ==========================================

print("\n" + "=" * 60)
print("PART 2 - REVENUE")
print("=" * 60)

df["Revenue"] = df["Price"] * df["Quantity"]

print(df[["Customer", "Product", "Revenue"]])

# ==========================================
# PART 3 - Statistics
# ==========================================

print("\n" + "=" * 60)
print("PART 3 - STATISTICS")
print("=" * 60)

print(f"Total Revenue         : ₹{df['Revenue'].sum():,}")
print(f"Average Revenue       : ₹{df['Revenue'].mean():,.2f}")
print(f"Highest Revenue       : ₹{df['Revenue'].max():,}")
print(f"Lowest Revenue        : ₹{df['Revenue'].min():,}")

# ==========================================
# PART 4 - Filtering
# ==========================================

print("\n" + "=" * 60)
print("PART 4 - FILTERING")
print("=" * 60)

print("\nElectronics Products")
print(
    df[df["Category"] == "Electronics"][
        ["Product", "Category", "Revenue"]
    ]
)

print("\nFurniture Products")
print(
    df[df["Category"] == "Furniture"][
        ["Product", "Category", "Revenue"]
    ]
)

print("\nBangalore Orders")
print(
    df[df["City"] == "Bangalore"][
        ["Customer", "Product", "Revenue"]
    ]
)

print("\nRevenue Greater Than ₹20,000")
print(
    df[df["Revenue"] > 20000][
        ["Customer", "Product", "Revenue"]
    ]
)

# ==========================================
# PART 5 - Sorting
# ==========================================

print("\n" + "=" * 60)
print("PART 5 - SORTING")
print("=" * 60)

print("\nHighest Revenue First")
print(
    df.sort_values("Revenue", ascending=False)[
        ["Customer", "Product", "Revenue"]
    ]
)

print("\nLowest Revenue First")
print(
    df.sort_values("Revenue")[
        ["Customer", "Product", "Revenue"]
    ]
)

print("\nHighest Price First")
print(
    df.sort_values("Price", ascending=False)[
        ["Product", "Price"]
    ]
)

# ==========================================
# PART 6 - Group By
# ==========================================

print("\n" + "=" * 60)
print("PART 6 - GROUP BY")
print("=" * 60)

print("\nRevenue by City")
revenue_by_city = df.groupby("City")["Revenue"].sum()
for city, revenue in revenue_by_city.items():
    print(f"{city:<12} : ₹{revenue:,}")

print("\nRevenue by Customer")
revenue_by_customer = df.groupby("Customer")["Revenue"].sum()
for customer, revenue in revenue_by_customer.items():
    print(f"{customer:<12} : ₹{revenue:,}")

print("\nRevenue by Category")
revenue_by_category = df.groupby("Category")["Revenue"].sum()
for category, revenue in revenue_by_category.items():
    print(f"{category:<12} : ₹{revenue:,}")

print("\nOrders per City")
orders_per_city = df.groupby("City").size()
for city, count in orders_per_city.items():
    print(f"{city:<12} : {count}")

# ==========================================
# PART 7 - Business Questions
# ==========================================

print("\n" + "=" * 60)
print("PART 7 - BUSINESS QUESTIONS")
print("=" * 60)

best_customer = revenue_by_customer.idxmax()
best_customer_revenue = revenue_by_customer.max()

best_city = revenue_by_city.idxmax()
best_city_revenue = revenue_by_city.max()

best_category = revenue_by_category.idxmax()
best_category_revenue = revenue_by_category.max()

product_quantity = df.groupby("Product")["Quantity"].sum()

best_product = product_quantity.idxmax()
best_quantity = product_quantity.max()

print(f"🏆 Best Customer      : {best_customer}")
print(f"💰 Customer Revenue   : ₹{best_customer_revenue:,}")

print()

print(f"🏙️ Best City          : {best_city}")
print(f"💰 City Revenue       : ₹{best_city_revenue:,}")

print()

print(f"📦 Best Category      : {best_category}")
print(f"💰 Category Revenue   : ₹{best_category_revenue:,}")

print()

print(f"🛒 Most Sold Product  : {best_product}")
print(f"📈 Quantity Sold      : {best_quantity}")

# ==========================================
# PART 8 - Final Report
# ==========================================

print("\n" + "=" * 60)
print("📊 FINAL REPORT")
print("=" * 60)

print(f"Total Orders          : {len(df)}")
print(f"Total Revenue         : ₹{df['Revenue'].sum():,}")
print(f"Average Revenue       : ₹{df['Revenue'].mean():,.2f}")
print(f"Highest Revenue       : ₹{df['Revenue'].max():,}")
print(f"Lowest Revenue        : ₹{df['Revenue'].min():,}")

print()

print(f"Best Customer         : {best_customer}")
print(f"Best City             : {best_city}")
print(f"Best Category         : {best_category}")
print(f"Most Sold Product     : {best_product}")

print("=" * 60)

# ==========================================
# Save CSV
# ==========================================

output_path = os.path.join(current_folder, "sales_report.csv")

df.to_csv(output_path, index=False)

print("\n✅ Report saved successfully!")
print(f"📂 File Location: {output_path}")