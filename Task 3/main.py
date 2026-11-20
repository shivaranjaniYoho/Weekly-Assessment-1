
# HR NumPy, Pandas and Matplotlib Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# TASK 1: NUMPY
# --------------------------------

print("NUMPY ANALYSIS")

# Marks of 4 students in 3 subjects
marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 88, 95],
    [55, 60, 70]
])

# Print the marks
print("Marks:")
print(marks)

# Print array shape
print("Shape:", marks.shape)

# Average marks of each student
student_average = np.mean(marks, axis=1)
print("Student averages:", student_average)

# Average marks of each subject
subject_average = np.mean(marks, axis=0)
print("Subject averages:", subject_average)

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("Marks after grace marks:")
print(grace_marks)

# Calculate weighted scores
weights = np.array([0.5, 0.3, 0.2])

weighted_scores = np.dot(marks, weights)
print("Weighted scores:", weighted_scores)


# --------------------------------
# TASK 2: LOAD EMPLOYEE DATA
# --------------------------------

print("\nPANDAS ANALYSIS")

# Read employee data
df = pd.read_csv("data/employees.csv")

# Read department data
departments = pd.read_csv("data/departments.csv")

# Display first five rows
print("\nFirst five employees:")
print(df.head())

# Display information
print("\nEmployee information:")
df.info()

# Display statistics
print("\nEmployee statistics:")
print(df.describe())

# Using loc
print("\nUsing loc:")
print(df.loc[0:2, ["name", "department", "salary"]])

# Using iloc
print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])

# Filtering employees with salary above 50000
print("\nEmployees with salary above 50000:")
print(df[df["salary"] > 50000])


# --------------------------------
# TASK 3: DATA CLEANING
# --------------------------------

print("\nDATA CLEANING")

# Check missing salaries
print("Missing salaries:")
print(df["salary"].isnull().sum())

# Remove duplicate rows first
df = df.drop_duplicates()

# Fill missing salaries with median
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

# Correct data types
df["employee_id"] = df["employee_id"].astype(str)
df["name"] = df["name"].astype(str)
df["department"] = df["department"].astype(str)
df["age"] = df["age"].astype(int)
df["salary"] = df["salary"].astype(float)

print("\nCleaned employee data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nData types after cleaning:")
print(df.dtypes)

# Save cleaned data
df.to_csv("data/cleaned_employees.csv", index=False)


# --------------------------------
# TASK 4: DEPARTMENT ANALYSIS
# --------------------------------

print("\nDEPARTMENT ANALYSIS")

# Group employees by department
department_summary = df.groupby("department").agg(
    headcount=("employee_id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment summary:")
print(department_summary)

# Inner merge
inner_result = pd.merge(
    df, departments, on="department", how="inner"
)

print("\nInner merge:")
print(inner_result)

# Left merge
left_result = pd.merge(
    df, departments, on="department", how="left"
)

print("\nLeft merge:")
print(left_result)

# Outer merge
outer_result = pd.merge(
    df, departments, on="department", how="outer"
)

print("\nOuter merge:")
print(outer_result)

# Find departments without employees
employee_departments = df["department"].unique()

empty_departments = departments[
    ~departments["department"].isin(employee_departments)
]

print("\nDepartments without employees:")
print(empty_departments)


# --------------------------------
# TASK 5: CREATE CHARTS
# --------------------------------

print("\nCREATING CHARTS")

# Chart 1: Bar chart
department_average = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
department_average.plot(kind="bar", label="Average Salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/bar_chart.png")
plt.show()

print("Insight: The bar chart compares the average salary of each department.")


# Chart 2: Histogram
plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, label="Employee Salary",
         edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("charts/histogram.png")
plt.show()

print("Insight: The histogram shows how employee salaries are distributed.")


# Chart 3: Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df["age"], df["salary"], label="Employees")

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/scatter_plot.png")
plt.show()

print("Insight: The scatter plot shows the relationship between employee age and salary.")


# Chart 4: Line chart
plt.figure(figsize=(8, 5))

department_average.plot(
    kind="line",
    marker="o",
    label="Average Salary"
)

plt.title("Department Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/line_chart.png")
plt.show()

print("Insight: The line chart shows how average salaries differ across departments.")

print("\nHR DATA ANALYSIS COMPLETED SUCCESSFULLY!")
