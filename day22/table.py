from turtle import Turtle

class Table(Turtle):

	def __init__(self):
		super().__init__()
		self.speed(0)
		self.penup()
		self.goto(-400, -300)
		self.color("cyan")
		self.pendown()
		self.hideturtle()

	def drawn_square(self, wid, height):
		"""
		Draw a square with the specified width and height.
		
		:param width: Width of the square
		:param height: Height of the square
		"""
		for _ in range(2):  # Two sides of the square
			self.forward(wid)
			self.left(90)  # Turn left 90 degrees
			self.forward(height)
			self.left(90)
