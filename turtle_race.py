from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Place a bet!", 
                            prompt="Who is gonna win: red, orange, yellow, green, blue, purple?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
Y = -150
is_game_on = False

def finish():
    """Drawing a finish line"""
    judge = Turtle()
    judge.hideturtle()
    judge.penup()
    judge.goto(x=250, y=270)
    judge.pendown()
    judge.goto(x=250, y=-270)

def turtles(ycor):
    """Creating turtles"""
    turtles = []
    ycor = Y
    for c in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(c)
        new_turtle.penup()
        new_turtle.goto(x=-270, y=ycor)
        ycor += 40
        turtles.append(new_turtle)
    return turtles

if user_bet:
    is_game_on = True
    finish()
    all_turtles = turtles(Y)

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 270:
            win = turtle.pencolor()            
            is_game_on = False
            again = screen.textinput("Play again?", f"The {win} turtle is the winner!\nDo you want to play again? yes/no")
            if again == "yes":
                user_bet = screen.textinput(title="Place a bet!", 
                            prompt="Who is gonna win: red, orange, yellow, green, blue, purple?")
                is_game_on = True
                screen.clear()
                finish()
                all_turtles = turtles(Y)
        rand_step = random.randint(0, 10)
        turtle.forward(rand_step)




screen.exitonclick()