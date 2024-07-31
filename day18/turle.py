from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)
# timmy2 = Turtle()
# timmy2.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def square():
	for _ in range(4):
		timmy.forward(100)
		timmy.right(90)

def steps():
	for _ in range(10):
		timmy.forward(10)
		timmy.penup()
		timmy.forward(10)
		timmy.pendown()

def draw_shape(num_sides, turt, side):
	for _ in range(num_sides):
		angle = 360 / num_sides
		turt.forward(100)
		if side == "left":
			turt.left(angle)
		elif side == "right":
			turt.right(angle)

def turn_print(times):
	for _ in range(times):
		for i in range(3, 11):
			timmy.color(random.choice(colours))
			timmy.speed(0)
			draw_shape(i, timmy, "left")

		for i in range(3, 11):
			timmy2.color(random.choice(colours))
			timmy2.speed(0)
			draw_shape(i, timmy2, "right")
		timmy.left(90)
		timmy2.right(90)

def draw_spirograph(size_of_gap):
	for _ in range(int(360/size_of_gap)):
		timmy.color(random.choice(colours))
		timmy.dot(100)
		timmy.setheading(timmy.heading() + size_of_gap)

screen = Screen()
screen.exitonclick()
