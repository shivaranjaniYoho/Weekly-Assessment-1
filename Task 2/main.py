
import csv
import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API key loaded successfully")
else:
    print("API key not found")


# Read employee data from CSV file
employees = []

with open("employees.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(line for line in file if line.strip())

    for row in reader:
        employees.append(row)

print("\nEmployee Details:")

for employee in employees:
    print(employee)

# Write employee data into JSON file
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

    print("\nemployees.json created successfully")


# Create CSV file for employees earning above 50000
with open("high_earners.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name", "department", "salary", "city"]
    )

    writer.writeheader()

    for employee in employees:
        if int(employee["salary"]) > 50000:
            writer.writerow(employee)

print("high_earners.csv created successfully")


# Get user details from API

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    # Print first 3 users
    print("\nFirst 3 Users from API:")

    for user in users[:3]:
        print("ID:", user.get("id"))
        print("Name:", user.get("name"))
        print("Email:", user.get("email"))
        print("-------------------")

    # Get nested user details
    user_details = []

    for user in users:
        user_details.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "company": user.get("company", {}).get("name")
        })

    # Save user details in JSON file
    with open("users.json", "w") as file:
        json.dump(user_details, file, indent=4)

    print("users.json created successfully")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)


# Check 404 error

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("\n404 Error: User not found")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")
