import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color\n(red/ orange/ yellow/ green/ blue/ purple): ",
)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_number in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_number])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[turtle_number])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!. The winner is {winning_color} turtle")
            else:
                print(f"You lost! The winner is {winning_color} turtle")


screen.exitonclick()
