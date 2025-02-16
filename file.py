from methods import add_task,remove_task,mark_task_completed,view_tasks,save_tasks_to_json,load_tasks_from_json

choice = 0

while choice !=6:

    data = load_tasks_from_json()

    print("Task Management System")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View Pending Tasks")
    print("5. View Completed Tasks")
    print("6. Exit")

    try:   
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter task name: ").lower()
            while True:
                priority = input("Enter Priority High/Medium/Low: ").lower()

                if priority == "high" or priority == "medium" or priority == "low":
                    add_task(name,priority)
                    break 
                else:
                    print("Wrong priority type")
                    continue

        elif choice == 2:
            name = input("Enter task name: ").lower()
            remove_task(name)
        elif choice == 3:
            name = input("Enter task name: ").lower()
            mark_task_completed(name)
        elif choice == 4:
            view_tasks(data,choice)
        elif choice == 5:
            view_tasks(data,choice)
        elif choice == 6:
            exit()
        else:
            print("Type only 1,2,3,4,5,6")
    except ValueError:
        print("Type integer")
