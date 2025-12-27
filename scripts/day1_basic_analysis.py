import pandas as pd
df = pd.read_csv("employees.csv")
print("Dataset preview")
print(df.head())

total_salary = df["salary"].sum()
avg_salary = df["salary"].mean()
highest_salary = df["salary"].max()
lowest_salary = df["salary"].min()

# KPI Output
print("\n--- Salary KPIs ---")
print(f"highest_salary:  {highest_salary}")
print(f"lowest_salary:  {lowest_salary}")
print(f"avg_salary:  {avg_salary}")
print(f"total_salary:  {total_salary}")
