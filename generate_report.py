import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
# Locate the cleaned dataset
base_path = Path(__file__).parent
input_file = base_path / "cleaned_data.csv"
df = pd.read_csv(input_file)
# Create a summary by department
department_summary = df.groupby("Department").agg(
    Total_Students=("Student_ID", "count"),
    Average_Marks=("Marks", "mean"),
    Average_Attendance=("Attendance", "mean")
).round(2)
# Create an overall summary
overall_summary = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Average Marks",
        "Average Attendance",
        "Missing Values Remaining",
        "Duplicate Rows Remaining"
    ],
    "Value": [
        len(df),
        round(df["Marks"].mean(), 2),
        round(df["Attendance"].mean(), 2),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum())
    ]
})
# Export summaries to an Excel workbook
excel_file = base_path / "automated_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    department_summary.to_excel(writer, sheet_name="Department Summary")
    overall_summary.to_excel(writer, sheet_name="Overall Summary", index=False)
print("Excel report created:", excel_file)
print("\nDepartment Summary:")
print(department_summary)
# Chart 1: Average marks by department
department_summary["Average_Marks"].plot(
    kind="bar",
    title="Average Marks by Department",
    ylabel="Average Marks",
    xlabel="Department"
)
plt.tight_layout()
plt.savefig(base_path / "department_marks_chart.png")
plt.show()
# Chart 2: Marks distribution
plt.figure()
df["Marks"].plot(
    kind="hist",
    bins=5,
    title="Distribution of Student Marks",
    xlabel="Marks"
)
plt.tight_layout()
plt.savefig(base_path / "marks_distribution_chart.png")
plt.show()
print("\nCharts saved successfully!")