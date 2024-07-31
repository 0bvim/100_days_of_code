from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def mov_forwards():
	tim.forward(10)

def mov_back():
	tim.backward(10)

def mov_left():
	new_heading = tim.heading() - 10
	tim.setheading(new_heading)

def mov_right():
	new_heading = tim.heading() + 10
	tim.setheading(new_heading)

def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()


def moves(key, func):
	keys = ["w", "W", "A", "a", "S", "s", "d", "D"]
	if key in keys:
		screen.onkey(key, fun)

screen.listen()
screen.onkey(key="w", fun=mov_forwards)
screen.onkey(key="s", fun=mov_back)
screen.onkey(key="a", fun=mov_left)
screen.onkey(key="d", fun=mov_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
