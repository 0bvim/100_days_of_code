from turtle import Screen
from scoreboard import Scoreboard
from food import Food
import time
from snake import Snake

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("do you see the snake getting in?")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_is_on = False    
        scoreboard.game_over()


screen.exitonclick()

