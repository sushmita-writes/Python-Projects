from turtle import Turtle
from config import MAX_YCOR, BASE_SPEED

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.my_speed = BASE_SPEED

    def move(self):
        x = self.xcor() + self.x_step
        y = self.ycor() + self.y_step
        self.goto(x, y)

    def tb_collision(self):
        """Returns true if Ball object collides with top or bottom of the window."""
        return self.ycor() > MAX_YCOR or self.ycor() < -MAX_YCOR

    def bounce_y(self):
        """pre: Ball object collided to the top or bottom of the window
        post: Reverses y-direction of the Ball object"""
        self.y_step *= -1

    def bounce_x(self):
        """pre: Ball object collided to paddle
        post: Reverses x-direction of the Ball object"""
        self.x_step *= -1
        self.my_speed *= 0.9

    def new_round(self):
        """Reset ball's position and direct it to new direction"""
        self.teleport(0, 0)
        self.my_speed = BASE_SPEED
        self.bounce_x()
