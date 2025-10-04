# toDoApp.py

tasksList=[]

def addtask(taskToAdd) :
    tasksList.append(taskToAdd)
    print("Task \"" + taskToAdd + "\" successfully added!")

# Iterates to the tasks list and prints it 
def showTasks( ):
    if (len(tasksList) == 0):
        print("Task list is empty..")
    else:
        print("----- Task List -----")
        for i in range (len(tasksList)):
            print(i + 1, "-" , tasksList[i])
        print("---------------------")

def removeTask(taskToRemove):
    print("Task #", taskToRemove, "successfully removed!")
    tasksList.pop(taskToRemove - 1) 

# Main function
def main():
    while True:
        # To-Do App UI
        print("+====== TASK LIST SYSTEM ======+")
        print("|     [1] Add Task             |")
        print("|     [2] Show Tasks           |")
        print("|     [3] Remove Task          |")
        print("|     [4] Exit                 |")
        print("+==============================+")
        choice = input("Choose an Option: ")
        if choice == "1":
            taskToAdd = input("Enter Task Name: ")
            addtask(taskToAdd)
        elif choice == "2":
            showTasks()
        elif choice == "3":
            showTasks()
            taskToRemove = int(input("Enter Task # to Remove: "))
            try:
                if tasksList[taskToRemove - 1] in tasksList:
                    removeTask(taskToRemove)
                else:
                    print("Task does not exist.")
            except:
                print("Error.")
        elif choice == "4":
            print("Thank you, goodbye!")
            break
        else:
            print("Invalid Input, Please Try Again..")

# Calls the main function
main()
