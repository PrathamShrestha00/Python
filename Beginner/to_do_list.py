import json
import os

FILE_NAME = "tasks.json"  # File to store tasks

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def display_menu():
    """Displays the menu options for the to-do list."""
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Clear all tasks")
    print("6. Exit")

def view_tasks(tasks):
    """Displays the current list of tasks."""
    if not tasks:
        print("\nNo tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

def add_task(tasks):
    """Adds a new task to the to-do list."""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append({'task': task, 'done': False})
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def mark_task_done(tasks):
    """Marks a task as done."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("\nEnter the task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]['done'] = True
                print(f"Task '{tasks[index]['task']}' marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    """Deletes a task from the to-do list."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("\nEnter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def clear_tasks(tasks):
    """Clears all tasks from the to-do list."""
    confirmation = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirmation == "yes":
        tasks.clear()
        print("All tasks have been cleared!")
    else:
        print("No tasks were cleared.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()  # Load tasks from file
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)  # Save tasks before exiting
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the application
if __name__ == "__main__":
    main()
