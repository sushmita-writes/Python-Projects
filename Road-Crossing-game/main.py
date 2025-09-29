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

while not game_end:
    time.sleep(0.1)
    window.update()

    for car in cars:
        car.move()

    new_car = Car()

    # relocate Car object if it overlaps with another
    while True:
        overlap = False
        for car in cars:
            if new_car.distance(car) < 60:
                new_car.relocate()
                overlap = True
                break

        if not overlap:
            break

    cars.append(new_car)

window.exitonclick()
