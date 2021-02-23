from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid = 1, stretch_len = 5)
        self.setheading(90)
        self.color('white')
        self.penup()
        self.setpos(position) 

        
    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
    
    




