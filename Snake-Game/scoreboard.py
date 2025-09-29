from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.pendown()
        self.pencolor("white")
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align='center', font=('Arial', 10, 'normal'))

    def increment_score(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.pencolor("red")
        self.write(arg=f"GAME OVER", align='center', font=('Arial', 18, 'bold'))
        self.pencolor("white")
        self.goto(0, -18)
        self.write(arg=f"Final Score: {self.score}", align='center', font=('Arial', 10, 'normal'))

