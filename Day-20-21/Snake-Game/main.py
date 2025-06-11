from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Set up class instances.
# Turtle is 20x20 pixels.
snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()

# Set up key bindings.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop.
game_is_on  = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.display_score()
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# The range function can take 3 arguments to specify start, stop, increment amount.
# The stop is exclusive.
# The default value for increment is 1.
# You can move backwards through the list using -1.






screen.exitonclick()
