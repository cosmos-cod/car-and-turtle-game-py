import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()
car =  CarManager()
score = Scoreboard()

screen.onkey(turtle.move_up , "w")
print(car.added_cars)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
#detect the collision
    for _ in car.added_cars:
        if _.distance(turtle) < 20:
            game_is_on = False

    if turtle.finishing_line():
        turtle.go_to_start()
        car.increase_speed_of_cars()
        score.level_up()

screen.exitonclick()
