#Import Modules
import turtle as t

#Create Class
class PlayerClass(t.Turtle): #Inharite Turtle Class

    def __init__(self):
        super().__init__()
        self.starting_position=(0,-240) #Make Starting Position
        self.create_trutle()
        self.draw_line()
    
    #Create Turtle
    def create_trutle(self):
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(self.starting_position) #Move Turtle to specific position
    
    #Move Turtle Forward
    def up(self):
        self.forward(10)

    #Move Turtle Backward
    def down(self):
        self.backward(10)

    #Draw finishing Line on Screen
    def draw_line(self):
        line=t.Turtle()
        line.speed("fastest")
        line.hideturtle()
        line.penup()
        line.goto(-250,240)
        line.pendown()
        line.goto(250,240)