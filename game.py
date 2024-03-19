import random

def user_choice():
    while True:
        #when user enters choice it is to be converted to lower case for comparision
        uchoice=input("select rock,paper or scissors  :").lower()
        if uchoice in ['rock','paper','scissors']:
            return uchoice
        else:
            print("invalid choice, select only one from those options:")
            
            
def computer_choice():
    return random.choice(['rock','paper','scissors'])

def winner(uchoice,cchoice):
    if uchoice==cchoice:
        return "Tie!!"
    elif uchoice=='rock' and cchoice=='scissors':
        return "you won!!"
    elif uchoice=='paper' and cchoice=='rock':
        return "you won!!"
    elif uchoice=='scissors' and cchoice=='paper':
        return "you won!!"
    else:
        return "Computer won!!"
    


def play():
    #initially scores are 0
    user=0
    computer=0
    
    while True:
        uchoice=user_choice()
        cchoice=computer_choice()
        print(f"\n enter ur choice: {uchoice}")
        print(f"\n computer's choice: {cchoice}")
        
        ans=winner(uchoice,cchoice)
        print(ans)
        #if user won score increases for user or for computer
        if ans=="better luck next time":
            computer+=1
        elif ans=="You won !!":
            user+=1
        
        print(f"Scores are: for User:{user} computer:{computer}")
        
        once_more=int(input("\n Wanna play again: ??\n Enter 0 to stop and 1 to play: "))
        if once_more!=1:
            print("Hope u like the game! Thank You!!")
            break
        
play()


        