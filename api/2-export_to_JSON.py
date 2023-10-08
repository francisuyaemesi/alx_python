import requests
import json
import sys

def export_employee_todo_list_to_json(employee_id):
    """Exports the employee's TODO list to a JSON file."""
    try:
        # Get the employee's TODO list items.
        todo_list_items_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_list_items_response = requests.get(todo_list_items_url)
        todo_list_items_response.raise_for_status()  # Raise an exception for bad responses.
        todo_list_items = todo_list_items_response.json()

        # Create a dictionary to store JSON data.
        json_data = {
            "USER_ID": [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": task["username"]
                }
                for task in todo_list_items
            ]
        }
