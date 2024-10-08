from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(0.5,0.5)
        self.color('yellow')
        self.speed(0)
        self.move()
    def move(self):
        random_x= random.randint(-250,250)
        random_y= random.randint(-250,250)
        self.goto(random_x,random_y)