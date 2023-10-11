import json 
#Initialize an empty to-do list
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append({"task": task, "completed": False})

# Function to mark a task as completed
def complete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
    else:
        print("Invalid task index")

# Function to remove a task from the list
def remove_task(task_index):
    if 0 <= task_index < len(todo_list):
        del todo_list[task_index]
    else:
        print("Invalid task index")

# Function to display the to-do list
def display_tasks():
    for index, task in enumerate(todo_list):
        status = "✓" if task["completed"] else " "
        print(f"{index}: [{status}] {task['task']}")

# Function to save the to-do list to a file
def save_to_file(filename):
    with open(filename, "w") as file:
        json.dump(todo_list, file)

# Function to load the to-do list from a file
def load_from_file(filename):
    global todo_list
    try:
        with open(filename, "r") as file:
            todo_list = json.load(file)
    except FileNotFoundError:
        todo_list = []

# Main loop
if _name_ == "_main_":
    filename = "todo_list.json"
    load_from_file(filename)

    while True:
        print("\nTo-Do List:")
        display_tasks()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Save and Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to mark as completed: "))
            complete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(task_index)
        elif choice == "4":
            save_to_file(filename)
            print("To-Do List saved. Quitting.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")