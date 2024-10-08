from turtle import Turtle
class Snake():
    def __init__(self):
        self.arr=[(0,0),(-20,0),(-40,0),(-60,0),(-80,0)]
        self.snake= []
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        for position in self.arr:
             self.add_segment(position)
    
    def extend(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self,position):
        snake_segment= Turtle(shape='square')
        snake_segment.color('white')
        snake_segment.pu()
        snake_segment.goto(position)
        self.snake.append(snake_segment)
    def move_up(self):
        if(self.head.heading()!=270):
            self.head.setheading(90)
        return
    def move_down(self):
        if(self.head.heading()!=90):
            self.head.setheading(270)
        return
    def move_left(self):
        if(self.head.heading()!=0):
            self.head.setheading(180)
        return
    def move_right(self):
        if(self.head.heading()!=180):
            self.head.setheading(0)
        return
    def move(self):
        for seg in range(len(self.snake)-1,0,-1):
                new_x= self.snake[seg-1].xcor()
                new_y= self.snake[seg-1].ycor()
                self.snake[seg].goto(new_x,new_y)
        self.head.forward(20)
    
    def tail_collision(self):
        for i in range(3,len(self.snake)):
            print(self.head.distance(self.snake[i]))
            if(self.head.distance(self.snake[i])<=20):
                return True
            