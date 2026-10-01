import auction_art as art

data={}
print("\nWelcome to the Secret Auction Program.")

def result(data):
    print(art.logo)
    max=0
    for name in data:
        amount=data[name]
        if max<amount:
            max=amount
            winner=name

    print(f"\nThe Winner is {winner} with Bid of ${max}")

over=False
while not over:
    print(art.logo)
    name=input("\nwhat is your Name ? : ").capitalize()
    bid=int(input("Enter your Bid's : $"))
    data[name]=bid

    ask=input("\nAny Other Bid's ? [Yes or No] : ").lower()
    if ask=="no":
        over=True
        result(data)
