from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_piece = Turtle(shape="square")
            new_piece.color('white')
            new_piece.penup()
            new_piece.goto(position)
            self.segments.append(new_piece)

    def move(self):
        for piece_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[piece_num - 1].xcor()
            new_y = self.segments[piece_num - 1].ycor()
            self.segments[piece_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
