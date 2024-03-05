from turtle import Turtle, Screen
import random

is_race_on  = False
screen = Screen()
screen.setup(500,400)
user_bet= screen.textinput(title="Make your bet", prompt="Whcih turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtless = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtless.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtless:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("You lost")
        rand_distance = random.randint(0,19)
        turtle.forward(rand_distance)
screen.exitonclick()
