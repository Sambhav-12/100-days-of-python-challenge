# triangle, square , pentagon , hexagon , heptagon , octagon , nonagon , decagon
import random
from turtle import Turtle

t = Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black"]

def draw_shape(n):
    angle = 360/n 
    for i in range(n):
        t.forward(100)
        t.right(angle)

for shape in range(3,11):
    t.color(random.choice(colors))
    draw_shape(shape)