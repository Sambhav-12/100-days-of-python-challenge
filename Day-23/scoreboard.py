from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.update_level()

    def update_level(self):
        self.write(f"level: {self.level}", align = "left" , font = FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align = "center" , font = FONT)
