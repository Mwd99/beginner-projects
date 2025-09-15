#program to make a to-do list 
#my first project
print("Welcome to your to-do list")
print("--------------------------")
chooseTask="Choose a task :\nA. Add a task\nB. View tasks\nC.Remove a task\nD. Exit"

l=[]
m=[]
tasknumber = 0

def addTask ():
    while True : 
        task= input ("Enter your task : ")
        l.append(task)
        nomoreTask = input ("Enter no, if you dont want to add another task, any other key to continue :") 
        if nomoreTask == "no":
            break

while True :
    print(chooseTask)   
    userInput = input("Enter your choice - ")
    if userInput.lower() == "a":
        addTask()
    elif userInput.lower() == "b":
        print(l) 
    elif userInput.lower() == "c":
        remtask=input("Enter taskname to remove :")
        l.remove(remtask)
        print("Task has been removed")
        print("Updated list : ",l)
    elif userInput.lower() == "d":
        print("Thank you!!")
        break   
    else:
        print("Invalid choice")
        
        

