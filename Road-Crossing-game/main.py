from turtle import Screen
from configure import W_HEIGHT, W_WIDTH
from generate_car import Car
import time

window = Screen()
window.setup(width=W_WIDTH, height=W_HEIGHT)
window.bgcolor("black")
window.title("Road Crossing Game")
window.tracer(0)

car = Car()

game_end = False

while not game_end:
    time.sleep(0.1)
    window.update()

window.exitonclick()
