from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
from border import Border
import random
import time

screen= Screen()
screen.screensize(600,600)
screen.title("Snake Game.")
screen.bgcolor('black')
screen.tracer(0)

snake= Snake()
food= Food()
score_board= ScoreBoard()
border= Border()



screen.listen()
screen.onkey(snake.move_up,'w')
screen.onkey(snake.move_down,'s')
screen.onkey(snake.move_left,'a')
screen.onkey(snake.move_right,'d')


is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food)<=15):
        food.move()
        snake.extend()
        score_board.increase_score()
    #detect collision with a wall.
    if(snake.head.xcor()>=270 or snake.head.xcor()<=-250 or snake.head.ycor()>=270 or snake.head.ycor()<=-250):
        score_board.game_over()
        is_game_on=False
    for segment in snake.snake:
        if(segment==snake.head):
            pass
        elif snake.head.distance(segment)<10:
            score_board.game_over()
            is_game_on=False
    
screen.exitonclick()