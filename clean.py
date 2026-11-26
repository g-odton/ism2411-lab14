# exercise 1 - inspect
import pandas as pd
df = pd.read_csv("data/messy_sales.csv")
df.info()
df.isnull().sum()
print()

# 3 data quality issues:
# 1. unit price isn't float
# 2. index starts at 1 instead of 0
# 3. customer id should also be float?

# exercise 2 - standardize the columns
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns)

# exercise 3 - handle missing values
df = df.dropna(subset=["order_id", "order_date"])
df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())
df["quantity_sold"] = df["quantity_sold"].astype(int)