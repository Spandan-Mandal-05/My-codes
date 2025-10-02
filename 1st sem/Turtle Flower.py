import turtle as pen
import colorsys as cs
pen.setup(800,800)
pen.speed(0)
pen.tracer(30)
pen.width(2)
pen.bgcolor("black")


for j in range(25):
    for i in range(15):
        pen.color(cs.hsv_to_rgb( i/15 , j/25 , 1))
        pen.right(90)
        pen.circle(200-j*4,90)
        pen.left(90)
        pen.circle(200-j*4,90)
        pen.right(180)
        pen.circle(50,24)
pen.hideturtle()
pen.done()

