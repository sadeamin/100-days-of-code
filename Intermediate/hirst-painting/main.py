import colorgram

# rgb_colors = []
# colors = colorgram.extract("Capture.PNG", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
color_list = [(194, 166, 117), (142, 91, 54), (180, 154, 37), (216, 203, 126), (141, 31, 6), (79, 41, 28), (59, 89, 124), (212, 218, 224), (131, 156, 176), (149, 178, 147), (56, 119, 91), (12, 93, 62), (36, 63, 75), (226, 179, 170), (152, 135, 147), (232, 228, 229), (176, 108, 89), (34, 66, 96), (179, 201, 174), (16, 72, 71), (32, 82, 85), (99, 144, 128), (111, 127, 147), (186, 191, 204), (69, 64, 55), (124, 123, 124), (113, 138, 139), (200, 188, 191)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots = 100

for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()