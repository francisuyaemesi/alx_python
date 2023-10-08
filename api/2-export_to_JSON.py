"""fetching employee,TODO lists and counting completed tasks
"""

import json
import requests

def get_employee_todo_list_progress(employee_id):
    # Get employee details
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_name = response.json()['name']

    # Get employee TODO list
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])

    # Print progress report
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    for todo in todos:
        if todo['completed']:
            print(f'\t{todo["title"]}')

    # Export data to JSON file
    data = {str(employee_id): []}
    for todo in todos:
        data[str(employee_id)].append({
            'task': todo['title'],
            'completed': todo['completed'],
            'username': employee_name
        })

    with open(f'{employee_id}.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
