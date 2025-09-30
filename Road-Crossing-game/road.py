from turtle import Turtle

class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.color("gray20")
        self.shape("square")
        self.shapesize(stretch_wid=18, stretch_len=30)
