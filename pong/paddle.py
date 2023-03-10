from turtle import Turtle

class Paddle(Turtle):

    def __init__ (self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.showturtle()

    def up(self):
        ycor = self.ycor() + 20
        self.goto(x=self.xcor(), y=ycor)

    def down(self):
        ycor = self.ycor() - 20
        self.goto(x=self.xcor(), y=ycor)