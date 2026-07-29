# Random Walk
import random
from turtle import Turtle, Screen

t = Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black"]
directions = [0, 90, 180, 270]
size = [1, 2, 3, 4, 5, 6, 7, 8, 9]
speed = ["fastest", "fast", "slow", "slowest", "normal"]

for _ in range(400):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))
    t.pensize(random.choice(size))
    t.speed(random.choice(speed))

screen = t.Screen()
screen.exitonclick()