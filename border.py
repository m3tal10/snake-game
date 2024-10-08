from turtle import Turtle

class Border(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('red')
        self.pu()
        self.goto(-250,-250)
        self.pd()
        for i in range(1,5):
            self.forward(520)
            self.setheading(90*i)
