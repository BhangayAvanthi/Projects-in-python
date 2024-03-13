def main():
    while True:
        print("*****Simple Calculator*****")
        a=float(input("enter a: "))
        b=float(input("enter b: "))
        print("operations")
        print("1.add")
        print("2.subtract")
        print("3.multiply")
        print("4.divide")
        print("5.exit")
        ch=int(input("\nEnter choice: "))
        if ch==1:
            print("result: ",a+b)
        elif ch==2:
            print("result: ",a-b)
        elif ch==3:
            print("result: ",a*b)
        elif ch==4:
            print("result: ",a/b)
        else:
            print("exiting")
            break
    
if __name__=="__main__":
    main()
