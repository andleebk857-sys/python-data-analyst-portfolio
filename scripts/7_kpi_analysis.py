import pandas as pd
import numpy as np
df = pd.read_csv("cleaned_employee.csv")
Total_payroll = df["salary"].sum()
Avg_salary = df["salary"].mean()
df["salary_band"] = np.where(df["salary"]<50000, "Low", np.where((df["salary"]>=50000) & (df["salary"]<=80000), "Medium", "High"))
# percentage of high, low and medium
salary_distribution = df["salary_band"].value_counts(normalize=True) * 100
# percentage of high
High_salary_distribution = salary_distribution.get("High", 0).astype(str) + "%"

# pr department percentage of salary from total salary
dept_cost_share = (df.groupby("department")["salary"].sum()/Total_payroll *100).round(2).astype(str) + "%"

KPI_summary = pd.DataFrame({
    "KPI" : [
        "Total_salary",
        "Avg_salary",
        "High_salary_percentage"
    ],
    "Value" : [
        round(Total_payroll,2),
        round(Avg_salary,2),
        High_salary_distribution
    ]
})
KPI_summary.to_csv("Analysis.summary.csv", index=False)
dept_cost_share.to_csv("pr_department_cost_percentage.csv")
