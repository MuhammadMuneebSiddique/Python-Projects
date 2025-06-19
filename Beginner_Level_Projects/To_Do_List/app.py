
def add_task():
    tasks = []
    while True:
        task = input("Enter the Task you can add and 'exit' to quit: ")
        tasks.append(task)

        if task.lower() == "exit":
            break
        
        show_task = input("Press enter to show the task: ")
        if show_task == "":
            num = 0
            for items in tasks:
                num += 1
                print(F"Task 0{num} : {items}")

add_task()
