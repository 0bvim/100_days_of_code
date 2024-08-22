from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):

    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
