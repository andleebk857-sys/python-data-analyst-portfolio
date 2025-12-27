import pandas as pd
import numpy as np
df = pd.read_csv("cleaned_employee.csv")
df["salary_band"] = np.where(df["salary"]<50000, "Low", np.where((df["salary"]>=50000) & (df["salary"]<=80000), "Medium", "High"))
print(df)
department = df[df["salary_band"] == "High"]["department"].value_counts().idxmax()
print("This department have max high salary bands")
print(department)
total_employees = len(df)
high_salary_count = (df["salary_band"] == "High").sum()
percentage = (high_salary_count/total_employees) * 100
print(f"percentage of no.of employees have high salary: {percentage}%")
