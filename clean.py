# self-assessment
# 1. the fill decision feels most ambiguous because i have to decide whether or not the gap of a missing value is meaningful or not
# 2. anyone reading my comments would probably would understand why i made a decision 
# 3. the most important things i noticed about thsi dataset that i didn't expect would be that the quantities sold would be so little despite the total amount, and that there would be a placeholder value of 9999 for quantity sold. i also didn't expect to see negative revenue values

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
# 1. max is 9999 for quantity sold, but the mean is 11 -- possible placeholder
# 2. negative revenue -- refunds/returns

df = df[df['quantity_sold'] != 9999]
print(df.describe())
print()

# exercise 7 - save
df.to_csv("data/clean_sales.csv", index=False)
print("\nSaved clean_sales.csv")