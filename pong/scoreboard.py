from turtle import Turtle
ALIGEMENT = "center"
FONT = ("Courier", 60, "normal")


class ScoreBoard(Turtle):
        
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0   
        self.r_score = 0     
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGEMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGEMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


