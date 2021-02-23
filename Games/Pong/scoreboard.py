from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.lscore} | {self.rscore}", align = ALIGNMENT, font = FONT )

    def increase_lscore(self):
        self.lscore += 1
        self.clear()
        self.update_scoreboard()
    
    def increase_rscore(self):
        self.rscore += 1
        self.clear()
        self.update_scoreboard()