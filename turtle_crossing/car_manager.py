from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INC = 5

class CarManager():

    def __init__ (self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)
    
    def level_up(self):
        self.speed += MOVE_INC

