from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.segment[0].xcor()>280 or snake.segment[0].xcor()<-280 or snake.segment[0].ycor()>290 or snake.segment[0].ycor()<-290:
        score.game_over()
        game_is_on = False

    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()