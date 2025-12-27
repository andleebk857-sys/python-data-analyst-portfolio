import pandas as pd
df = pd.read_csv("cleaned_employee.csv")
kpis = {
    "Total salary cost" : df["salary"].sum(),
    "Total employees" : df["emp_id"].nunique(),
    "Average salary" : df["salary"].mean().round(2),
    "Highest paid department" : df.groupby("department")["salary"].sum().idxmax(),
    "Lowest paid department" : df.groupby("department")["salary"].sum().idxmin()
}
kpis_df = pd.DataFrame(list(kpis.items()), columns=["KPI", "Value"])
kpis_df.to_csv("KPI_summary.csv", index=False)
