#Import Turtle module
import turtle as t

#Create Score class
class ScoreClass(t.Turtle):#Inharite Turtle Class

    def __init__(self):
        super().__init__()
        self.left_score=0 #Set plays Score
        self.right_score=0 #Set plays Score
        self.penup()
        self.color("white")
        self.hideturtle()
        self.display_score()

    #Display Score on Screen
    def display_score(self):
        self.clear() #To Clear the Prevoius Text
        self.goto(-100,200) #Display Test on Screen in Specific Position
        self.write(self.left_score,align="center",font=("courier",35,"normal")) #Display Score on Screen
        self.goto(100,200) #Display Test on Screen in Specific Position
        self.write(self.right_score,align="center",font=("courier",35,"normal")) #Display Score on Screen
    
    #Increase Left Player Score
    def l_score(self):
        self.left_score+=1
        self.display_score()
    
    #Increase Right Player Score
    def r_score(self):
        self.right_score+=1
        self.display_score()
    
    #Check Who Win The Game
    def check(self):
        if self.right_score==11: #Check the Right player score is 11 or not
            self.goto(0,0) #Display Test on Screen in Specific Position
            self.write("Right Player Win.",align="center",font=("courier",20,"normal")) #Display Winner on Screen
            return True
        elif self.left_score==11: #Check the Left player score is 11 or not
            self.goto(0,0) #Display Text on specific Position on Screen
            self.write("Left Player Win.",align="center",font=("courier",20,"normal")) #Display Winner on Screen 
            return True

        return False