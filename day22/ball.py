from turtle import Turtle

width_limit = 800
height_limit = 600

class Ball(Turtle):
	
	def __init__(self):
		super().__init__()
		self.color("white")
		self.shape("circle")
		self.penup()

	def move(self):
		new_x = self.xcor() + 10
		new_y = self.ycor() + 10
		self.goto(new_x, new_y)
