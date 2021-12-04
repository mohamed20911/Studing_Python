import turtle

t = turtle.Turtle()
scr = turtle.Screen()
scr.listen()

def square():
    for i in range(4):
        t.forward(200)
        t.left(90)

def rectangle():
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(125)
        t.left(90)

def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)

def shapes():
    for i in range(8):
        t.forward(100)
        t.left(45)

def star():
    for i in range(6):
        t.left(70)
        t.forward(10)
        t.right(130)
        t.forward(10)

scr.onkey(square, "s")
scr.onkey(rectangle, "r")
scr.onkey(triangle, "t")
scr.onkey(shapes, "p")
scr.onkey(t.clear, "space")
scr.onkey(star, "a")