import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
num_of_turtles = random.randrange(1 ,30)



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.added_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_cars(self):
        car_range = random.randint(1 ,3)
        if car_range == 1 :

            random_y_position = random.randrange(-300, 250)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1 ,stretch_len=2)
            new_car.penup()
            new_car.goto(x=260 , y=random_y_position)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.added_cars.append(new_car)

    def move_cars(self):
        for car in self.added_cars :
            car.forward(self.car_speed)
    def increase_speed_of_cars(self):

        self.car_speed += 5


