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
print()

# exercise 3 - handle missing values
before = len(df)
df = df.dropna(subset=["order_id", "order_date"]) # no way to place order
print(f"Dropped {before - len(df)} rows missing order_id or order_date")
df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean()) # low % missing, aggregate analysis
print()

# exercise 4 - convert data types
df["unit_price"] = df["unit_price"].str.replace("$", "", regex=False)
df["unit_price"] = df["unit_price"].str.replace(",", "", regex=False).astype(float)
df["quantity_sold"] = df["quantity_sold"].astype(int)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
bad_dates = df["order_date"].isnull().sum()
print(f"Unparseable dates: {bad_dates}")
print(df.dtypes)
print()

# exercise 5 - check duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(df.shape)
print()

# exercise 6 - describe
print("\nDescriptive stats after cleaning:")
print(df.describe())
print()

# at least 2 stats that look suspicious:
# 1. unit price and quantity sold have really long decimal places
# 2. order date for mean(???) has a long decimal place, while all others have 00:00:00 for time

df = df.dropna(subset=["quantity_sold"]) # made max 9999

# exercise 7 - 