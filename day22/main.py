from turtle import Screen
from paddle import Paddle

def screen_init():
	screen = Screen()
	screen.bgcolor("black")
	screen.setup(width=800, height=600)
	screen.title("Welcome to the Pongle")
	return screen

# initialize screen
screen = screen_init()

#put paddles
paddle = Paddle()

# listen events
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

screen.exitonclick()
