"""
Snake Game by Keerthana
Classic Snake game using Python Turtle graphics.
"""

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Keerthana")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-290, 290)
border.pendown()
for _ in range(4):
    border.forward(580)
    border.right(90)
border.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Control functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x, y = head.xcor(), head.ycor()
    if head.direction == "up":
        head.sety(y + 20)
    elif head.direction == "down":
        head.sety(y - 20)
    elif head.direction == "left":
        head.setx(x - 20)
    elif head.direction == "right":
        head.setx(x + 20)

def restart_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 0.1
    update_scoreboard()

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Keyboard bindings (Arrow keys only)
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(restart_game, "r")

# Main game loop
while True:
    wn.update()

    if abs(head.xcor()) > 280 or abs(head.ycor()) > 280:
        restart_game()

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)
        delay = max(0.05, delay - 0.001)
        score += 10
        if score > high_score:
            high_score = score
        update_scoreboard()

    for index in range(len(segments)-1, 0, -1):
        x, y = segments[index-1].xcor(), segments[index-1].ycor()
        segments[index].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            restart_game()

    time.sleep(delay)

wn.mainloop()

