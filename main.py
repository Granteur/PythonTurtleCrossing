import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()
    
    #detect when car hits turtle stop game if that happens
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    #detect when turtle player has reached top edge of screen
    if player.finish_line():
        player.next_level()
        #increase score
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        #when this happens, move turtle back to bottom and increase the speed of cars
        car_manager.level_up()
        
    

screen.exitonclick()
