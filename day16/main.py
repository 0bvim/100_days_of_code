#this module introduce oop with python lib 'turtle'
from prettytable import PrettyTable
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "brown")
# timmy.forward(100)

# for steps in range(100):
# 	for c in ('blue', 'red', 'green'):
# 		timmy.color(c)
# 		timmy.forward(steps)
# 		timmy.right(30)

# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

x = PrettyTable() 
x.add_column("City name", ["Name", "Phone", "Last Name"])

print(x)
