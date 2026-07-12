#Hangman Game
import random
import hangman_art as art

print(art.logo)
chosen_word=random.choice(art.words).upper()

def add():
    print("The word is : ",end="")
    for i in display:
        print(i,end=" ")

display=[]
word_length=len(chosen_word)

for i in range(word_length):
    display.append("_")

add()

life=7
gameovar=False

while not gameovar:    
    guess=input("\n\nGuess the Letter: ").upper()

    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess

    if guess not in chosen_word:
        life-=1
        print(art.stages[life])
        if life==0:
            print(art.logo)
            print(art.stages[life])
            gameovar=True
            print(art.lose)
            print(f"\nThe word is : {chosen_word} ")
            break

    print(art.logo)

    if life < 7:
        print(art.stages[life])

    add()   

    if '_' not in display:
        gameovar=True
        print(art.win)