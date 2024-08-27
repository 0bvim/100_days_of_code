from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.penup()
        self.goto(-290, 250)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def updated_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
