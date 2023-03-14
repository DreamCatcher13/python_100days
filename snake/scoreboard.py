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
        self.high_score = self.get_high_score()    
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
            with open("data.txt", "w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        try:
            with open("data.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write("0")
                return 0

