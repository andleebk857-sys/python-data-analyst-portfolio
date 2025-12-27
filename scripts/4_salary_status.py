import pandas as pd
import numpy as np
df = pd.read_csv("cleaned_employee.csv")

# employees have salaries above department avg.
df["salary"] = df["salary"].round(2)
df["dept_avg_salary"] = df.groupby("department")["salary"].transform("mean").round(2)
employees = df.loc[df["salary"]>df["dept_avg_salary"], "name"].unique()
employees_above_avg = ", ".join(employees)
print("These employees have salaries above average")
print(employees_above_avg)

# salary status
df["salary_status"] = np.where(df["salary"]>df["dept_avg_salary"], "High", "Low")

# save ouput
df.to_csv("employees_salary_analysis.csv", index=False)
print("Department analysis completed successfully.")
