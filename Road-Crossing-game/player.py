from turtle import Turtle
from configure import ROAD_EDGE_Y

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("aquamarine4")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.teleport(x=0, y=-ROAD_EDGE_Y - 30)

    def move_up(self):
        self.forward(10)