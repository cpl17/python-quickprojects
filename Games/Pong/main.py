from turtle import Screen,Turtle
from time import sleep

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard




#Set up screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title('Pong')
screen.tracer(0)





r_pad = Paddle((350,0))
l_pad = Paddle((-350,0))


screen.listen()

# Right paddle
screen.onkey(r_pad.up,"Up")
screen.onkey(r_pad.down,"Down")

# Left paddle

screen.onkey(l_pad.up,"w")
screen.onkey(l_pad.down,"s")


# Create ball 

ball = Ball()

# Create scoreboard 

score = ScoreBoard()


game_is_on = True

while game_is_on:
    

    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall

    if abs(ball.ycor()) > 280:
        ball.bounce()

    # Detect collision with paddle 

    if ((ball.distance(r_pad) < 50) | (ball.distance(l_pad) < 50)) & (abs(ball.xcor())>320):
        ball.collision()

    # Detect Right miss
    
    if ball.xcor() > 350:
        
        
        ball.reset_position()
        score.increase_lscore()
        screen.update()
        
    
    # Detect Left miss

    if ball.xcor() < -350:
    
        ball.reset_position()
        score.increase_rscore()
        screen.update()
       
        

    


    
    



screen.exitonclick()