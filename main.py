# Made by Piotr Zięba on 07.11.2023.
# It creates a dot art. 

import turtle as t
import random
# import colorgram    # imports the module
# rgb_colors = []    # creates a list
# colors = colorgram.extract('image.jpg', 25)    # extracts colors from the picture
# for color in colors:    # Makes a for loop to select rgb colors from colors
#    r = color.rgb.r    # Takes red
#    g = color.rgb.g    # takes green
#    b = color.rgb.b    # takes blue
#    new_color = (r, g, b)    # Creates a tuple
#    rgb_colors.append(new_color)    # adds it to the rgb_colors

# Code above extracted tuples from the list bellow. These are colors from the picture. I removed those too bright.
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]


tim = t.Turtle()    # We create a turtle
tim.speed("fastest")    # It gets proper speed
screen = t.Screen()    # Gets hold of the screen
screen.colormode(255)    # Allows us to use RGB
screen.setup(width=500, height=520, startx=400, starty=100)    # Sets the h and w of the screen and places it in the c.


def random_color(my_list):
    """Selects random color from color_list"""
    return random.choice(my_list)


tim.up()    # Prevents tim from drawing.
tim.setheading(225)    # Turns the turtle to the corner.
tim.forward(300)    # Goes to the place I want turtle to start drawing.
tim.left(135)    # Turns left to draw a straight line.

for _ in range(10):    # Makes the turtle to go for 10 rows.
    for _ in range(10):    # Creates 10 dots with random colors from color_list.
        tim.dot(30, random_color(color_list))    # Tim makes dots.
        tim.forward(45)    # Moves 45 ahead.
    tim.setheading(90)    # Turns
    tim.forward(50)    # Goes forwards
    tim.setheading(180)
    tim.forward(450)
    tim.setheading(0)

screen.exitonclick()    # Allows me to exit the screen on click
