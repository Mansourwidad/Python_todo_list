import json
import os

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if name == "main":
    main()
