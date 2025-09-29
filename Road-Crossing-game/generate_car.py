from turtle import Turtle
from configure import X_MAX

class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.teleport(x=X_MAX + 10, y=0)
