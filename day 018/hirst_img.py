# import colorgram
# 
# img_colors = []
# colors = colorgram.extract('/home/ajay/Public/projects/100 days of coding/day 018/img.jpg', 24)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     img_colors.append(new_color)

# print(img_colors)

from turtle import Turtle,Screen
from random import choice

colors_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54)]


t = Turtle()
t.hideturtle()
t.shape('classic')
t.pensize(10)
t.speed(0)

s = Screen()
s.colormode(255)

t.penup()
t.backward(225)
t.right(90)
t.forward(215)
t.right(-90)
t.pendown()

for i in range(10):
    for j in range(10):
        t.dot(20,choice(colors_list))
        t.penup()
        t.forward(50)
        t.pendown()
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.backward(500)
    t.pendown()


s.exitonclick()