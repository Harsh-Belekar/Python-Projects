#import Modules
import turtle as t
import random

#Create Food class
class FoodClass(t.Turtle): #Inharite Turtle Class

    #Create Food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #Set Size of the Food
        self.color("blue")
        self.speed("fastest")
        self.display_food()

    #Display Food on Screen Randomly
    def display_food(self):
        random_x=random.randint(-230,230)
        random_y=random.randint(-230,230)
        self.goto(random_x,random_y) #Move to Specific Position