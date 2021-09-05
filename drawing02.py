import turtle
import time

turtle.setup(1100,590)
turtle.colormode(255)
turtle.bgcolor(0,0,51)
turtle.pencolor(255,255,255)
turtle.pensize(0)

def tree(length=300):
    
    if length <= 15:
        turtle.fd(length)
        turtle.bk(length)
        return

    turtle.fd(length*3/8)

    turtle.rt(30)
    tree(length * 2/3)
    turtle.lt(30)

    turtle.fd(length/4)

    turtle.lt(35)
    tree(length * 3/4)
    turtle.rt(35)

    turtle.fd(length/8)

    turtle.rt(25)
    tree(length/2)
    turtle.lt(25)

    turtle.fd(length/4)

    turtle.bk(length)

time.sleep(20)
turtle.lt(90)
turtle.speed(0)
turtle.up()
turtle.setpos(-100,-260)
turtle.down()
tree()
turtle.speed(4)

turtle.rt(90)
turtle.fd(300)
turtle.color(255,255,255)
turtle.write('月と鼈',False,'left',font = ('arial', 25, 'italic'))
turtle.color(255,255,255)
turtle.fd(400)

turtle.up()
turtle.setpos(280,40)
turtle.pencolor(255,255,0)
turtle.color(255,255,0)
turtle.begin_fill()
turtle.circle(110)
turtle.end_fill()

turtle.lt(90)
turtle.fd(10)
turtle.down()

turtle.done()