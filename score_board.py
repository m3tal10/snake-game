from turtle import Turtle
FONT= ('courier', 14, 'normal')

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(0,240)
        self.score=0
        self.write(f'Score: {self.score}', move=False, align='center', font=FONT)
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f'Score: {self.score} ', move=False, align='center', font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write('GAME OVER', move=False, align='center', font=FONT)