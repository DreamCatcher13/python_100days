from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
my_screen = Screen()
my_screen.colormode(255)
timmy.speed("fast")

# colors_obj = colorgram.extract("image.jpg", 30)
# colors = []
# for _ in colors_obj:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     colors.append((r,g,b))

# print (colors)

my_colors = [(227, 235, 243), (247, 230, 238), (124, 180, 210), (234, 243, 23), (198, 174, 16), (29, 119, 167),
 (176, 14, 45), (235, 150, 76), (236, 204, 90), (217, 124, 163), (26, 144, 74), (215, 80, 123), (9, 171, 210),
 (212, 61, 27), (237, 77, 45), (245, 157, 187), (64, 21, 53), (12, 183, 150), (13, 31, 75), (161, 57, 106), 
 (76, 27, 22), (129, 209, 233), (161, 192, 164), (15, 48, 132), (102, 116, 181), (250, 159, 152), 
 (168, 24, 19), (121, 216, 209), (3, 88, 57)]

timmy.hideturtle()
timmy.penup()
timmy.setposition(-200, -200)
y = -200
for i in range(10):
    for i in range(10):
        timmy.dot(20, random.choice(my_colors))
        timmy.forward(30)
    y += 30
    timmy.setposition(-200, y )




my_screen.exitonclick()