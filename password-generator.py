import random
import string
def main():
    while True:
        val=string.ascii_letters
        val+=string.digits
        val+=string.punctuation

        len=int(input("Enter length: "))
        password=" "
        
        for i in range(len):
            password+=random.choice(val)

        print("Genarated password is :",password)
    
if __name__=="__main__":
    main()
