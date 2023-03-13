from turtle import Turtle
ALIGEMENT = "left"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
        
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 0       
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGEMENT, font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER", align=ALIGEMENT, font=FONT)
