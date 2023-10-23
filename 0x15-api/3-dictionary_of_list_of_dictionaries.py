#!/usr/bin/python3
"""
This script fetches data from a REST API to display TODO list progress for
all employees and exports it to a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    # Fetch all employee data from the API
    all_employees_response = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    all_employees_data = all_employees_response.json()

    # Initialize an empty dictionary to hold all employee tasks
    all_tasks = {}

    # Loop through each employee to fetch their tasks
    for employee_data in all_employees_data:
        employee_id = employee_data.get('id')

        # Fetch the TODO list for the employee
        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(employee_id))
        todos_data = todos_response.json()

        # Prepare data for JSON export
        tasks = []
        for task in todos_data:
            tasks.append({
                "username": employee_data.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        # Add the tasks to the all_tasks dictionary
        all_tasks[employee_id] = tasks

    # Export data to JSON file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_tasks, json_file)
