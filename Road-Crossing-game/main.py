from turtle import Screen
from configure import W_HEIGHT, W_WIDTH
from generate_car import Car
import time

window = Screen()
window.setup(width=W_WIDTH, height=W_HEIGHT)
window.bgcolor("black")
window.title("Road Crossing Game")
window.tracer(0)

cars = [Car()]

game_end = False
interval = 1

while not game_end:
    time.sleep(0.1)
    window.update()

    for car in cars:
        car.move()

    # get the new car to generate only after certain interval
    if interval % 5 == 0:
        cars.append(Car())
    interval += 1


window.exitonclick()
