import turtle as t
import random

T=t.Turtle()
screen=t.Screen()
t.colormode(255)
T.speed("fastest")
T.penup()
T.hideturtle()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)

    return color

T.setheading(225)
T.forward(300)
T.setheading(0)

for i in range(1,101):
    T.dot(10,random_color())
    T.forward(50)

    if i % 10 ==0:
        T.setheading(90)
        T.forward(50)
        T.setheading(180)
        T.forward(500)
        T.setheading(0)



screen.mainloop()