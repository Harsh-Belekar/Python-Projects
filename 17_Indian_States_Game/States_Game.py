import turtle as t
import pandas

screen=t.Screen()
screen.setup(900,600)
screen.title("States Guessing Game.")

image="./Assets/blank map.gif"
screen.addshape(image)
t.shape(image)

data=pandas.read_csv("./Assets/States name.csv")

states_list=data.States.to_list()
guessed_states=[]

def display_state():
    guessed_states.append(answer_state)
    T=t.Turtle()
    T.hideturtle()
    T.penup()
    state_data=data[data.States == answer_state]
    T.goto(int(state_data.x),int(state_data.y))
    T.write(answer_state)

def missing_data():
    missing_states=[state for state in states_list if state not in guessed_states]

    new_dic={"States": missing_states}
    new_data=pandas.DataFrame(new_dic)
    new_data.to_csv("./Assets/Missing States name.csv")

while len(guessed_states)<=36:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/36 States Correct",prompt="What is State Name ?").title()
    if answer_state=="Exit":
        missing_data()
        break

    if answer_state in states_list:
        display_state()
