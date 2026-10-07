tasks = []

print("Welcome to the To-do list app!")       # greeting message.

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    option = int(input("Choose an option: "))    # user chooses an option.
    if option == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added")
    elif option == 2:
        print("Your tasks are: ") 
        for i, task in enumerate(tasks, start=1):        # To list out the items.
            print(f"{i}. {task}")
    elif option == 3:   
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):              # This checks if the task number is valid.
            removed_task = (task_num - 1)
            tasks.pop(removed_task)
            print("Task removed")
        else:
            print("Invalid task number")
    elif option == 4:
        print("Exiting the app.")
        break

    

