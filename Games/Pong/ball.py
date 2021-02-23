from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.dx = 10
        self.dy = 10
        self.move_speed = .1
    
    def move(self):
        
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x,new_y)
    
    def bounce(self):

        self.dy *= -1
    
    def collision(self):

        self.dx *= -1
        self.move_speed *= .9
    
    def reset_position(self):

        self.dx *= -1
        self.move_speed = .1
        self.home()
    
    def increase_speed(self):

        self.dx *= 1.2 
        self.dy *= 1.2 





        
            
        


        
