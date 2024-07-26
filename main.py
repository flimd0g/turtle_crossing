import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_count = 0
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    car_count += 1
    time.sleep(0.1)
    screen.update()
    if car_count % 6 == 0:
        car_manager.create_car()
    car_manager.move()

    if player.ycor() > 300:
        player.reset()
        car_manager.level_up()
        score.level_up()

    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            score.game_over()
            screen.exitonclick()


