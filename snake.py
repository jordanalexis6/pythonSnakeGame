# imports
import turtle
import time
import random

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

# main game loop
while True:
    wn.update()


wn.mainloop()
