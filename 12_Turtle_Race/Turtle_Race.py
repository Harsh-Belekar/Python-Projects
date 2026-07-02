import turtle as t
import random 
screen=t.Screen()
screen.setup(width=600,height=500)

colors_list=["red","orange","pink","green","blue","purple"]
turtle_list=[]

user_bet=screen.textinput(title="Make a Bet.",prompt="Which Turtle Win?, Enter a color \n"
                "[red,blue,green,pink,orange,purple] : ")
position=[105,70,35,0,-35,-70]

for i in range(0,6):
    color=colors_list[i]
    color=t.Turtle(shape="turtle")
    color.penup()
    color.color(colors_list[i])
    color.goto(x=-280,y=position[i])
    turtle_list.append(color)

T=t.Turtle()
T.penup()
T.hideturtle()
T.goto(x=280,y=150)
T.right(90)
T.pendown()
T.pensize(2)
T.forward(280)

race=True
while race:
    for turtle in turtle_list:
        if turtle.xcor()>280:
            winner=turtle.pencolor()
            race=False
        move=random.randint(1,10)
        turtle.forward(move)

if winner == user_bet.lower():
    print(f"You Win, {winner.capitalize()} Turtle Win the Race.")
else:
    print(f"You Lose, {winner.capitalize()} Turtle Win the Race.")

screen.mainloop()