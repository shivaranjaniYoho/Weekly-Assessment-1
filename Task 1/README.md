# HR Employee Analysis Project

## Project Description
This project analyses employee and department data using Python. It helps the HR team understand employee salaries, department details and salary distribution.

## Files Used
- `employees.csv` – Contains employee information such as name, department, salary and city.
- `hr_analysis.py` – Contains the Python code for the analysis.
- `employee_report.csv` – Stores employee details in a new CSV file.
- `HR_Report.txt` – Contains the final HR analysis results.
- PNG files – Contain the five charts created using Matplotlib.

## Python Concepts Used

1. **Functions:** Used a bonus function to calculate employee bonuses.
2. **OOP:** Created Employee and Manager classes using inheritance.
3. **Exception Handling:** Created InvalidSalaryError to prevent negative salaries.
4. **File Handling:** Used CSV files to read and write employee information.
5. **API:** Used the JSONPlaceholder API to practise getting data safely.
6. **NumPy:** Calculated average, maximum, minimum and total salary.
7. **Pandas:** Read employee data and calculated department-wise average salaries.
8. **Matplotlib:** Created five charts to understand employee salary and department information.

## Decisions Made

- Used separate functions and classes to keep the code organised.
- Used try, except and finally to handle errors.
- Used list comprehension, map and filter to practise working with employee data.
- Used NumPy and Pandas to make salary calculations easier.
- Used Matplotlib to present the results visually.
- Saved the final results in CSV, text and image files.

## How to Run the Project

Install the required libraries:

```bash
python -m pip install requests numpy pandas matplotlib
```

Run the Python file:

```bash
python hr_analysis.py
```

## Project Conclusion

This project helped me practise Python programming, file handling, API requests, data analysis, data visualisation and GitHub. The analysis provides a basic understanding of employee salaries and department-wise salary distribution.