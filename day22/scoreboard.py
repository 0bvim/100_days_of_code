from turtle import Turtle
import time

WIN = 1
MESSAGE = " point!"

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.left_score = 0
		self.right_score = 0
		self.winner = "none"
		self.write_score()

	def increase_score(self, side):
		if side == "left":
			self.left_score += 1
		elif side == "right":
			self.right_score += 1
		self.write_score()
	
	def write_score(self):
			self.clear()
			self.goto(-100, 188)
			self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
			self.goto(100, 188)
			self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
			self.check_winner()
	
	def check_winner(self):
		if self.left_score == WIN:
			self.winner = "left"
		elif self.right_score == WIN:
			self.winner = "right"
		if self.winner != "none":
			self.goto(0, 180)
			self.write(self.winner + MESSAGE, align="center", font=("Arial", 25, "normal"))
