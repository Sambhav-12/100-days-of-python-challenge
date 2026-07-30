from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def turn_right():
    t.right(10)
def turn_left():
    t.left(10)
def clear():
    t.reset()

screen.listen()
screen.onkey(key="c", fun =clear)
screen.onkey(key="w", fun =move_forwards)
screen.onkey(key="s", fun =move_backwards)
screen.onkey(key="a", fun =turn_left)
screen.onkey(key="d", fun =turn_right)
screen.mainloop()