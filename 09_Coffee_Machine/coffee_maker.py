import coffee_art as art

Resources=art.resources
class CoffeeMaker:

    def is_resource_sufficient(self,order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item]>=Resources[item]:
                print(f"Sorry,We dont have enough {item}.")
                return False
            
        return True
    
    def money(self,price):
        pay=int(input(f"Please Enter {price} Rs.: ")) 
        if pay>price:
            change=pay-price
            print(f"Here's your Change {change} Rs.")
            return True
        
        if pay!=price :
            print("Sorry you dont have enough Money. Money Refunded.")
            return False
        
        return True
    
    def make_coffee(self,coffee_name,coffee_ingredients):    
        for item in coffee_ingredients:
            Resources[item]-=coffee_ingredients[item]

        print(f"Here is your {coffee_name} ☕.")

    def display(self,choice):
        try:
            drink=art.MENU[choice]
            if  self.is_resource_sufficient(drink["ingredients"]):
                if self.money(drink["cost"]):
                    self.make_coffee(choice,drink["ingredients"])
                    return drink["cost"]
        except :
            print(f"Sorry, We dont have '{choice}' coffee.")  
    
