import os
import pandas as pd
current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "sales_data.csv")
df = pd.read_csv(csv_path)

print("=" * 50)
print("Sales Data Analyzer")
print("=" * 50)

# Information 
print(f"Total Products : {len(df)}")
print(f"Average Price : {df['Price'].mean()}")
print(f"Highest price : {df['Price'].max()}")
print(f"Lowest Price : {df['Price'].min()}")
print(f"Total Quantity Sold : {df['Quantity'].sum()}")

print("=" * 50)

#Product Above 10000
print("Product Above 10000")
print("=" * 50)
print(
     df[df["Price"] > 10000][
        ["Product", "Price", "Quantity"]
    ]
)
print("=" * 50)


#Only Furniture
print("Only Furniture")
print("=" * 50)
print(
    df[df["Category"] == "Furniture"][
        ["Category", "Price", "Quantity"]
    ]
)

print("=" * 50)
print("Only Bangalore Sales")
print("=" * 50)

print(
    df[df["City"] == "Bangalore"][
        ["City", "Price", "Quantity"]
    ]
)
print("=" * 50)
print("Product sold by Rahul")
print("=" * 50)

print(
    df[df["Salesperson"] == "Rahul"][
        ["Product", "Price", "Quantity"]
    ]
)

print("=" * 50)
print("Show Product Price is greater than ₹5000")
print("=" * 50)

print(
    df[df["Price"] > 5000][
        ["Product", "Price"]
    ]
)

print("=" * 50)
print("Show products where Category is Electronics & Price is greater than ₹10,000")
print("=" * 50)

print(
    df[
        (df["Category"] == "Electronics") & 
        (df["Quantity"] > 5)
        ][
        "Product", "Quantity", "Salesperson"
    ]
)


#Find the Top 3 Most Expensive Products.
print("=" * 50)
print("Find the Top 3 Most Expensive Products")
print("=" * 50)

print(
    df.sort_values("Price", ascending=True)[
        "Product", "Price"
    ]
)

#Revenue = Price × Quantity

df["Revenue"] = df["Price"] * df["Quantity"]
print(
    df[
        ["Product", "Revenue"]
    ]
)

#Highest Total revenue

highest_total_revenue = df.groupby("Salesperson")["Revenue"].sum()
for Salesperson, Revenue in highest_total_revenue.items():
    print(f"{Salesperson:<10} : {Revenue} ")

