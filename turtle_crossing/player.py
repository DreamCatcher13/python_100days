from turtle import Turtle

START = (0, -280)
MOVE_DIST = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.begin()

    def begin(self):
        self.setheading(90)
        self.goto(START)

    def up(self):
        self.forward(MOVE_DIST)

    def at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
