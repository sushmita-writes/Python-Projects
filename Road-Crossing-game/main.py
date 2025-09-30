from turtle import Screen
from configure import W_HEIGHT, W_WIDTH, ROAD_EDGE_Y
from generate_car import Car
from road import Road
from player import Player
import time

window = Screen()
window.setup(width=W_WIDTH, height=W_HEIGHT)
window.bgcolor("gray80")
window.title("Road Crossing Game")
window.tracer(0)

my_road = Road()
my_player = Player()


window.listen()
window.onkey(fun=my_player.move_up, key="Up")

cars = [Car()]

game_end = False
interval = 1

while not game_end:
    time.sleep(0.1)
    window.update()

    for car in cars:
        car.move()

    # the new car to generate at certain interval
    if interval % 5 == 0:
        cars.append(Car())
    interval += 1

    # if player has crossed the road, return it to start
    if my_player.ycor() > ROAD_EDGE_Y + 10:
        my_player.goto_start()



window.exitonclick()
