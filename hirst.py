import colorgram
import random
from turtle import Turtle,Screen

screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)


colors = colorgram.extract('imagenow.jpeg', 15)
rgb_list = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    rgb_list.append([r, g, b])


def hirst(turt,len):
    for _ in range(1,len+1):
        for _ in range (1,len+1):
            turt.color(random.choice(rgb_list))
            turt.dot(disc_size)
            turt.forward(40)
        turt.backward(40*len-1)
        turt.left(90)
        turt.forward(40)
        turt.right(90)



felx = Turtle()
felx.shape("blank")
disc_size = 20
felx.penup()
felx.goto(-100,-100)
felx.speed(0)

hirst(felx,10)


screen.exitonclick()