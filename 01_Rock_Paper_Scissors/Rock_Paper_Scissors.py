import random
import rock_art as rk

print("Welcome to Rock,Paper & Scissors Game!")

def user_art(user_choice):
    computer_choice=random.randint(0,2)
    if user_choice=="rock":
        u_art=rk.rock
        user_choice=0
    elif user_choice=="paper":
        u_art=rk.paper
        user_choice=1
    elif user_choice=="scissors":
        u_art=rk.scissors
        user_choice=2
    else:
        print("please select valid option!")
        choice()
    print(f"You Choice[{user_choice}]:{u_art}")
    computer_art(computer_choice)
    result(user_choice,computer_choice)
        
def computer_art(computer_choice):
    if computer_choice==0:
        c_art=rk.rock
    elif computer_choice==1:
        c_art=rk.paper
    elif computer_choice==2:
        c_art=rk.scissors
    print(f"Computer Choice[{computer_choice}]:{c_art}")

def choice():
    user_choice=input("\nWhat did you choice? [Rock,Paper or Scissors] : ").lower()
    user_art(user_choice)

def playagain():
    play=input("\nWant to play again ? [Yes or No]: ").lower()
    if play=="yes" or play=="y":
        choice()

def result(user_choice,computer_choice):
    if user_choice==0:
        if computer_choice==0:
            print("It's Tie.") 
        elif computer_choice==1:
            print("You Lose.")
        else :
            print("You Win.")
    if user_choice==1:
        if computer_choice==0:
            print("You Win.")
        elif computer_choice==1:
            print("It's Tie.") 
        else :
            print("You Lose.")

    if user_choice==2:
        if computer_choice==0:
            print("You Lose.")
        elif computer_choice==1:
            print("You Win.")
        else :
            print("It's Tie.") 

    playagain()
    
choice()