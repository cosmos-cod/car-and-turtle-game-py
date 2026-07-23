from turtle   import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-275,275)
        self.color("black")
        self.write(f"current lvl = {self.level} ", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"current lvl = {self.level} ", align="left", font=FONT)

