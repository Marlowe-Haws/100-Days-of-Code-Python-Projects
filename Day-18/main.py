# This was the practice section of the project.

from turtle import Turtle, Screen
from random import random, choice

#turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("navy")
tim.speed(0)
tim.pensize(2)

# Way to generate random color with default rgb values.
def random_color():
    r = random()
    g = random()
    b = random()
    return r, g, b

# Way to generate random color using 255 color mode
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return r, g, b

def draw_shape(sides):
    angle = 360/sides
    for side in range(sides):
        tim.forward(100)
        tim.lt(angle)

def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.pu()
        tim.forward(10)
        tim.pd()

def draw_shapes_in_range(least_sides_shape, most_sides_shape):
    for shape in range(least_sides_shape, most_sides_shape):
        tim.color(random_color())
        draw_shape(shape)

def random_walk(steps):
    directions = [0, 90, 180, 270]
    for step in range(steps):
        tim.color(random_color())
        tim.setheading(choice(directions))
        tim.forward(30)

def draw_spirograph(circle_radius, turn_angle):
    num_turns = int(360/turn_angle)
    for circle in range(num_turns):
        tim.color(random_color())
        tim.circle(circle_radius)
        tim.rt(turn_angle)

draw_spirograph(100, 5)

screen = Screen()
screen.exitonclick()
