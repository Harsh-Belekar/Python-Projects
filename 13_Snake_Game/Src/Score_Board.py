#Import Module
import turtle as t

font_style=("courier",15,"normal") #Set font Style
#Create Score class
class ScoreClass(t.Turtle): #Inharite Turtle Class

    def __init__(self):
        super().__init__()
        self.score=0
        with open("./Assets/Snake_data.txt","r") as file: #Open File in Read Mode
            self.high_score=int(file.read()) #Set the High Score
        self.display_score()

    #Display Score on Screen
    def display_score(self):
        self.clear() #To Clear the Prevoius Text
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,225) #Display Test on Screen in Specific Position
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=(font_style)) #Display Text on Screen

    #Update Score
    def update_score(self):
        self.score+=1 #Increase Score
    
    #Check HighScore
    def check_highscore(self):
        if self.score > self.high_score: #Check the Current Score is Greater then HighScore or not
            self.high_score=self.score
            with open("./Assets/Snake_data.txt","w") as file: #Open File in Write Mode
                file.write(f"{self.high_score}") #Write HighScore in File

    #Display Game Over on Screen 
    def gameover(self):
        self.goto(0,0) #Display Test on Screen in Specific Position
        self.write("Game Over",align="center",font=(font_style),) #Display Text on Screen