# todo.py - Simple Console To-Do List

tasks = []  # List to store all tasks

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ").strip()

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:  # don't add empty tasks
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted_task = tasks.pop(num - 1)
                    print(f"Deleted: '{deleted_task}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye! See you next time 👋")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
