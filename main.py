from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.new_score()

    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 290 or snake.head.ycor()<-290:
        game_on = False
        score.game_over()

    for snake_segments in snake.new_snake[1:]:

        if snake.head.distance (snake_segments) < 10:
            game_on = False
            score.game_over()







































screen.exitonclick()