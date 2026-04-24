def tasks():
    tasks = [] #empty list
    print("------welcome to the task management app------")
    total_task = int(input("enter a how many task you want to add =")) #5
    for i in range(1, total_task+1):
        task_name = input(f"enter a task {i} = ") # neter a task 3 =
        tasks.append(task_name)
    print(f"today's tasks are\n{tasks}")
    while True:
        operation= int(input("enter 1-add\n2-update\n3-deleted\n4-view\n5-exit/stop/"))
        if operation == 1 :
            add = input("enter task you want to add = ")
            tasks.append(add)
            print(f"tasks {add} has been successfully added....")
        elif operation == 2:
            updated_val = input("enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("enter new task =")
                ind = tasks.index(updated_val) 
                tasks[ind] = up
                print(f"updated task {up}")
        elif operation ==3:
            del_val = input("which you want to delelt = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
            del tasks[ind] 
            print(f"tasks {del_val} has been deleted   ......") 
        elif operation ==4:
            print(f"total tasks = {tasks}")
        elif operation ==5:
            print("closing the prog........")
            break
        else:
            print("invalid input")
tasks()            
