from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_pos = [-70, -40 , -10 , 20 , 50 , 80]
all_turtles = []

for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(x = -230, y = y_pos[turtle_index])
    all_turtles.append(t)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                turtle.write(f"You've won the race! {winning_color} is the winner",align="center", 
    font=("Courier", 24, "bold italic"))
                
            else:
                turtle.write(f"You've lost the race! {winning_color} is the winner",align="center", 
    font=("Courier", 24, "bold italic"))
                

        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()

