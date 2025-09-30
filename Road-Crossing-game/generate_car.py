from turtle import Turtle
from configure import X_MAX, ROAD_EDGE_Y, car_speed, light_colors
import random


class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color(random.choice(light_colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y = random.randint(-ROAD_EDGE_Y + 10, ROAD_EDGE_Y - 10)
        self.teleport(x=X_MAX + 30, y=self.y)
        self.penup()

    def move(self):
        x = self.xcor()
        # move the car only within the bounds
        if x > -X_MAX - 20:
            self.goto(x=x - car_speed, y=self.y)
