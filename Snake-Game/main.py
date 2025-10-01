from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WINDOW_W = 620
WINDOW_H = 540


window = Screen()
window.setup(width=WINDOW_W, height=WINDOW_H)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0) #tracer off

my_snake = Snake()
snake_food = Food()
my_scoreboard = Scoreboard()

window.listen()
window.onkey(my_snake.right, "Right")
window.onkey(my_snake.left, "Left")
window.onkey(my_snake.up, "Up")
window.onkey(my_snake.down, "Down")

def hit_right():
    return my_snake.head.xcor() > 300

def hit_left():
    return my_snake.head.xcor() < -300

def hit_up():
    return my_snake.head.ycor() > 260

def hit_down():
    return my_snake.head.ycor() < -260

game_over = False

while not game_over:
    window.update()
    time.sleep(0.12)
    
    my_snake.move()

    # Detect if snake eats the food
    if my_snake.head.distance(snake_food) <= 15:
        my_snake.grow()
        snake_food.new()
        my_scoreboard.increment_score()

    # Detect if snake hits the wall
    if hit_right() or hit_left() or hit_up() or hit_down():
        my_scoreboard.update_high_score()
        my_snake.reset()

    # Detect if snake eats its tail
    for segment in my_snake.segments[1:]:  # slicing head
        if my_snake.head.distance(segment) < 10:
            my_scoreboard.update_high_score()
            my_snake.reset()

window.exitonclick()
