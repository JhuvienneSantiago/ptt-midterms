# toDoApp.py

tasks=[]

def addtask(task) :
    tasks.append(task)
    print("Task \"" + task + "\" successfully added!")

def showTasks( ):
    if len(tasks) == 0:
        print("Task list is empty..")
    else:
        print("----- Task List -----")
        for i in range (len(tasks)):
            print(i+1,"-",tasks[i])
        print("---------------------")

def removetask(tasknumber):
    print("Task #", tasknumber, "successfully removed!")
    tasks.pop(tasknumber)

def main():
    while True:
        print("+====== TASK LIST SYSTEM ======+")
        print("|     [1] Add Task             |")
        print("|     [2] Show Tasks           |")
        print("|     [3] Remove Task          |")
        print("|     [4] Exit                 |")
        print("+==============================+")
        ch = input("Choose an Option: ")
        if ch == "1":
            t = input("Enter Task Name: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            showTasks()
            n = int(input("Enter Task # to Remove: "))
            removetask(n)   
        elif ch == "4":
            print("Thank you, goodbye!")
            break
        else:
            print("Invalid Input, Please Try Again..")
main()