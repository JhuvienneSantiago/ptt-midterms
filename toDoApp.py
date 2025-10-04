# toDoApp.py

tasksList=[]

def addtask(task) :
  tasksList.append(task)
  print("task added!")

def showTasks( ):
    if len(tasksList)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasksList)):
      print(i+1,".",tasksList[i])

def removetask(taskNumber):
    tasksList.pop(taskNumber) 
    print("task removed!!")

def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        choice = input("enter choice : ")
        if choice=="1":
            taskToDo = input("enter task : ")
            addtask(taskToDo)
        elif choice=="2":
            showTasks()
        elif choice=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)
        elif choice=="4":
            break
        else:
            print("wrong choice!!")
main()
