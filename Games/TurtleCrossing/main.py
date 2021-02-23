import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True


create_new_car = False
while game_is_on:
    
    time.sleep(0.1)
    screen.update()

    # Create cars and make them move 
    
    manager.make_new_car()

    for car in manager.cars_on_screen:
        car.move()
       
    # Remove off screen cars 

    manager.remove_off_screen_cars()

    # Detect collision 

    for car in manager.cars_on_screen:

        if manager.collision(car,player):
            player.reset()
            manager.reset()
            scoreboard.reset()
            scoreboard = Scoreboard()

    # Detect making it across 

    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_score()
        manager.increase_speed()
        



screen.exitonclick()
