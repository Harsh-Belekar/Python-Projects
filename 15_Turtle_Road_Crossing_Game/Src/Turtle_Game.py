#Import Modules
import turtle as t
import time
import Player
import Car
import Score_Board

#Creationg Objects
screen=t.Screen()
player=Player.PlayerClass()
car_manager=Car.CarClass()
score=Score_Board.ScoreClass()

#Setup Screen
screen.screensize(500,500)
screen.title("Turtle Crossing Game.")
screen.tracer(0)#turnOff Animation

#Set program to Take User Inputs
screen.listen()
screen.onkey(player.up,"Up") ##Move Turtle to Forward
screen.onkey(player.down,"Down") ##Move Turtle to Backward

#Game on
game_on=True
while game_on:
    time.sleep(0.1) #Sleep for 0.1 Second
    screen.update() #Fast Forward Turtle Animation

    score.display_level() #Display Level on Screen
    car_manager.drive_car() #Create Car on Screen
    car_manager.move_car() #Move Car 
    
    #Check the Turtle by a Car or Not
    for car in car_manager.all_cars:
        if car.distance(player) <25:
            score.gameover() #Display GameOver Text
            game_on=False #Stop the Game
    
    #Check the Turtle Cross the Road or Not
    if player.ycor() >250:
        player.goto(0,-240) #Move Turtle to Starting Position
        car_manager.speed+=1 #Increase Car Speed
        score.level+=1 #Increase Level
    
    #Check the User Win the Game or Not
    if score.check():
        player.goto(0,-240) #Move Turtle to Starting Position
        game_on=False #Stop the Game

screen.mainloop()