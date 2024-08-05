from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("do you see the snake getting in?")
screen.tracer(0)
snake_pieces = []
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
	new_piece = Turtle(shape="square")
	new_piece.penup()
	new_piece.color('white')
	new_piece.goto(position)
	snake_pieces.append(new_piece)

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)
	for piece in snake_pieces:
		piece.forward(20)

screen.exitonclick()
