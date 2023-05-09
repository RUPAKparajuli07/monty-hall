import random
import turtle

# Create a Turtle graphics window
window = turtle.Screen()
window.title("Monty Hall Simulator")
window.bgcolor("white")

# Create a Turtle graphics pen for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Define the fifteen doors and randomly place the car behind one of them
doors = [0] * 15
car_index = random.randint(0, 14)
doors[car_index] = 1

# Draw the doors on the screen
for i in range(15):
    x = -200 + (i % 5) * 100
    y = 200 - (i // 5) * 100
    pen.setpos(x, y)
    pen.pendown()
    pen.setheading(0)
    pen.forward(80)
    pen.right(90)
    pen.forward(120)
    pen.right(90)
    pen.forward(80)
    pen.right(90)
    pen.forward(120)
    pen.penup()
    pen.setpos(x + 40, y - 80)
    pen.write(str(i), align="center", font=("Arial", 12, "normal"))

# Let the player choose a door
player_choice = int(window.textinput("Monty Hall Simulator", "Choose a door (0-14): "))

# Show the doors that Monty opens, which are the ones that the player didn't choose and don't have the car behind them
monty_choices = [i for i in range(15) if i != player_choice and doors[i] == 0]
monty_choices = random.sample(monty_choices, min(12, len(monty_choices)))
for i in monty_choices:
    x = -200 + (i % 5) * 100
    y = 200 - (i // 5) * 100
    pen.setpos(x + 20, y - 60)
    pen.write("X", align="center", font=("Arial", 24, "normal"))
    pen.setpos(x + 50, y - 60)
    pen.write("!", align="center", font=("Arial", 24, "normal"))

# Let the player decide whether to switch doors or stick with their original choice
switch = window.textinput("Monty Hall Simulator", "Do you want to switch doors? (y/n): ")
if switch == "y":
    player_choices = [i for i in range(15) if i != player_choice and i not in monty_choices]
    player_choice = random.choice(player_choices)

# Determine if the player won or lost
if doors[player_choice] == 1:
    pen.setpos(0, 0)
    pen.write("Congratulations, you won!", align="center", font=("Arial", 24, "normal"))
else:
    pen.setpos(0, 0)
    pen.write("Sorry, you lost.", align="center", font=("Arial", 24, "normal"))
    window.tracer(0)
    for i in range(5):
        window.bgcolor("red")
        window.update()
        window.bgcolor("red")
        window.update()
    window.tracer(1)

# Wait for the user to close the window
window.mainloop()