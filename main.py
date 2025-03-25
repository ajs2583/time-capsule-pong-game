from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
TOP_BOARD = 280
BOTTOM_BOARD = -280
# Goal constants
GOAL_RIGHT = 380
GOAL_LEFT = -380


# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# Paddle Initialization
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Ball setup
ball = Ball()

# Scoreboard setup
scoreboard = Scoreboard()

# Key-stroke event-listener
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with bottom walls
    if ball.ycor() > TOP_BOARD or ball.ycor() < BOTTOM_BOARD:
        ball.bounce_y()

    # Detect collision with right paddle
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect if ball goes out of bounds
    # right player
    if ball.xcor() > GOAL_RIGHT:
        time.sleep(0.3)
        ball.reset_position()
        scoreboard.right_point()

    if ball.xcor() < GOAL_LEFT:
        time.sleep(0.3)
        ball.reset_position()
        scoreboard.left_point()


screen.exitonclick()
