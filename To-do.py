import json

# Load Task
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
# Save Task:
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks,file)


# Adding Task:
        
def add_taks(tasks, task_name, due_date, priority):
    tasks.append({
        "taks_name" : task_name,
        "due_date"  : due_date,
        "priority"  : priority,
        "completed" : False
    })

# Removing Task:
    
def remove_task(tasks, index):
    del tasks[index]


# Display Tasks:
    
def display_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for index, task in enumerate(tasks):
            if 'task_name' in task:
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index + 1}. {task['task_name']} - Due: {task['due_date']} - Priority:{task['priority']} - Status:{status}")
            else:
                print("Task structure is invalid. Please check your data.")
                  
# Logic
            
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter your task name: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_taks(tasks,task_name,due_date,priority)
            save_tasks(tasks)
            print("Taks Added Successfully. ")

        elif choice == "2":
            display_tasks(tasks)
            index = int(input("Enter index of task to remove: ")) - 1
            remove_task(tasks, index)
            save_tasks(tasks)
            print("Task removed successfully.")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Calling main function:

if __name__ == "__main__":
    main()