from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.listen()
game_is_on = True
ball_speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(ball_speed)
    scoreboard.update_scoreboard()
    ball.move()
    # Detect collision with wall or paddles.
    if ball.y > 280:
        ball.bounce("top")
    elif ball.y < -280:
        ball.bounce("bottom")
    elif ball.distance(r_paddle) < 50 and 360 > ball.x > 330:
        ball.bounce("right")
        if ball_speed > 0.01:
            ball_speed -= 0.01
    elif ball.distance(l_paddle) < 50 and -360 < ball.x < -330:
        ball.bounce("left")
        if ball_speed > 0.01:
            ball_speed -= 0.01
    # Detect right paddle miss.
    elif ball.x > 380:
        ball.reset_ball()
        scoreboard.player_1_score += 1
        ball_speed = 0.1
    # Detect left paddle miss.
    elif ball.x < -389:
        ball.reset_ball()
        scoreboard.player_2_score += 1
        ball_speed = 0.1
    if scoreboard.player_1_score > 9 or scoreboard.player_2_score > 9:
        game_is_on = False
        scoreboard.final_score()

screen.exitonclick()
