import turtle as t
from turtle import Screen
import random
t.colormode(255)

list_of_colors = [(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205), (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)]
tim=t.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
tim.speed("fastest")
for count_dots in range(1, num_of_dots+1):
    tim.dot(20, random.choice(list_of_colors))
    tim.forward(50)
    if count_dots%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()