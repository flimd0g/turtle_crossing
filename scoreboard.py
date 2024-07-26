from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.penup()
        self.goto(x=-280, y=240)
        self.write(f"Level {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-110,0)
        self.write(f"Game over. Score: {self.level}", font=FONT)
