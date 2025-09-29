from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("palegreen")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.new()


    def new(self):
        rx = random.randint(-290, 290) # window_width / 2  - 20
        ry = random.randint(-250, 240) # window_height / 2 - 20
        self.goto(x=rx, y=ry)
