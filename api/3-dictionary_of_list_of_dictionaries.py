import requests
import json
import sys

def export_all_employees_todo_to_json():
    """Exports TODO lists for all employees to a JSON file."""
    try:
        # Get a list of all users
        users_url = "https://jsonplaceholder.typicode.com/users"
        users_response = requests.get(users_url)
        users_response.raise_for_status()  # Raise an exception for bad responses.
        users = users_response.json()

        # Create a dictionary to store JSON data for all employees.
        all_employees_data = {}

        for user in users:
            user_id = user["id"]
            username = user["username"]

            # Get the employee's TODO list items.
            todo_list_items_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
            todo_list_items_response = requests.get(todo_list_items_url)
            todo_list_items_response.raise_for_status()  # Raise an exception for bad responses.
            todo_list_items = todo_list_items_response.json()

            # Store TODO list data for the user.
            user_todo_data = [
                {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                for task in todo_list_items
            ]

            all_employees_data[user_id] = user_todo_data

        # Open a JSON file for writing.
        json_file_path = "todo_all_employees.json"
        with open(json_file_path, "w") as json_file:
            # Write JSON data to the file.
            json.dump(all_employees_data, json_file, indent=2)

        print(f"TODO lists for all employees exported to {json_file_path}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO lists for all employees: {e}")

if __name__ == "__main__":
    export_all_employees_todo_to_json()
