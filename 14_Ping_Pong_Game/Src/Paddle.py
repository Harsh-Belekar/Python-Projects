#Import Turtle Module
import turtle as t

#Create PAddle Class 
class PaddleClass(t.Turtle): #Inharite Turtle Class
    
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

    #Create Paddle
    def create_paddle(self,position):
            self.shape("square")
            self.color("white")
            self.penup()
            self.shapesize(stretch_wid=5,stretch_len=1) #Set Paddle Size
            self.goto(position) #Move to Specific Position

    #Move Left Paddle Upward        
    def left_up(self):
        new_x=self.xcor()
        new_y=self.ycor()+20
        #Prevent Paddle from going Outside the Screen
        if self.ycor() < 200: 
            self.goto(new_x,new_y) #Move to Specific Position

    #Move Left Paddle Downward    
    def left_down(self):
        new_x=self.xcor()
        new_y=self.ycor()-20
        #Prevent Paddle from going Outside the Screen
        if self.ycor() > -200: 
            self.goto(new_x,new_y) #Move to Specific Position

    #Move Right Paddle Upward    
    def right_up(self):
        new_x=self.xcor()
        new_y=self.ycor()+20
        #Prevent Paddle from going Outside the Screen
        if self.ycor() < 200: 
            self.goto(new_x,new_y) #Move to Specific Position

    #Move Right Paddle Downward    
    def right_down(self):
        new_x=self.xcor()
        new_y=self.ycor()-20
        #Prevent Paddle from going Outside the Screen
        if self.ycor() > -200: 
            self.goto(new_x,new_y) #Move to Specific Position         