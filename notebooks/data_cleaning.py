import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/raw_dataset.csv")
print("Initial shape:", df.shape)

# =====================================================
# 1. Missing values
# =====================================================
# Fill numeric NaNs with median
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical NaNs with mode
for col in df.select_dtypes(include=["object"]).columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

# Drop Cabin column (too many missing values)
if "Cabin" in df.columns:
    df = df.drop(columns=["Cabin"])

# =====================================================
# 2. Duplicates
# =====================================================
df = df.drop_duplicates()

# =====================================================
# 3. Inconsistencies
# =====================================================
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].str.strip().str.lower()

# =====================================================
# 4. Outliers (IQR method for numeric columns)
# =====================================================
def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df = remove_outliers_iqr(df, col)

# =====================================================
# Save cleaned dataset
# =====================================================
print("Final shape:", df.shape)
df.to_csv("../data/cleaned_dataset.csv", index=False)
print("✅ Cleaned dataset saved to data/cleaned_dataset.csv")
