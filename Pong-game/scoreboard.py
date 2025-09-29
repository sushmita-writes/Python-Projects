from turtle import Turtle
from config import MAX_YCOR

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.right = 0
        self.left = 0
        self.pencolor("pink")
        self.update()

    def update(self):
        self.clear()
        self.teleport(x=-100, y=MAX_YCOR - 20)
        self.write(arg=self.left, align="center", font=("Times New Roman", 20, "bold"))
        self.teleport(x=100, y=MAX_YCOR - 20)
        self.write(arg=self.right, align="center", font=("Times New Roman", 20, "bold"))

    def display_winner(self, winner):
        self.teleport(x=0, y=0)
        if winner == "DRAW":
            self.write(arg="DRAW!!", align="center", font=("Times New Roman", 30, "bold"))
        else:
            self.write(arg=f"{winner} WINS!!", align="center", font=("Times New Roman", 30, "bold"))