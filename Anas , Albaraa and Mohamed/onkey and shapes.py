import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.listen()


def Square():
    for i in range(4):
        t.forward(100)
        t.left(90)

def rectangle():
    for i in [200, 50, 200, 50]:
        t.forward(i)
        t.left(90)

def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)

def pentagon():
    for i in range(6):
        t.forward(100)
        t.left(60)

def circle():
    t.circle(75)

def up():
    t.setheading(90)
    t.forward(30)
def down():
    t.setheading(-90)
    t.forward(30)
def right():
    t.setheading(0)
    t.forward(30)
def left():
    t.setheading(180)
    t.forward(30)

# onkey Shapes
wn.onkey(Square, "s")
wn.onkey(rectangle, "r")
wn.onkey(triangle, "t")
wn.onkey(pentagon, "p")
wn.onkey(circle, "c")
wn.onkey(t.clear, "space")
wn.onkey(t.undo, "u")

# onkey
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(right, "Right")
wn.onkey(left, "Left")