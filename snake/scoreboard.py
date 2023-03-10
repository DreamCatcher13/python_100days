from turtle import Turtle
ALIGEMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):
        
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0        
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGEMENT, font=FONT)

    def increase_score(self): 
        self.score += 1       
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGEMENT, font=FONT)
        