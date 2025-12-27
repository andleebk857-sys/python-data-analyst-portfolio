import  pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("cleaned_employee.csv")
total_salary_pr_department = df.groupby("department")["salary"].sum()
# chart of total salary by department
plt.figure()
total_salary_pr_department.plot(kind="bar")
plt.title("Total salary by department")
plt.xlabel("Department")
plt.ylabel("Total salary")
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.savefig("Total_salary_pr_department")
plt.show()
