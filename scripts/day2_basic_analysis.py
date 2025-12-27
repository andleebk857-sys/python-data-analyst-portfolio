import pandas as pd
df = pd.read_csv("cleaned_employee.csv")
print("Dataset preview")
print(df.head())

total_salary = df["salary"].sum().round(2)
avg_salary = df["salary"].mean().round(2)
highest_salary = df["salary"].max().round(2)
lowest_salary = df["salary"].min().round(2)

# KPI Output
print("\n--- Salary KPIs ---")
print(f"highest_salary:  {highest_salary}")
print(f"lowest_salary:  {lowest_salary}")
print(f"avg_salary:  {avg_salary}")
print(f"total_salary:  {total_salary}")
