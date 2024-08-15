from turtle import Screen

def screen_init():
	screen = Screen()
	screen.bgcolor("black")
	screen.setup(width=800, height=600)
	screen.title("Welcome to the Pongle")
	return screen

screen = screen_init()
screen.exitonclick()
