import random
import guess_art as art

def check(chance):
    while chance!=0:
        print(f"\nYou have {chance} chance Left.")
        guess=int(input("\nGuess the Number: "))
        if guess==number:
            print(f"\nYou Guess the Number Correct :{guess}")
            break
        elif guess>number:
            print("\nToo High.")
            print("Guess Again.")
            chance-=1
        else:
            print("\nToo Low.")
            print("Guess Again.")
            chance-=1

        if chance==0:
            print("\nYou are Out of Chance, Game Over.")
            print(f"The Number is {number}")
            break

mode_list=["easy","hard"]

while True:
    print(art.logo)
    mode=""
    number=random.randint(1,100)
    
    print("\nWelcome to Number Gussing Game.")
    while mode not in mode_list:
        mode=input("Choose the Mode [Easy or Hard] : ").lower()

    if mode=="easy":
        chance=10
        check(chance)
    else:
        chance=5
        check(chance)

    start=input("\nDid You want to Play Again? [Yes or No] : ").lower()
    if start!="yes":
        break