import json
File = "todo.json"

try:
    with open(File, "r") as f:
        content = f.read()
        tasks = json.loads(content) if content.strip() else []
except FileNotFoundError:
    tasks = []
    
while True:
    print("-------------- Welcome To To-Do List Manager Simulator----------------- ")
    print("1: Add a Task")
    print("2: View Tasks")
    print("3: Delete a Task")
    print("4: Exit")
    c1 = int(input("Enter Your Choice: "))
    
    if (c1 == 1):
        name = input("Enter The name of the task: ")
        desc = input("Enter the description of the task: ")
        time = input("Enter the time of task: ")
        new_task = {
            "name": name,
            "description": desc,
            "time": time,
        }
        tasks.append(new_task)
        with open(File, "w") as f:
            json.dump(tasks, f, indent=4)
        print(f"The task {name} is added succesfully")
        
    elif (c1 == 2):
        if not tasks:
            print("No Task To Show Please add a task")
        else:
            for t in tasks:
                print(t)
                
    elif (c1 == 3):
        r_name = input("Enter The Name of taskk you want to remove: ")
        found = False
        for t in tasks:
            if r_name.lower() == t["name"].lower():
                found = True
                tasks.remove(t)
                break
        if found:
            with open(File, "w") as f:
                json.dump(tasks, f, indent=4)
            print(f"The Task {r_name} removed successfully")
        else:
            print(f"The task {r_name} not found")
            
    elif (c1 == 4):
        print("Thanks For Using!")
        break
