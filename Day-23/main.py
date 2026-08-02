import time
import random
from turtle import Screen
from player import FINISH_LINE_Y, Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if random.randint(1,6) == 1:
        car_manager.create_car()
    car_manager.move_cars()


    # At finish line
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.increase_level()
        player.reset_pos()
        car_manager.level_up()

    # Collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()