import turtle as tur
import colorsys as cs
tur.bgcolor("black")
#tur.tracer(5)
tur.setup(800,800)
tur.speed(0)

j=0
for i in range(60):
    tur.color(cs.hsv_to_rgb(j/30,i/60,1))
    tur.forward(100)
    tur.left(60)
    tur.forward(100)
    tur.right(120)
    tur.circle(50)
    tur.left(240)
    tur.forward(100)
    tur.left(60)
    tur.forward(200)
    tur.right(60)
    tur.forward(100)
    tur.left(120)
    tur.circle(-50)
    tur.right(240)
    tur.forward(100)
    tur.right(60)
    tur.forward(100)
    tur.right(5)
    j+=0.5
tur.hideturtle()
tur.done()
                            

