from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to snake game :)")

snake = []
for i in [0, -20, -40]:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=i, y=0)
    snake.append(new_turtle)












screen.exitonclick()