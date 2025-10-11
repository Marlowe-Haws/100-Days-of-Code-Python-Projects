from turtle import Screen
import time

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.ycor() > player.ycor():
            if car.distance(player) < 25:
                game_is_on = False
                scoreboard.game_over()
        else:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

    # Detect successful crossing
    if player.passed_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
