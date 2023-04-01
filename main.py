import turtle
import pandas
from turtle import Turtle,Screen

screen=Screen()
screen.title("US states game")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]


while len(guessed_states)<50:


    answer_state= screen.textinput(title=f"{len(guessed_states)}/50 correct states",prompt="What's another state name? ").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        int_x_coordinate=int(state_data.x)
        int_y_coordinate=int(state_data.y)
        t.goto(int_x_coordinate,int_y_coordinate)
        t.write(answer_state)


#states to learn.csv



screen.exitonclick()