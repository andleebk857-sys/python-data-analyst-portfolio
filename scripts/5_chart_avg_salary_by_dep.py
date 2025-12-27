import pandas as pd
import matplotlib.pyplot as plt
from rapidfuzz import process, fuzz
df = pd.read_csv("cleaned_employee.csv")
dept_avg_salary = df.groupby("department")["salary"].mean()
plt.figure()
dept_avg_salary.plot(kind="bar")
plt.title("Avg salary pr Department")
plt.xlabel("Department")
plt.ylabel("Dept_avg_salary")
plt.tight_layout()
plt.savefig("Avg_salary_Department")
plt.show()
