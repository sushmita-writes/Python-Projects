from turtle import Turtle
from config import W_HEIGHT

class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.x_pos = x_pos
        self.color("pink")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=self.x_pos, y=0)

    def move_up(self):
        cur_y = self.ycor()
        if cur_y > int(W_HEIGHT / 2 - 60):
            pass
        else:
            self.goto(y=cur_y + 20, x=self.x_pos)

    def move_down(self):
        cur_y = self.ycor()
        if cur_y < -int(W_HEIGHT / 2 - 60):
            pass
        else:
            self.goto(y=cur_y - 20, x=self.x_pos)
