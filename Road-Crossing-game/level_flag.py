from turtle import Turtle
from configure import X_MAX, Y_MAX, FONT

class Level(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.teleport(x=-X_MAX + 30, y=Y_MAX - 50)
        self.color("gray10")
        self.level = 1
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(arg=f"LEVEL: {self.level}", align="left", font=FONT)