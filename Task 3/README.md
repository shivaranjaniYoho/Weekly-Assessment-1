
# HR NumPy and Pandas Analysis

## Project Description

This project analyses employee and department data using Python.

## Libraries Used

- NumPy
- Pandas
- Matplotlib

## Tasks Completed

1. Created a NumPy marks array.
2. Calculated student and subject averages.
3. Calculated weighted scores using np.dot.
4. Loaded employee and department CSV files.
5. Cleaned missing values and duplicate records.
6. Used groupby and merge operations.
7. Identified departments without employees.
8. Created four charts using Matplotlib.

## Charts

- Bar Chart
- Histogram
- Scatter Plot
- Line Chart

## How to Run

Install the required libraries:

pip install -r requirements.txt

Run the Python file:

python main.py

## Output

The project generates cleaned employee data and four chart images.

## Project Status

Employee data analysis project completed.

# HR NumPy and Pandas Analysis

## Project Description
This project analyses employee and department data using Python, NumPy, Pandas and Matplotlib.

## Decisions and Explanations

1. **NumPy:** Created marks for four students and three subjects. Used averages to compare student and subject performance.

2. **Grace Marks:** Added 5 marks to each subject using broadcasting.

3. **Weighted Scores:** Used `np.dot()` with weights of 50%, 30% and 20% to calculate weighted marks.

4. **Missing Values:** Filled the two missing employee salaries using the median salary because it is less affected by unusually high or low salaries.

5. **Duplicate Records:** Removed the duplicate employee row using `drop_duplicates()` to avoid counting the same employee twice.

6. **Data Types:** Converted columns into suitable data types for correct analysis.

7. **Department Analysis:** Used `groupby()` to calculate employee count, average salary and maximum salary for each department.

8. **Merging:** Used inner, left and outer joins to compare employee and department information.

9. **Empty Department:** Added Marketing as an extra department to identify departments that have no employees.

## Charts and Insights

- **Bar Chart:** Compares average salaries across departments.
- **Histogram:** Shows the distribution of employee salaries.
- **Scatter Plot:** Compares employee age and salary.
- **Line Chart:** Shows average salary differences between departments.

## Project Structure

- `data/` – Original and cleaned CSV files.
- `charts/` – Four saved chart images.
- `main.py` – Python analysis code.
- `requirements.txt` – Required Python libraries.

## How to Run

Install libraries:

`pip install -r requirements.txt`

Run the project:

`python main.py`

## Conclusion

This project helped me practise NumPy calculations, Pandas data cleaning, grouping, merging and creating charts using Matplotlib.