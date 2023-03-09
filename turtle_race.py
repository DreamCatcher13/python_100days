from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Place a bet!", 
                            prompt="Who is gonna win: red, orange, yellow, green, blue, purple?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -150
all_turtles = []
is_game_on = False

"""Drawing a finish line"""
judge = Turtle()
judge.hideturtle()
judge.penup()
judge.goto(x=250, y=270)
judge.pendown()
judge.goto(x=250, y=-270)
""" """

for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(c)
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 270:
            win = turtle.pencolor()
            if win == user_bet:
                print(f"You've won! The {win} turtle is the winner!")
            else:
                print(f"You've lost! The {win} turtle is the winner!")
            is_game_on = False
            continue
        rand_step = random.randint(0, 10)
        turtle.forward(rand_step)




screen.exitonclick()