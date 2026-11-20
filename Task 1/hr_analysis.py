
import csv

# --------------------------------
# 1. Bonus Function
# --------------------------------

def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate

    for extra in extras:
        result = result + extra

    if "cap" in options:
        if result > options["cap"]:
            result = options["cap"]

    return result


print("Bonus Amount:")
print(bonus(30000))
print(bonus(30000, 0.1, 500, 1000, cap=3500))


# --------------------------------
# 2. Custom Exception
# --------------------------------

class InvalidSalaryError(Exception):
    pass


# --------------------------------
# 3. Employee Class
# --------------------------------

class Employee:

    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary)


# --------------------------------
# 4. Manager Class (Inheritance)
# --------------------------------

class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            "Name: " + self.name +
            ", Salary: " + str(self.salary) +
            ", Team Size: " + str(self.team_size)
        )


# --------------------------------
# 5. Try, Except and Finally
# --------------------------------

try:
    employee1 = Employee("Arun", 30000)
    print("\nEmployee Details:")
    print(employee1.get_details())
    print("Annual Salary:", employee1.annual_salary())

    # Testing negative salary
    employee2 = Employee("Rahul", -5000)

except InvalidSalaryError as error:
    print("\nError:", error)

finally:
    print("Salary checking finished")


# --------------------------------
# 6. Manager Object
# --------------------------------

manager1 = Manager("Priya", 45000, 5)

print("\nManager Details:")
print(manager1.get_details())


# --------------------------------
# 7. Read Employee Data from CSV
# --------------------------------

employees = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

print("\nEmployee Data:")
for employee in employees:
    print(employee)


# --------------------------------
# 8. List Comprehension
# Names with salary above 50000
# --------------------------------

high_salary_names = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]

print("\nEmployees with salary above 50000:")
print(high_salary_names)


# --------------------------------
# 9. Map and Lambda
# Add 10% salary raise
# --------------------------------

salaries = [employee["salary"] for employee in employees]

new_salaries = list(map(lambda salary: round(salary * 1.10, 2), salaries))

print("\nSalary after 10% raise:")
print(new_salaries)


# --------------------------------
# 10. Filter
# Keep Chennai Employees
# --------------------------------

chennai_employees = list(
    filter(lambda employee: employee["city"] == "Chennai", employees)
)

print("\nEmployees from Chennai:")

for employee in chennai_employees:
    print(employee["name"])


# --------------------------------
# 11. For Loop with Continue and Break
# --------------------------------

print("\nChecking Employee Salaries:")

for employee in employees:

    salary = employee["salary"]

    if salary == 0:
        print("Skipped salary 0")
        continue

    print("Salary:", salary)

    if salary > 85000:
        print("Salary above 85000. Stopping the loop.")
        break


print("\nProgram completed")


# --------------------------------
# 12. Write Data into a CSV File
# --------------------------------

with open("employee_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["Name", "Department", "Salary", "City"])

    # Write employee details
    for employee in employees:
        writer.writerow([
            employee["name"],
            employee["department"],
            employee["salary"],
            employee["city"]
        ])

print("\nEmployee report created successfully!")


# --------------------------------
# 14. NumPy and Pandas Analysis
# --------------------------------

import numpy as np
import pandas as pd

# Read employee data
df = pd.read_csv("employees.csv")

print("\nComplete Employee Data:")
print(df)


# 1. Average Salary using NumPy
average_salary = np.mean(df["salary"])

print("\nAverage Salary:")
print(average_salary)


# 2. Highest Salary
highest_salary = np.max(df["salary"])

print("\nHighest Salary:")
print(highest_salary)


# 3. Lowest Salary
lowest_salary = np.min(df["salary"])

print("\nLowest Salary:")
print(lowest_salary)


# 4. Total Salary
total_salary = np.sum(df["salary"])

print("\nTotal Salary:")
print(total_salary)


# 5. Department-wise Average Salary
department_salary = df.groupby("department")["salary"].mean()

print("\nDepartment-wise Average Salary:")
print(department_salary)


# --------------------------------
# 15. Data Visualisation
# --------------------------------

import matplotlib.pyplot as plt

# Chart 1: Employee Salary Bar Chart

plt.figure(figsize=(8, 5))

plt.bar(df["name"], df["salary"])

plt.title("Employee Salary")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("employee_salary.png")
plt.show()


# Chart 2: Department-wise Average Salary

department_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

plt.bar(department_salary.index, department_salary.values)

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()

plt.savefig("department_salary.png")
plt.show()


# Chart 3: Employee Count by Department

department_count = df["department"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(department_count.index, department_count.values)

plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig("employee_count.png")
plt.show()


# Chart 4: Employee Salary Pie Chart

plt.figure(figsize=(7, 7))

plt.pie(
    df["salary"],
    labels=df["name"],
    autopct="%1.1f%%"
)

plt.title("Employee Salary Distribution")

plt.savefig("salary_pie_chart.png")
plt.show()


# Chart 5: Salary Histogram

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig("salary_histogram.png")
plt.show()


print("All 5 charts created successfully!")


# --------------------------------
# 16. Create Final HR Report
# --------------------------------

# Calculate employee details
total_employees = len(df)
average_salary = df["salary"].mean()
highest_salary = df["salary"].max()
lowest_salary = df["salary"].min()

# Create report file
with open("HR_Report.txt", "w") as file:

    file.write("HR EMPLOYEE ANALYSIS REPORT\n")
    file.write("---------------------------\n\n")

    file.write("Total Employees: " + str(total_employees) + "\n")
    file.write("Average Salary: " + str(average_salary) + "\n")
    file.write("Highest Salary: " + str(highest_salary) + "\n")
    file.write("Lowest Salary: " + str(lowest_salary) + "\n\n")

    file.write("DEPARTMENT-WISE AVERAGE SALARY\n")

    for department, salary in department_salary.items():
        file.write(department + ": " + str(round(salary, 2)) + "\n")

    file.write("\nEMPLOYEES WITH SALARY ABOVE 50000\n")

    for name in high_salary_names:
        file.write(name + "\n")

print("\nHR Report created successfully!")
