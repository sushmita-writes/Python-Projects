from turtle import Turtle
from configure import X_MAX, CAR_SPEED

class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.teleport(x=X_MAX + 10, y=0)
        self.penup()

    def move(self):
        x = self.xcor()
        y = self.ycor()
        # move the car only within the bounds
        if x > -X_MAX - 20:
            self.goto(x=x - CAR_SPEED, y=y)
