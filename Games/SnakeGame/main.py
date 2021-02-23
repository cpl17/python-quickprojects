from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# TODO: Set Difficulty -> change sleep

# Set up screen

screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)




# Create a snake object

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Map direction movements to keys 

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# Start Game

game_is_on = True

while game_is_on:
    
    
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detect collision with wall

    if (abs(snake.head.xcor()) > 280) | (abs(snake.head.ycor()) > 280) :
        scoreboard.reset()
        snake.reset()
    
    # Detect collions with tail 

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 5:
            scoreboard.reset()
            snake.reset()

        

    
    
        



 



























screen.exitonclick()