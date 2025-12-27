import pandas as pd
import numpy as np
df = pd.read_csv("cleaned_employee.csv")

grouped = df.groupby("department")
department_summary = pd.DataFrame({
    "total_salary" : grouped["salary"].sum().round(2),
    "avg_salary" : grouped["salary"].mean().round(2),
    "no_of_employees" : grouped["emp_id"].count()
})

department_summary.to_csv("department_summary.csv", index=False)

# extremes salaries 
highest_dept_salary = department_summary["avg_salary"].idxmax()
lowest_dept_salary = department_summary["avg_salary"].idxmin()
salary_extremes = pd.DataFrame({
    "metric" : ["highest_dept_salary", "lowest_dept_salary"],
    "department" : [highest_dept_salary, lowest_dept_salary]
})
salary_extremes.to_csv("salary_extremes.csv", index=False)


print("Department analysis completed successfully.")
