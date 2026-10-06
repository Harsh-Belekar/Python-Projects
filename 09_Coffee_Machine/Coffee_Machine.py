import coffee_art as art
import coffee_maker as cm

ob=cm.CoffeeMaker()
profit=0
print(art.logo)
is_on=True
while is_on:
    choice=input("\nWhich Coffee you want? [Espresso,Latte,Cappuccino] or Info or Restart: ").lower()

    if choice=='restart':
        cm.Resources=art.data
        print(art.logo)

    elif choice=='info':
        for i in cm.Resources.items():
            print(f"{i[0].capitalize()} : {i[1]}")

        print(f"Money:{profit}")
        
    else:
        profit += ob.display(choice)