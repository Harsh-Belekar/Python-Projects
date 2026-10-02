import random
import blackjack_art as art

def game():
    play=input("\n\nYou want to play Blackjack[Y or N]: ").lower()
    if play=='y':
        blackjack()

def guess_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and len(cards)==2:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def check(u_score,c_score):
    if u_score==c_score:
        return "\nIt's Tie"
    elif c_score==0:
        return "\nYou Lose,Computer hit Blackjack."
    elif u_score==0:
        return "\nYou Win,With Blackjack."
    elif u_score>21:
        return "\nYou Lose,With Burst."
    elif c_score>21:
        return "\nYou win,Computer hit Burst."
    elif u_score>c_score:
        return "\nYou Win."
    else:
        return "\nYou Lose."

def blackjack():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    
    for _ in range(2):
        user_cards.append(guess_cards())
        computer_cards.append(guess_cards())

    game_over=False
    while not game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your Cards:{user_cards}, Current Score:{user_score}")
        print(f"Computer First Card:{computer_cards[0]}")

        while computer_cards!=0 and computer_score<17:
            computer_cards.append(guess_cards())
            computer_score=calculate_score(computer_cards)

        if user_score > 21:
            break

        if user_score==0 or computer_score==0:
            game_over=True

        else:
            choice=input("\nYou want another card ?[Y or N]: ").lower()
            if choice=="y":
                user_cards.append(guess_cards())
                user_score=calculate_score(user_cards)

            else:
                game_over=True

    print(check(user_score,computer_score))

    print(f"\nYour Final Cards:{user_cards}, Final Score:{user_score}")
    print(f"\nComputer Final Cards:{computer_cards},Final Score:{computer_score}")
    game()

game()