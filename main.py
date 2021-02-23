from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (red/orange/yellow/green/blue/purple) ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    y_pos = (-100 + index * 50)
    new_turtle.goto(x=-230, y=y_pos)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                print(f"You won!!! {turtle.pencolor()} is the winner !!!")
            else:
                print(f"You lose. {turtle.pencolor()} is the winner !!!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()