from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('square')
        self.shapesize(stretch_len = 2)
        self.penup()
        self.color(random.choice(COLORS))

        sign = [-1,1][random.randrange(2)]
        self.goto(x=280,y = 250 * random.random() * sign)
        self.seth(180)

        self.speed = STARTING_MOVE_DISTANCE
    
    def move(self):

        self.forward(self.speed)


class CarManager():

    def __init__(self):
        
        self.speed = STARTING_MOVE_DISTANCE
        self.cars_on_screen = []
    

    def increase_speed(self):

        for car in self.cars_on_screen:
            car.speed += MOVE_INCREMENT
            
    
    
    def make_new_car(self):

        temp = random.randint(0,2)
    
        if temp == 0:

            if len(self.cars_on_screen) < 30:
                car = Car()
                self.cars_on_screen.append(car)
        
    def remove_off_screen_cars(self):

        for car in self.cars_on_screen:
            if car.xcor() < -330:
                self.cars_on_screen.remove(car)

    


         
            
    
        
