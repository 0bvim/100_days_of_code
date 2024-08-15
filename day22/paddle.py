from turtle import Turtle

left = -350
right = 350

class Paddle(Turtle):
	
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("red")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(self._check_side(position))

	def _check_side(self, position):
		if position == "left":
			return (-350, 0)
		elif position == "right":
			return (350, 0)
		else:
			raise ValueError("Positio must be 'right' or 'left'")

	def go_up(self):
		if self.ycor() == (600/2):
			return ;
		print(self.ycor())
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		if self.ycor() == (600/2) * -1:
			return ;
		print(self.ycor())
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)
