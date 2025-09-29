from turtle import Turtle

class DashedLine:

    def __init__(self, max_y, pen_size):
        self.max_y = max_y
        self.dash = Turtle()
        self.dash.pencolor("pink")
        self.dash.pensize(pen_size)
        self.dash.hideturtle()

    def one_dash(self, y_cor, dash_size):
        """Draws one dashed line from y_cor
        in +ve y-axis if dash_size in +ve,
        and in -ve y-axis if dash_size is -ve."""

        y_cor += dash_size
        self.dash.pendown()
        self.dash.goto(x=0, y=y_cor)

        y_cor += dash_size
        self.dash.penup()
        self.dash.goto(x=0, y=y_cor)

    def draw(self):
        """Draws a divider with dashed line"""
        while self.dash.ycor() <= self.max_y:
            self.one_dash(self.dash.ycor(), +20)

        self.dash.goto(x=0, y=-20)

        while self.dash.ycor() >= -self.max_y:
            self.one_dash(self.dash.ycor(), -20)
