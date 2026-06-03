import pandas as pd
# Load Data
df = pd.read_csv("sales.csv")

print("Original Data")
print(df)

# Total Sales
total_sales = df["Sales"].sum()

# Average Sales
avg_sales = df["Sales"].mean()

# Sales By Region
region_sales = df.groupby("Region")["Sales"].sum()

print("\nTotal Sales:", total_sales)
print("\nAverage Sales:", avg_sales)

print("\nSales By Region")
print(region_sales)

# Save Summary
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Average Sales"],
    "Value": [total_sales, avg_sales]
})

summary.to_csv("summary_report.csv", index=False)

print("\nSummary Report Generated")
