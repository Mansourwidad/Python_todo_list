tasks = []

def show_menu():
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
