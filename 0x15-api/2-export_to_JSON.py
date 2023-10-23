#!/usr/bin/python3
"""
This script fetches data from a REST API to display an employee's TODO list
progress and exports it to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Check if the script received the employee ID as a parameter
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Fetch employee data from the API
    employee_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id))
    employee_data = employee_response.json()

    # Fetch the TODO list for the employee
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))
    todos_data = todos_response.json()

    # Prepare data for JSON export
    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_data.get('username')
        })

    # Export data to JSON file
    with open("{}.json".format(employee_id), 'w') as json_file:
        json.dump({employee_id: tasks}, json_file)
