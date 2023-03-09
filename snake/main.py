from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to snake game :)")
screen.tracer(0) # turn off auto screen updates
                 # you need to explicitly call update() when you want the screen to reflect the current state of the drawing
snake = []
for i in [0, -20, -40]:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=i, y=0)
    snake.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    
    for seg_num in range(len(snake)-1, 0, -1):
        snake[seg_num].goto(snake[seg_num-1].pos())
    snake[0].forward(20)














screen.exitonclick()