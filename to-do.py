def main():
    tasks=[]
    while True:
        print("*****To do list*****")
        print("1.Add tasks")
        print("2.Remove task when completed")
        print("3.Show tasks")
        print("4.Exit")
        
        ch=int(input("\nEnter choice: "))
        if ch==1:
            nota=int(input("Enter no. of tasks to add: "))
            for i in range(nota):
                task=input("enter task: ")
                tasks.append(task)
                print("Task added!!")
            print("\n")
                
        elif ch==2:
            task_num=int(input("Enter task to delete when completed: "))
            if task_num<len(tasks) and task_num>=0:
                #tasks.remove(task_num-1)
                del tasks[task_num-1]
                print("Task deleted!!")
            else:
                print("Invalid task")
            print("\n")
                
        elif ch==3:
            if not tasks:
                print("no tasks")
            else:
                print("Tasks are:")
                for i,task in enumerate(tasks):
                    print(i+1,task)
            print("\n")
                    
        elif ch==4:
            print("exiting.....")
            break
        
            
if __name__=="__main__":
    main()