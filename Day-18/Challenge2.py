from turtle import Turtle, Screen

t = Turtle()
for _ in range(20):
    t.forward(20)
    t.penup()
    t.forward(20)
    t.pendown()

screen = Screen()
screen.exitonclick()