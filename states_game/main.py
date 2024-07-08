from turtle import *
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv('50_states.csv')
score = 0
guess_states = []

while len(guess_states) < 50:
    if score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
        new_answer_state = answer_state.title()
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Corrects", prompt="What's another state's name?")
        new_answer_state = answer_state.title()

    if new_answer_state == "Exit":
        missing_states = [state for state in states['state'] if state not in guess_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    is_there = states['state'].str.contains(new_answer_state, case=True)

    for num, there in enumerate(is_there):
        if there:
            x = states.loc[num]['x']
            y = states.loc[num]['y']
            name = turtle.Turtle()
            name.hideturtle()
            name.penup()
            name.goto(x, y)
            name.write(new_answer_state, font=('Arial', 10, 'bold'))
            score += 1
            guess_states.append(new_answer_state)


screen.exitonclick()
