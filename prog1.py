# Simple To-Do List Application

def display_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f'Task "{task}" added.')
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            task_number = input("Enter the task number to remove: ")
            if task_number.isdigit() and 1 <= int(task_number) <= len(tasks):
                removed_task = tasks.pop(int(task_number) - 1)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
