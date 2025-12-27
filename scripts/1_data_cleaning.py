import pandas as pd
from rapidfuzz import process, fuzz
df = pd.read_csv("employees.csv")
print("first 5 rows")
print(df.head())
print("info")
print(df.info())
print("null")
print(df.isnull().sum())
# fill missing values 
df["department"] = df["department"].fillna("Unknown")
df["salary"] = df["salary"].fillna(df.groupby("department")["salary"].transform("mean")).round(2)
# standardize the department names
department_names = ["IT", "HR", "Finance", "Human_Resource", "Sales"]
def correct(names):
    if pd.isna(names):
        return None
    names = names.strip().title()
    match, score, _ = process.extractOne(names, department_names, scorer=fuzz.ratio)
    if score>=40:
        return match
    else:
        return None
df["department"] = df["department"].apply(correct)
df["department"] = df["department"].replace("Human_Resource", "HR")
# outlires
outliers = df[(df["salary"]<10000) | (df["salary"]>300000)]
print("Potential salary Outlires:")
print(outliers)
df.to_csv("cleaned_employee.csv", index=False)
print(df.isnull().sum())
print(df["department"].value_counts())
