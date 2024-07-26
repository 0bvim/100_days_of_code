#this module introduce oop with python lib 'turtle'
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "brown")
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()
print(my_screen.canvheight)
