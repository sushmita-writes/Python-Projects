from turtle import Screen
from configure import W_HEIGHT, W_WIDTH, ROAD_EDGE_Y, car_speed, increase_speed_by
from generate_car import Car
from road import Road
from player import Player
from status_flag import Level, GameOver
import time
import random

window = Screen()
window.setup(width=W_WIDTH, height=W_HEIGHT)
window.bgcolor("gray80")
window.title("Road Crossing Game")
window.tracer(0)

my_road = Road()
my_player = Player()
level = Level()

window.listen()
window.onkeypress(fun=my_player.move_up, key="Up")

cars = [Car()]

game_end = False

while not game_end:
    time.sleep(0.1)
    window.update()

    # the new car to generate at random times
    chance = random.randint(1, 5)
    if chance == 5:
        cars.append(Car())

    for car in cars:
        car.move(car_speed)
        # detect collision with cars
        if my_player.distance(car) < 20:
            game_over = GameOver()
            game_end = True
            break

    # if player has crossed the road, level up and return it to start
    if my_player.ycor() > ROAD_EDGE_Y + 10:
        level.update()
        car_speed *= increase_speed_by
        my_player.goto_start()

window.exitonclick()
