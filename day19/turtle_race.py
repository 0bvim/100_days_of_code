from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "black"] 
y_pos = [-70, -40,-10, 20, 50, 80]
all_turtles = []

for turtle_idx in range(0,6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(colors[turtle_idx])
	new_turtle.goto(x=-230, y=y_pos[turtle_idx])
	all_turtles.append(new_turtle)

if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 230:
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You've won! The {winning_color} turtle is the winner!")
			else:
				print(f"You've lost! The {winning_color} turtle is the winner!")
			is_race_on = False;
		random_dist = random.randint(0, 10)
		turtle.forward(random_dist)
	 

screen.exitonclick()
