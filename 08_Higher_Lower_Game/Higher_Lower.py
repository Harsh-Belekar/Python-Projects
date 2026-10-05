import random
import high_low_art as art

def select():
    return random.choice(art.data)

def display(account):
    for item in account.items():
        key=item[0].capitalize()
        value=item[1]
        if key!="Follower_count":
            print(f"{key} : {value}")

def start(account_1,account_2):
    print(art.logo)
    print("\nCompare A:\n")
    display(account_1)
    print(art.vs)
    print("\nAgainst B:\n")
    display(account_2)

def getFollower(account):
    for item in account.items():
        key=item[0].capitalize()
        value=item[1]
        if key=="Follower_count":
            return value
        
def check(guess,account_1,account_2,question):
    follower_1=getFollower(account_1)
    follower_2=getFollower(account_2)
    
    if question=="High":
        if follower_1>follower_2:
            res="A"
        else:
            res="B"
    else:
        if follower_1<follower_2:
            res="A"
        else:
            res="B"

    if guess==res:
        ans=True
    else:
        ans=False
    return ans

question_list=["High","Low"]
account_1=select()
over=False
score=0
while not over:
    account_2=select()
    while account_1==account_2:
        account_2=select()
    start(account_1,account_2)
    question=random.choice(question_list)
    guess=input(f"\nWho has {question}est Follower? [A or B] : ").upper()
    result=check(guess,account_1,account_2,question)

    if result:
        score+=1
        print(f"\nYou are Right. Your Curent Score is :{score}")
        if guess=="B":
            account_1=account_2

    else:
        print(f"\nYou are Wrong. Your Final Score is :{score}")
        over=True