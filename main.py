import turtle
import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput("make your bet", "Which turtle win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
y_index = [-150, -100, -50, 0, 50, 100, 150]
all_turtle = []
print(all_turtle)


for turtle_index in range(0, 7):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_index[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won")
            else:
                print(f"You lost. The winning color is {winning_color}.")
        random_dis = random.randint(0, 10)
        turtle.forward(random_dis)



# def forward():
#     tim.forward(100)
#
#
# screen.listen()
# screen.onkey(forward, "w")


screen.exitonclick()
