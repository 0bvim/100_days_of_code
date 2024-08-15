from turtle import Turtle

class Paddle(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.color("red")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(350, 0)

	def go_up(self):
		if self.ycor() == (600/2):
			return ;
		print(self.ycor())
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		if self.xcor() == (800/2):
			return ;
		print(self.xcor())
		new_x = self.xcor() - 20
		self.goto(new_x, self.ycor())
