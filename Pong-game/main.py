from turtle import Screen
import time
from divide import DashedLine
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from config import W_HEIGHT, W_WIDTH, MAX_XCOR

window = Screen()
window.setup(height=W_HEIGHT, width=W_WIDTH)
window.bgcolor("black")
window.title("Pong Game")
window.tracer(0)

divider = DashedLine(max_y=int(W_HEIGHT / 2), pen_size=3)
divider.draw()

right_paddle = Paddle(x_pos=MAX_XCOR)
left_paddle = Paddle(x_pos=-MAX_XCOR)

ball = Ball()
score_board = ScoreBoard()

window.listen()
window.onkey(fun=right_paddle.move_up, key="Up")
window.onkey(fun=right_paddle.move_down, key="Down")
window.onkey(fun=left_paddle.move_up, key="w")
window.onkey(fun=left_paddle.move_down, key="s")

game_end = False

while not game_end:
    time.sleep(ball.my_speed)

    ball.move()
    window.update()

    if ball.tb_collision():
        ball.bounce_y()

    # if collided with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > MAX_XCOR - 20 or ball.distance(left_paddle) < 50 and ball.xcor() < -MAX_XCOR + 20:
        ball.bounce_x()

    # if ball goes out of bounds
    if ball.xcor() > MAX_XCOR:  # right side out of bounds
        score_board.left += 1
        score_board.update()
        ball.new_round()

    elif ball.xcor() < -MAX_XCOR: #left side out of bounds
        score_board.right += 1
        score_board.update()
        ball.new_round()

    # Player that scores 10 first, wins!
    if score_board.left == 10:
        score_board.display_winner(winner="LEFT")
        game_end = True
    elif score_board.right == 10:
        score_board.display_winner(winner="RIGHT")
        game_end = True

window.exitonclick()
