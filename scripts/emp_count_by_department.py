import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("cleaned_employee.csv")
employees_count_pr_department = df.groupby("department")["emp_id"].count()
plt.figure()
employees_count_pr_department.plot(kind="bar")
plt.title("Number of employees by department")
plt.xlabel("Department")
plt.ylabel("Number of employees")
plt.tight_layout()
plt.savefig("Number of employees pr department")
plt.show()
