#Imports Modules
import turtle as t
import time
import Paddle
import Ball
import Score_Board

#Creating Objects
screen=t.Screen()
ball=Ball.BallClass()
score=Score_Board.ScoreClass()
right_paddle=Paddle.PaddleClass((370,0)) #Make Right Paddle
left_paddle=Paddle.PaddleClass((-380,0)) #Make Left Paddle

#Setup Screen
screen.setup(width=800,height=500)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)#Turn Off Animation

#Set Turtle to Listen User Input
screen.listen()
screen.onkey(right_paddle.left_up,"Up") #Make Right Paddle to Move Upward
screen.onkey(right_paddle.left_down,"Down") #Make Right Paddle to Move Downward
screen.onkey(left_paddle.right_up,"a") #Make Left Paddle to Move Upward
screen.onkey(left_paddle.right_down,"d") #Make Left Paddle to Move Downward

#Game on
game_on=True
while game_on:
    time.sleep(ball.ball_speed) #Set Ball Speed
    screen.update() #Fast Forward Turtle Animation
    ball.move_ball() #Move Ball

    if ball.ycor() > 228 or ball.ycor() < -225: #Check the Ball Touch the Up and Down screen
        ball.wall_bounce() #Bounce Back Ball

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340: #Check the Ball touch the Right Paddle
        ball.paddle_bounce() #Bounce Back Ball

    if ball.distance(left_paddle) < 50 and ball.xcor() < -350: #Check the Ball touch the Left Paddle
        ball.paddle_bounce() #Bounce Back Ball

    if ball.xcor()>370: #Check the Ball Miss the Right Paddle
        ball.reset_position() #Reset the ball Position
        score.l_score() #Increase the Left Player Score

    if ball.xcor()<-380: #Check the Ball Miss the Left Paddle
        ball.reset_position() #Reset the ball Position
        score.r_score() #Increase the Right Player Score

    if score.check(): #Check Who Player win the Game
        game_on=False #Stopthe Game

screen.mainloop()