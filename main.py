import random

import colorgram
import turtle as t

colors = colorgram.extract('picture.jpeg',30)
t.colormode(255)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r,g,b)
    print(color.rgb)
    rgb_colors.append(new_color)


tim = t.Turtle()
tim.hideturtle()
tim.shape("turtle")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()

