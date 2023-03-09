from turtle import Turtle

START = [(0,0), (-20,0), (-40,0)]
STEP = 15

class Snake():

    def __init__ (self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in START:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(i)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.segments[0].forward(STEP)
    
    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
        