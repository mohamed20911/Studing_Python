import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("python house")

t.penup()
p = t.xcor()
t.setx(p - 340)
t.pendown()
wn.colormode(255)
t.color(142,255,255)
t.begin_fill()
for i in range(2):
    t.forward(678.1)
    t.left(90)
    t.forward(340)
    t.left(90)
t.end_fill()
k = turtle.Turtle()
k.pensize(3)
k.color(239,186,255)
k.pencolor("black")
k.speed(10)
k.penup()
p = k.xcor()
k.setx(p - 170)
k.pendown()
k.begin_fill()
for i in range(2):
    k.forward(250)
    k.left(90)
    k.forward(200)
    k.left(90)
k.pencolor("black")
k.end_fill()
k.left(90)
k.forward(200)
k.color(0,184,255)
k.begin_fill()
k.right(50)
k.forward(160)
k.right(78.5)
k.forward(162)
k.end_fill()
k.right(50)
k.forward(70)
k.right(90)
k.penup()
k.forward(50)
k.pendown()
k.color("white")
k.pensize(3)
k.begin_fill()
k.pencolor("black")
for o in range(4):
    k.forward(25)
    k.right(90)
k.end_fill()
k.penup()
k.forward(100)
k.pendown()
k.begin_fill()
for o in range(4):
    k.forward(25)
    k.right(90)
k.end_fill()
k.penup()
k.forward(50)
k.pendown()
k.begin_fill()
for o in range(4):
    k.forward(25)
    k.right(90)
k.end_fill()
k.left(90)
k.penup()
k.forward(50)
k.left(90)
k.pendown()
k.begin_fill()
for o in range(4):
    k.forward(25)
    k.right(90)
k.end_fill()
m = turtle.Turtle()
m.color(142,255,255)
m.pencolor("black")
m.begin_fill()
m.left(90)
m.forward(50)
m.right(90)
m.forward(50)
m.right(90)
m.forward(50)
m.end_fill()
l = turtle.Turtle()
l.forward(25)
l.left(90)
l.forward(50)