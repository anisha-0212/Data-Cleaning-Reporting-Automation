
import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
input_file = base_path / "student_data.csv"

# Load dataset
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove repeated student IDs
df = df.drop_duplicates(subset=["Student_ID"], keep="first").copy()

# Fill missing values with median
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].median()
)

# Standardize department names
df["Department"] = (
    df["Department"]
    .str.strip()
    .str.upper()
    .replace({"AI & DS": "AI & DS"})
)

# Save cleaned data
output_file = base_path / "cleaned_data.csv"
df.to_csv(output_file, index=False)

print("\nDATA CLEANING COMPLETED")
print("Cleaned dataset shape:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nCleaned dataset:")
print(df)
print("\nCleaned file saved to:", output_file)
