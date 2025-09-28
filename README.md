# Data Cleaning with AI Support

## Student Information
- **Name:** JEMAR JOHN J LUMINGKIT  
- **Course Year:** BSCS 4  
- **Date:** 2003-09-28  

---

## Dataset
- **Source:** [Titanic - Machine Learning from Disaster (Kaggle)](https://www.kaggle.com/competitions/titanic/data)  
- **Name:** Titanic Dataset  

---

## Issues Found
- **Missing values:**  
  - `Age`: 177 missing  
  - `Cabin`: 687 missing  
  - `Embarked`: 2 missing  
- **Duplicates:** None  
- **Inconsistencies:** None  

```python
=== Dataset Description ===
        PassengerId    Survived      Pclass  ...        Fare Cabin  Embarked
count    891.000000  891.000000  891.000000  ...  891.000000   204       889
unique          NaN         NaN         NaN  ...         NaN   147         3
top             NaN         NaN         NaN  ...         NaN    G6         S
freq            NaN         NaN         NaN  ...         NaN     4       644
mean     446.000000    0.383838    2.308642  ...   32.204208   NaN       NaN
std      257.353842    0.486592    0.836071  ...   49.693429   NaN       NaN
min        1.000000    0.000000    1.000000  ...    0.000000   NaN       NaN
25%      223.500000    0.000000    2.000000  ...    7.910400   NaN       NaN
50%      446.000000    0.000000    3.000000  ...   14.454200   NaN       NaN
75%      668.500000    1.000000    3.000000  ...   31.000000   NaN       NaN
max      891.000000    1.000000    3.000000  ...  512.329200   NaN       NaN
```
```python
=== Missing Values Per Column ===
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

=== Duplicate Rows Found: 0 ===
```
---

## Key Data Cleaning Steps
1. **Missing Values**
   - Age: Imputed missing values with median.  
   - Embarked: Filled missing values with most common value ("S").  
   - Cabin: Too many missing entries → dropped the column for analysis.  

2. **Name Cleaning**
   - Removed titles (`Mr.`, `Mrs.`, `Miss.`, etc.).  
   - Standardized format from `SURNAME, FIRST NAME` → `First Name Surname`.  
   - Removed content in parentheses (e.g., maiden names).  

3. **Ticket Column**
   - Converted to numeric where possible.  
   - Standardized formatting.  
   - Removed duplicate ticket numbers to ensure uniqueness.  

4. **Fare Column**
   - Standardized to two decimal places (`.00` format).  
   - Checked for extreme outliers.  

5. **Duplicates & Empty Rows**
   - Dropped duplicate rows.  
   - Removed rows with mostly empty fields.  
---

## AI Prompts Used
**Prompt 1:**  
*"Generate Pandas code to clean and corrected data:"*  

**Generated code:**  
```python
# 🧹 Data Cleaning Notebook for Titanic Dataset

## 1. Import Libraries
import pandas as pd

## 2. Load Dataset
df = pd.read_csv("../data/raw_dataset.csv")
print("Original Shape:", df.shape)
df.head()

## 3. Initial Exploration
df.info()
df.describe(include="all")

# Age → fill missing with median, convert to int
df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)

# Embarked → fill missing with most common (mode)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin → replace NaN with 'Unknown'
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Drop rows that are entirely empty
df = df.dropna(how="all")

# Remove titles (Mr., Mrs., Miss., Master., Dr., etc.)
df['Name'] = df['Name'].str.replace(r"(Mr\.|Mrs\.|Miss\.|Master\.|Don\.|Dr\.|Rev\.)", "", regex=True)

# Remove parentheses and contents inside them
df['Name'] = df['Name'].str.replace(r"\(.*\)", "", regex=True).str.strip()

# Split Surname, Firstname -> reorder to Firstname Surname
def reorder_name(name):
    if "," in name:
        parts = [p.strip() for p in name.split(",")]
        if len(parts) >= 2:
            return parts[1] + " " + parts[0]
    return name

df['Name'] = df['Name'].apply(reorder_name)

# Extract numeric part of ticket (remove letters, spaces, dots)
df['Ticket'] = df['Ticket'].astype(str).str.replace(r"\D", "", regex=True)

# Drop duplicates based on Ticket Number
df = df.drop_duplicates(subset=['Ticket'])

# Ensure Ticket column is numeric
df['Ticket'] = pd.to_numeric(df['Ticket'], errors='coerce')

df['Sex'] = df['Sex'].str.strip().str.lower()

# Fill missing fares with median
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# Round to 2 decimal places
df['Fare'] = df['Fare'].round(2)

# Keep only the first letter (deck)
df['Cabin'] = df['Cabin'].apply(lambda x: x[0] if x != 'Unknown' else 'Unknown')

df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

df.to_csv("../data/cleaned_dataset.csv", index=False)
print("✅ Cleaned dataset saved!")


```
---
## Results
- **Rows before cleaning**: `(891, 12)`
- **Rows after dropping duplicates & empty rows**: 561  
- **Final Shape**: `(561, 11)`  

#### Data Types After Cleaning
```python
RangeIndex: 561 entries, 0 to 560
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  561 non-null    int64  
 1   Survived     561 non-null    int64  
 2   Pclass       561 non-null    int64  
 3   Name         561 non-null    object 
 4   Sex          561 non-null    object 
 5   Age          561 non-null    float64
 6   SibSp        561 non-null    int64  
 7   Parch        561 non-null    int64  
 8   Ticket       561 non-null    object 
 9   Fare         561 non-null    float64
 10  Cabin        0   non-null    object #Dropped due to low data & statistical irrelevant 
 11  Embarked     561 non-null    object 
dtypes: float64(2),   int64(5),   object(5)
```
---
## Video
 - https://tinyurl.com/KINGSTING

        

