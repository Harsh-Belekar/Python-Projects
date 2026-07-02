#Import Module
import turtle as t

#Create Score class
class ScoreClass(t.Turtle): #Inharite Turtle Class

    def __init__(self):
        super().__init__()
        self.level=1
        self.display_level()

    #Display Level on Screen
    def display_level(self):
        self.clear() #To Clear the Prevoius Text
        self.penup()
        self.hideturtle()
        self.goto(-260,240) #Display Test on Screen in Specific Position
        self.write(f"Level {self.level}",align="center",font=("courier",15,"bold")) #Display Text on Screen
    
    #Check the User Win the Game or Not
    def check(self):
        if self.level==6:
            self.goto(0,240) #Display Test on Screen in Specific Position
            self.write("You Win the Game.",align="center",font=("courier",20,"bold")) #Display Text on Screen
            return True
        
        return False

    #Display Game Over on Screen 
    def gameover(self):
        self.goto(0,240) #Display Test on Screen in Specific Position
        self.write("Game Over",align="center",font=("courier",20,"bold")) #Display Text on Screen