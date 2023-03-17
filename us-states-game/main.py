import turtle
import pandas

screen = turtle.Screen()
screen.title("US States game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

all_data = pandas.read_csv("50_states.csv")
states_list = all_data["state"].to_list()
user_score = 0
while user_score != 50:
    answer = screen.textinput(title=f"{user_score}/50 states",
                          prompt="What's another state name?").title()
    if answer == "Exit":
        break
    if answer in states_list:
        user_score += 1
        new_t = turtle.Turtle()
        new_t.penup()
        new_t.hideturtle()
        state_data = all_data[all_data["state"] == answer]
        xcor = int(state_data.x)
        ycor = int(state_data.y)
        new_t.goto(x=xcor, y=ycor)
        new_t.write(state_data.state.item()) #to get value from a row




