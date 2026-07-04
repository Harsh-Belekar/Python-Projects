#Importing modules
import turtle as t
import time
import Snake
import Food
import Score_Board

#Create objects
snake=Snake.SnakeClass()
food=Food.FoodClass()
score=Score_Board.ScoreClass()
screen=t.Screen()

#Setup main Screen 
screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #Off Turtle Animation

#Adding key to Move snake 
screen.listen() #Setup Program to Take user Input
screen.onkey(snake.Up,"Up") #Move Snake UP
screen.onkey(snake.Down,"Down") #Move Snake Down
screen.onkey(snake.Left,"Left") #Move Snake Left
screen.onkey(snake.Right,"Right") #Move Snake Right

#Game On
game_on=True
while game_on:
    screen.update() #Fast Forward Turtle Animation
    time.sleep(0.1) #Add 0.1 Second Delay on Snake Movement
    snake.move() #Move Snake Forword
    score.display_score() #Display Current Score
    score.check_highscore()#Keep Track of HighScore

    #Display Food & Score on screen and Add Snake Tail
    if snake.head.distance(food) < 15:
        food.display_food() #Display Food on Screen
        snake.add_tail() #Add Snake Tail
        score.update_score() #Update Score

    #Check the Snake touch the end of the Screen 
    if snake.head.xcor()> 245 or snake.head.xcor()< -245 or snake.head.ycor()> 245 or snake.head.ycor()< -245:
        game_on=False #Game Stop
        score.gameover()
    
    #Check the Snake touch it's own body 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10 :
            game_on=False #Game Stop
            score.gameover()

screen.mainloop()