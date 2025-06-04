from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet. Rainbow colors.",
                            prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
position1_x, position1_y = -230, 80
is_race_on = False
all_turtles = []

# My inefficient first attempt.
# class TurtleRacer:
#     def __init__(self, color, start_x, start_y):
#         self.turtle = Turtle()
#         self.turtle.penup()
#         self.turtle.color(color)
#         self.turtle.shape("turtle")
#         self.turtle.goto(start_x, start_y)
#
# red_turtle = TurtleRacer("red", position1_x, position1_y)
# orange_turtle = TurtleRacer("orange",  position1_x, position1_y -30)
# yellow_turtle = TurtleRacer("yellow", position1_x, position1_y -60)
# green_turtle = TurtleRacer("green", position1_x, position1_y -90)
# blue_turtle = TurtleRacer("blue", position1_x, position1_y -120)
# indigo_turtle = TurtleRacer("indigo", position1_x, position1_y -150)
# violet_turtle = TurtleRacer("violet", position1_x, position1_y -180)

# After teacher help.
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(position1_x, position1_y - (turtle_index * 30))
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Intro warmup.
# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# tim.goto(x=-230, y=180)

#screen.listen()

# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def reset():
#     tim.clear()
#     tim.hideturtle()
#     tim.penup()
#     tim.home()
#     tim.showturtle()
#     tim.pendown()
#
# # When you pass a function as an argument, you leave out the parenthesis.
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=reset)

screen.exitonclick()
