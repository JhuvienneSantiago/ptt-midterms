# The tasks "database"
tasksList=[]

# Adds a new task to the tasksList
# Parameters: taskToAdd (str) - the task description
# Side effect: Prints confirmation message
def addtask(taskToAdd) :
    tasksList.append(taskToAdd)
    print("Task \"" + taskToAdd + "\" successfully added!")

# Displays all tasks in the tasksList
# If no tasks exist, shows a message instead 
def showTasks( ):
    if (len(tasksList) == 0):
        print("Task list is empty..")
    else:
        print("----- Task List -----")
        for i in range (len(tasksList)):
            print(i + 1, "-" , tasksList[i])
        print("---------------------")

# Removes a task by its task number (1-based index)
# Parameters: taskToRemove (int) - the task number to delete
# Side effect: Prints confirmation message
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
            # Add new task
            taskToAdd = input("Enter Task Name: ")
            addtask(taskToAdd)
        elif choice == "2":
            showTasks()
        elif choice == "3":
            # Show tasks first, then prompt the user to remove a task by number
            showTasks()
            taskToRemove = int(input("Enter Task # to Remove: "))
            try:
                # Validate then tries to remove
                if tasksList[taskToRemove - 1] in tasksList:
                    removeTask(taskToRemove)
                else:
                    print("Task does not exist.")
            except:
                # Handles invalid inputs
                print("Error.")
        elif choice == "4":
            # Simply exits the program
            print("Thank you, goodbye!")
            break
        else:
            # Input validation
            print("Invalid Input, Please Try Again..")

# Calls the main function
main()
