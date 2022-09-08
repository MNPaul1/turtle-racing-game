from msilib.schema import Font
from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-280,260)
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "Left", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = FONT)