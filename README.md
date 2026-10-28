# Data Cleaning & Reporting Automation

## Project Overview
This project automates data cleaning and reporting using Python. It processes a sample student dataset, handles missing values, removes duplicate student IDs, standardizes department names, and generates Excel reports and charts.

## Objectives
- Identify and handle missing values.
- Remove duplicate student records.
- Standardize inconsistent department names.
- Generate Excel summary reports automatically.
- Visualize student marks using charts.

## Technologies Used
- Python
- Pandas
- OpenPyXL
- Matplotlib
- PyCharm

## Project Workflow
1. Generate a sample student dataset.
2. Load and clean the data.
3. Fill missing marks and attendance with median values.
4. Remove repeated student IDs.
5. Standardize department names.
6. Export cleaned data to CSV.
7. Generate an Excel report with department summaries.
8. Create charts for marks analysis.

## Output Files
- `student_data.csv` — original sample dataset
- `cleaned_data.csv` — cleaned dataset
- `automated_report.xlsx` — automated Excel report
- `department_marks_chart.png` — average marks by department
- `marks_distribution_chart.png` — marks distribution chart

## How to Run
Install the required libraries:

`pip install pandas openpyxl matplotlib`

Run the Python files in this order:
1. `student_data_generator.py`
2. `data_cleaning_report.py`
3. `generate_report.py`

## Conclusion
This project demonstrates how Python can automate data preprocessing, data-quality checks, Excel reporting, and visualization, reducing repetitive manual work.
