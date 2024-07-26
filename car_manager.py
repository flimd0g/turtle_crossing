from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
possible_values = list(range(-250, 281, 5))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager():
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []


    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def create_car(self):
        self.new_car = Turtle("square")
        self.new_car.color(random.choice(COLORS))
        self.new_car.penup()
        self.new_car.shapesize(1, 2)
        self.new_car.goto(x=290, y=random.choice(possible_values))
        self.all_cars.append(self.new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        def reset(self):
            for car in self.all_cars:
                car.hideturtle()
            self.all_cars.clear()
            self.car_speed = STARTING_MOVE_DISTANCE
