from turtle import Turtle
UNIT_DISTANCE = 20  # constant

class Snake:

    def __init__(self):
        self.segments = []

        # initialize snake
        self.get_segment()  # head
        self.head = self.segments[0]
        for _ in range(2):  # body
            self.grow()

    def get_segment(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)

    def grow(self):
        new_xcor = self.segments[-1].xcor() - 20  # each square is 20 unit long
        new_ycor = self.segments[-1].ycor()

        self.get_segment()
        self.segments[-1].goto(x=new_xcor, y=new_ycor)

    def move(self):
        # range(start, stop, step) NOTE: stop is exclusive
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)
        self.head.forward(UNIT_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        self.get_segment()  # head
        self.head = self.segments[0]
        for _ in range(2):  # body
            self.grow()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
