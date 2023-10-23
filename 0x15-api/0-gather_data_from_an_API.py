#!/usr/bin/python3
"""
This script fetches data from a REST API to
display an employee's TODO list progress.
"""

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

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task.get('completed'))

    # Display the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_data.get('name'), completed_tasks, total_tasks))

    # Display the titles of completed tasks
    for task in todos_data:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
