from turtle import Turtle
import time

FONT = ("Courier", 16, "normal")
ALIGNMENT = 'left'

class Scoreboard(Turtle):

    def __init__(self):
            super().__init__()
            self.level = 1
            self.color('black')
            self.hideturtle()
            self.penup()
            self.goto(-260,260)
            self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level} ", align = ALIGNMENT, font = FONT )

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over", align = 'center', font = FONT )
    
    def reset(self):
        self.level = 1 
        self.update_scoreboard()
        self.game_over()

        time.sleep(1)
        
        self.clear()


