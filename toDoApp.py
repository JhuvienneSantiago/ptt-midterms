tasks=[]

# Adds a task to the tasks list
def addtask(task) :
  tasks.append(task)
  print("task added!")

# Iterates to the tasks list and prints it 
def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

# Removes items to the tasks list
def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

# Main function
def main():
    while True:
        # To-Do App UI
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")

# Calls the main function
main()
