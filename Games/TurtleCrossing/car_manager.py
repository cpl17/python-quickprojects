from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self,speed):
        super().__init__()

        self.shape('square')
        self.shapesize(stretch_len = 2)
        self.penup()
        self.color(random.choice(COLORS))

        sign = [-1,1][random.randrange(2)]
        self.goto(x=280,y = 250 * random.random() * sign)
        self.seth(180)

        self.speed = speed
    
    def move(self):

        self.forward(self.speed)


class CarManager():

    def __init__(self):
        
        self.speed = STARTING_MOVE_DISTANCE
        self.cars_on_screen = []
           
    # Creation and removal of cars 

    def make_new_car(self):

        temp = random.randint(0,7)
    
        if temp == 0:

            car = Car(self.speed)
            self.cars_on_screen.append(car)
        
    def remove_off_screen_cars(self):

        for car in self.cars_on_screen:
            if car.xcor() < -330:
                self.cars_on_screen.remove(car)
    
    def remove_all_cars(self):
        for car in self.cars_on_screen:
            car.hideturtle()
            car.goto(-300,car.ycor())
    

    # Speed Methods 

    def increase_speed(self):

        #Increase speed for on screen 

        for car in self.cars_on_screen:
            car.speed += MOVE_INCREMENT
        
        #Increase speed for all future cars

        self.speed += MOVE_INCREMENT
    
    
    def reset_speed(self):

        self.speed = STARTING_MOVE_DISTANCE
    

    # Reset Game 

    def reset(self):
        self.reset_speed()
        self.remove_all_cars()


    
    @staticmethod
    def collision(car,player):

        #Side Collision
        if (abs(car.xcor() - player.xcor())) <25 & (abs(car.ycor() - player.ycor()) <20):
            return True
           
        #Top Colliosn
        if (abs(car.ycor() - player.ycor()) <20) & (abs(car.xcor() - player.xcor()) <40):
            return True
            


    


         
            
    
        
