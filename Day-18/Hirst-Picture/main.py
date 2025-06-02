import colorgram
import turtle
import random

turtle.colormode(255)
my_screen = turtle.Screen()
my_screen.setup(600, 600)
my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(0)
my_turtle.penup()
my_turtle.goto(-225, -225)

# colors = colorgram.extract('Hirst-spot-painting.jpg', 49)

# This loop was used to extract the colors.
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_tuple = (r, g, b)
#     colors_extracted.append(rgb_tuple)

# We copied these colors extracted from the loop, then removed colors that were near-white.
colors_extracted = [
    (237, 221, 110), (19, 110, 193), (224, 61, 94), (226, 151, 89), (119, 153, 209), (216, 127, 162), (143, 89, 46),
    (33, 196, 118), (149, 179, 16), (103, 106, 195), (200, 13, 34), (233, 57, 46), (242, 154, 185), (113, 193, 149),
    (189, 48, 82), (17, 183, 210), (145, 225, 173), (34, 52, 118), (134, 217, 235), (234, 172, 157), (197, 214, 5),
    (33, 37, 80), (8, 156, 117), (172, 176, 227), (86, 30, 34), (83, 33, 31), (254, 4, 46), (202, 18, 14), (67, 74, 47)
]

def draw10_dots():
    for dot in range(10):
        my_turtle.dot(20, random.choice(colors_extracted))
        my_turtle.forward(50)

def draw_spot_picture():
    for double_rows in range(5):
        draw10_dots()
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(50)
        draw10_dots()
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(0)
        my_turtle.forward(50)

draw_spot_picture()

my_screen.exitonclick()
