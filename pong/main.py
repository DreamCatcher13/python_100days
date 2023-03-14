from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370,0))
ball = Ball()
board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with top / bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.xcor() > 350 and ball.distance(r_paddle) < 50) or (ball.xcor() < -350 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    # detect paddle missed the ball
    if ball.xcor() > 380:
        ball.reset()
        board.l_point()
        if board.l_score == 10:
            game_is_on = False

    if ball.xcor() < -380:
        ball.reset()
        board.r_point()
        if board.r_score == 10:
            game_is_on = False




screen.exitonclick()