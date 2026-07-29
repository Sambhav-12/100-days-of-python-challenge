import random
import turtle
t = turtle.Turtle()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size):
    for _ in range(int(360/size)):
        t.circle(100)
        t.color(random_color())
        t.setheading(t.heading() + size)

t.speed("fastest")
draw_spirograph(10)

screen = turtle.Screen()
screen.exitonclick()