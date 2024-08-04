from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "black"] 
y_pos = [-70, -40,-10, 20, 50, 80]

for turtle_idx in range(0,6):
	tim = Turtle(shape="turtle")
	tim.penup()
	tim.color(colors[turtle_idx])
	tim.goto(x=-230, y=y_pos[turtle_idx])


screen.exitonclick()
