# exercise 1 - inspect
import pandas as pd
df = pd.read_csv("data/messy_sales.csv")
df.info()
df.isnull().sum()

# exercise 2 - standardize the columns
# df.columns = df.columns.str.lower().str.replace(" ", "_")
# print(df.columns)