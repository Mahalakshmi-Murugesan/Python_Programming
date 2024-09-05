# Simple To-Do List Application in Python

tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("----------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number you want to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                print(f"Task {task_num} updated to '{new_task}'.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number you want to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()