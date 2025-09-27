# 1. Import libraries
import pandas as pd

# 2. Load raw dataset
df = pd.read_csv("../data/raw_dataset.csv")

# 3. Exploratory checks
print("=== Dataset Info ===")
df.info()

print("\n=== Dataset Description ===")
print(df.describe(include="all"))

# 4. Missing values check
print("\n=== Missing Values Per Column ===")
print(df.isnull().sum())

# 5. Duplicate rows check
duplicates = df.duplicated().sum()
print(f"\n=== Duplicate Rows Found: {duplicates} ===")
