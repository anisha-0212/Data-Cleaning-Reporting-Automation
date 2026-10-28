
import pandas as pd
from pathlib import Path

# Create sample student data
data = {
    "Student_ID": [101, 102, 103, 104, 105, 102, 107, 108, 109, 110],
    "Name": [
        "Aarav", "Diya", "Rahul", "Priya", "Kiran",
        "Diya", "Meera", "Arjun", "Sneha", "Vikram"
    ],
    "Department": [
        "CSE", "cse", "AIML", "AI & DS", "IT",
        "cse", "AIML", "IT", "CSE", "aiml"
    ],
    "Marks": [85, 92, None, 78, 66, 92, 88, None, 73, 95],
    "Attendance": [90, 95, 82, None, 75, 95, 89, 80, None, 98]
}

df = pd.DataFrame(data)

file_path = Path(__file__).parent / "student_data.csv"
df.to_csv(file_path, index=False)

print("Sample dataset created successfully!")
print(df)
print("\nDataset saved to:", file_path)
