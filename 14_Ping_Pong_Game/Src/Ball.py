#Import Turtle module
import turtle as t

class BallClass(t.Turtle): #Inharite Turtle Class

    def __init__(self) :
        super().__init__()
        self.create_ball()
        self.x_move=10 #coordinate for ball Move 
        self.y_move=10 #coordinate for ball Move 
        self.ball_speed=0.1 #ball speed
    
    #Create Ball
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    #Move Ball
    def move_ball(self):
        self.speed("fastest")
        new_x=self.xcor()+self.x_move #change Ball Coordinate
        new_y=self.ycor()+self.y_move #change Ball Coordinate
        self.goto(new_x,new_y) #move Ball to specific Position
    
    #Make ball Bounce with Wall
    def wall_bounce(self):
        self.y_move *= -1 #Change ball Y-coordinate
    
    #Make ball Bounce with Paddle
    def paddle_bounce(self):
        self.x_move *= -1 #Change ball X-coordinate
        self.ball_speed*=0.9 #Increase ball speed
    
    #Reset the Ball Position
    def reset_position(self):
        self.goto(0,0) #Move Ball to default Poistion 
        self.ball_speed=0.1 #Reset ball speed
        self.paddle_bounce()