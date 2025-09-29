from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
