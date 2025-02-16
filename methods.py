import datetime
import json

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_task(task_name, priority):

    data = load_tasks_from_json()

    task = {
        "name": task_name,
        "priority": priority,
        "timestamp": time,
        "completed": False
    }

    data.append(task)
    save_tasks_to_json(data)

def remove_task(task_name):
    
    data = load_tasks_from_json()

    taskexist = False

    for task in data:
        if task_name == task["name"]:
            taskexist = True
            data.remove(task)
            print(f"Task {task_name} removed successfully")
    
    if taskexist == False:
        print(f"No task as {task_name}")

    save_tasks_to_json(data)

def mark_task_completed(task_name):

    data = load_tasks_from_json() 
    
    taskexist = False 

    for task in data:
        if task_name == task["name"]:
            task["completed"] = True 
            taskexist = True
            print(f"Task {task_name} marked completed")
            break
            
    if taskexist == False:
        print(f"No task as {task_name}")
    
    save_tasks_to_json(data)

def view_tasks(status,truefalse):

    try:
        taskname = input("Write name of task, or type all: ").lower()
        if truefalse == 4:
            notcompleted = []
            high = []
            medium = []
            low = []

            print("Pending Tasks:")
            for task in status:
                if task["completed"] == False:
                    notcompleted.append(task)
                    for task in notcompleted:
                        if task["priority"] == "high":
                            high.append(task)
                        if task["priority"] == "medium":
                            medium.append(task)
                        if task["priority"] == "low":
                            low.append(task)
                    if taskname == "all":
                        if high:
                            print("[High Priority]")
                            for tasks in high:
                                print(f"- {tasks["name"]} (Added on: {tasks["timestamp"]})")
                            print("")
                        if medium:
                            print("[Medium Priority]")
                            for tasks in medium:
                                print(f"- {tasks["name"]} (Added on: {tasks["timestamp"]})")
                            print("")
                        if low:
                            print("[Low Priority]")
                            for tasks in low:
                                print(f"- {tasks["name"]} (Added on: {tasks["timestamp"]})")
                    else:
                        taskexist = False
                        for tasks in notcompleted:
                            if tasks["name"] == taskname:
                                taskexist = True
                                print(f"Task Name: {tasks["name"]} Priority: {tasks["priority"]} Timestamp: {tasks["timestamp"]} Completed: {tasks["completed"]}")
                        if taskexist == False:
                            print(f"No task as {taskname}")
        elif truefalse == 5:
            completed = []
            high = []
            medium = []
            low = []
           
            for task in status:
                if task["completed"] == True:
                    completed.append(task)
                    for task in completed:
                        if task["priority"] == "high":
                            high.append(task)
                        elif task["priority"] == "medium":
                            medium.append(task)
                        elif task["priority"] == "low":
                            low.append(task)
                    if taskname == "all":
                        if high:
                            print("[High Priority]")
                            for tasks in high:
                                print(f"- {tasks["name"]} (Added on: {tasks["timestamp"]})")
                        if medium:
                            print("[Medium Priority]")
                            for tasks in medium:
                                print(f"- {tasks["name"]} (Added on: {tasks["timestamp"]})")
                        if low:
                            print("[Low Priority]")
                            for tasks in low:
                                print(f"- {tasks["name"]} (Added on: {tasks["timestamp"]})")
                    else:
                        taskexist = False
                        for tasks in completed:
                            if tasks["name"] == taskname:
                                taskexist = True
                                print(f"Task Name: {tasks["name"]} Priority: {tasks["priority"]} Timestamp: {tasks["timestamp"]} Completed: {tasks["completed"]}")
                        if taskexist == False:
                            print(f"No task as {taskname}")

    except KeyError:    
        print("There is not any task in system")
        
def save_tasks_to_json(data):

    with open("data.json", "w") as file:
        json.dump(data, file, indent = 4)

def load_tasks_from_json():

    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("There is not any file like that")
        exit()