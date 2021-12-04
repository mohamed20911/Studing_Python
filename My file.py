import turtle
from random import randint
from time import sleep

# Creation og game board
wn = turtle.Screen()
wn.title("Snake Game G.K.C")
wn.setup(width=700, height=700)
wn.bgcolor('black')



# Snake's Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body
body_parts = []

# fruit object
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(80,50)
fruit.shapesize(0.6)

# score turtle object
writer = turtle.Turtle()
writer.speed(0)
writer.color('white')
writer.hideturtle()
writer.penup()
scores = [0, 0]

def move():
          if head.direction == "up":
                    head.setheading(90)
                    head.forward(10)
          if head.direction == "down":
                    head.setheading(270)
                    head.forward(10)
          if head.direction == "right":
                    head.setheading(0)
                    head.forward(10)
          if head.direction == "left":
                    head.setheading(180)
                    head.forward(10)

def go_up():
          if head.direction != "down":
                    head.direction = "up"

def go_down():
          if head.direction != "up":
                    head.direction = "down"

def go_right():
          if head.direction != "left":
                    head.direction = "right"

def go_left():
          if head.direction != "right":
                    head.direction = "left"

# Score function
def scoring():
          if head.distance(fruit) < 16:
                    writer.clear()
                    writer.score += 10
                    if writer.score > writer.high_score :
                              writer.high_score = writer.score
                              fruit.goto(randint(-290, 290), randint(-290, 290))


turtle.done()