import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.listen()

z = int(input("Please Enter the side length"))


class shapes:
    def square():
        for i in range(4):
            t.forward(z)
            t.left(90)
    def rectangle():
        for i in [200, 100, 200, 100]:
            t.forward(i)
            t.left(90)


wn.onkey(shapes.square, "s")
wn.onkey(shapes.rectangle, "r")
wn.onkey(t.clear, "space")