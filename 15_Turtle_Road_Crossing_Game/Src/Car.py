#Import Modules
import turtle as t
import random

#Create Class
class CarClass(): #Inharite Turtle Class

    def __init__(self):
        super().__init__()
        t.colormode(255) #Set color Mode to RGB color mode
        self.speed=5 #Set Car Speed
        self.all_cars=[] #Car list

    #Choose Random Color
    def random_color(self):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color=(r,g,b)

        return color
    
    #Display Car's on Screen 
    def drive_car(self):
        random_chance=random.randint(1,5)
        if random_chance==1:
            self.create_car()

    #Create Car 
    def create_car(self):
        new_car=t.Turtle("square")
        new_car.penup()
        new_car.color(self.random_color()) #Choose Random Color
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        random_y=random.randint(-210,225) #Set Car's Random Y_Position
        new_car.setheading(180)
        new_car.goto(300,random_y) #Display Car on Specific Position
        self.all_cars.append(new_car) #Add Car in Car_list
    
    #Move Car Forward
    def move_car(self):
        for move in self.all_cars:
            move.forward(self.speed)