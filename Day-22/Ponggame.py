from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, key= "Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key= "w")
screen.onkey(l_paddle.go_down, key="s")

game_on = True
while game_on:
    screen.update()
    ball.move()

    # collision with wall detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()

    # collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.xbounce()

    # Detect when r paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # Detect when l paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
