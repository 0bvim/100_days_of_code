from turtle import Screen
from paddle import Paddle

def screen_init():
	screen = Screen()
	screen.bgcolor("black")
	screen.setup(width=800, height=600)
	screen.title("Welcome to the Pongle")
	screen.tracer(0) # it is to turn off animation for creation of paddles
	return screen

def screen_listen(right_paddle, left_paddle):
	screen.listen()
	screen.onkey(right_paddle.go_up, "Up")
	screen.onkey(right_paddle.go_down, "Down")
	screen.onkey(left_paddle.go_up, "w")
	screen.onkey(left_paddle.go_down, "s")

# initialize screen
screen = screen_init()

#put paddles
left_paddle = Paddle("left")
right_paddle = Paddle("right")

# listen events
screen_listen(right_paddle, left_paddle)

game_is_on = True
while game_is_on:
	screen.update()

screen.exitonclick()
