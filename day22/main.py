from turtle import Screen
from table import Table
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

WIN = 1

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

def check_bounce(right, left, ball):
	if ball.distance(right) < 50 and ball.xcor() > 320 or \
		ball.distance(left) < 50 and ball.xcor() > -320:
		ball.bounce_x()

def check_missing(ball, scoreboard):
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.increase_score("left")
	elif ball.xcor() > 380:
		ball.reset_position()
		scoreboard.increase_score("right")

# initialize screen
screen = screen_init()

# create paddles
left_paddle = Paddle("left")
right_paddle = Paddle("right")

# create ball, scoreboard and table
ball = Ball()
scoreboard = Scoreboard()
table = Table()
table.drawn_square(800, 600)

# listen events
screen_listen(right_paddle, left_paddle)

game_is_on = True
while game_is_on:
	table.drawn_square(800, 600)
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()
	
	# collision with paddles
	check_bounce(right_paddle, left_paddle, ball)

	# detect paddles misses
	check_missing(ball, scoreboard)

screen.exitonclick()
