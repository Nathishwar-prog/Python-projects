import sys
import os
import json

TASK_FILE = "task.json"

def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE,'r') as file :
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASK_FILE,'w') as file:
        json.dump(tasks,file,indent=4)

def add_task(description):
    tasks = load_task()
    task = {"id":len(tasks) + 1,"description":description,"status":"not done"}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added :{description}")

def update_task(task_id,description):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_tasks(tasks)
            print(f"Task updated : {description}")
            return
    print("Task is not Found!")

def delete_task(task_id):
    tasks = load_task()
    task =[task for task in tasks if task["id"] != task_id]
    save_tasks(task)
    print("Task Deleted !")

def mark_task(task_id,status):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"]= status
            save_tasks(tasks)
            print(f"Task {status}")
            return
    print("Task not Found !")

def list_task(filter_task = None):
    tasks = load_task()
    if filter_task:
        tasks = [task for task in tasks if task["status"] == filter_task]
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")
#
def main():
    print(sys.argv)
    if len(sys.argv)>2:
        print("Usage : python task_manager <action> [parameters]")
        return
    actions = sys.argv[1]
    if actions == "add" and len(sys.argv)>=3:
        add_task("".join(sys.argv[2:]))
    elif actions == "update" and len(sys.argv)>=4:
        update_task(int(sys.argv[2]),"".join(sys.argv[3:]))
    elif actions == "delete" and len(sys.argv)>= 3:
        delete_task(int(sys.argv[2]))
    elif actions == "mark" and len(sys.argv)>=4:
        mark_task(int(sys.argv[2]),sys.argv[3])
    elif actions == "list":
        list_task()
    elif actions == "list-done":
        list_task("done")
    elif actions == "list-not-done":
        list_task("not done")
    elif actions == "list-in-progress":
        list_task("in progress")
    else:
        print("Invalid command or missing parameters")

if __name__ == "__main__":
    main()
  # or 
# print(load_task())
# add_task("Buy groceries")
# add_task("Break fast")
# add_task("Lunch")
# add_task("Dinner")
# mark_task(2,"done")
# mark_task(3,"in progress")
# update_task(1,"Buy a laptop")
# delete_task(3)
# # #
# print(load_task())
# update_task(2,"Build a Project")
# delete_task(1)
# delete_task(2)
# delete_task(3)
# delete_task(4)
# delete_task(5)
# mark_task(1,"done")
# mark_task(2,"in progress")
# mark_task(3,"done")
# mark_task(4,"in progress")
# list_task()
# list_task("in progress")
