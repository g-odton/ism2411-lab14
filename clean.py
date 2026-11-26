# self-assessment
# 1.
# 2.

# exercise 1 - inspect
import pandas as pd
df = pd.read_csv("data/messy_sales.csv")
print(df.info())
print(df.isnull().sum())

# 3 data quality issues:
# 1. unit price should be float but is object
# 2. index starts at 0, not 1
# 3. column names are not standardized

# exercise 2 - standardize column names


# exercise 3 - handle missing values


# exercise 4 - fix types


# exercise 5 - check duplicates


# exercise 6 - describe


# exercise 7 - save

