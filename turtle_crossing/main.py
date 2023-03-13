from turtle import Screen
from scoreboard import ScoreBoard
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the road")
screen.tracer(0)

timmy = Player()
board = ScoreBoard()
manager = CarManager()

#board = ScoreBoard()

screen.listen()
screen.onkey(timmy.up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()    

    manager.create_car()
    manager.move()

    #detect collision with the car
    for car in manager.all_cars:
        if timmy.distance(car) < 20:
            board.game_over()
            game_is_on = False
        
    #detect collision with the top
    if timmy.at_finish_line():
        timmy.begin()
        board.update_scoreboard()
        manager.level_up()




screen.exitonclick()