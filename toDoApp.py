# toDoApp.py

tasksList=[]

def addtask(taskToAdd) :
    tasksList.append(taskToAdd)
    print("task added!")

# Iterates to the tasks list and prints it 
def showTasks( ):
    if (len(tasksList) == 0):
        print("no tasks yet")
    else:
        for i in range (len(tasksList)):
            print(i + 1, "-" , tasksList[i])

def removeTask(taskToRemove):
    tasksList.pop(taskToRemove - 1) 
    print("task removed!!")

# Main function
def main():
    while True:
        # To-Do App UI
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        choice = input("enter choice : ")
        if choice == "1":
            taskToAdd = input("enter task : ")
            addtask(taskToAdd)
        elif choice == "2":
            showTasks()
        elif choice == "3":
            taskToRemove=int(input("enter task no to remove: "))
            try:
                if tasksList[taskToRemove - 1] in tasksList:
                    removeTask(taskToRemove)
                else:
                    print("Task does not exist.")
            except:
                print("Error.")
        elif choice == "4":
            break
        else:
            print("wrong choice!!")

# Calls the main function
main()
