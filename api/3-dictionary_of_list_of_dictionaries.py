"""fetching employee,TODO lists and counting completed tasks
"""
import json
import requests

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
todos = json.loads(response.text)

# Create a dictionary to hold all tasks from all employees
all_tasks = {}

# Iterate over each task and add it to the dictionary
for todo in todos:
    user_id = todo['userId']
    task = {
        'username': 'USERNAME',
        'task': todo['title'],
        'completed': todo['completed']
    }
    if user_id in all_tasks:
        all_tasks[user_id].append(task)
    else:
        all_tasks[user_id] = [task]

# Save the dictionary as a JSON file
with open('todo_all_employees.json', 'w') as f:
    json.dump(all_tasks, f)
