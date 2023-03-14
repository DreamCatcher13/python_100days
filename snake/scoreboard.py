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
        self.high_score = 0     
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):        
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", False, align=ALIGEMENT, font=FONT)

    def increase_score(self): 
        self.score += 1       
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
