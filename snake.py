# imports
import turtle
import time
import random

delay = 0.1

# main screen
wn = turtle.Screen()
wn.title("Simple Snake Game by @jordanalexis6")
wn.bgcolor("#28113d")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# funtions
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() + 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


# main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)


wn.mainloop()
