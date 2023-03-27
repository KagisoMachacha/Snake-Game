#Kagiso Machacha

import turtle
import time
import random

delay = 0.1
score = 0 
 
# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Xenzia")
wn.bgcolor("lightgreen")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)
 
# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
# food in the game
food = turtle.Turtle()
colors = random.choice('red')
shapes = random.choice('square')
food.speed(5)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
 
pen = turtle.Turtle()
pen.speed(5)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0", align="center",
          font=("candara", 24, "bold"))
 
 
# assigning key directions
def goNorth():
    if head.direction != "south":
        head.direction = "north" 
 
 
def goSouth():
    if head.direction != "north": 
        head.direction = "south" 
 
 
def goWest():
    if head.direction != "east": 
        head.direction = "west" 
 
 
def goEast():
    if head.direction != "west": 
        head.direction = "east" 
 
 
def move():
    if head.direction == "north": 
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "south":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "west":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "east":
        x = head.xcor()
        head.setx(x+20)
 
 
wn.listen()
wn.onkeypress(goNorth, "w")
wn.onkeypress(goSouth, "s")
wn.onkeypress(goWest, "a")
wn.onkeypress(goEast, "d")
 
 