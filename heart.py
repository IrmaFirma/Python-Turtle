import turtle

wn = turtle.Screen()
wn.setup(width=400, height=400)
heart = turtle.Turtle()

def curve():
    for i in range(200):
        heart.right(1)
        heart.forward(1)

def draw_heart():
    heart.fillcolor("red")
    heart.begin_fill()
    heart.left(140)
    heart.forward(113)
    curve()
    heart.left(120)
    curve()
    heart.forward(112)
    heart.end_fill()

draw_heart()

heart.penup()
heart.goto(0,50)
heart.write("LOVE YOU", font=("Arial", 20, "bold"), align="center")
heart.ht()
turtle.done()
