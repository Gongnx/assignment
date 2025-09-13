from turtle import *

def draw_heart():
    import turtle as t  
    t.setup(1000.800)
    t.pensize(5)
    t.color("blue")
    t.fillcolor
    t.begin_fill()

    t.lt(50) 
    t.circle(-100,180)

    t.rt(10)
    t.fd(200)

    t.rt(80)
    t.fd(200)

    t.rt(10)
    t.circle(-100,180)
    t.end_fill()
    t.done()
    exitonclick()

def draw_sun():
    import turtle as t 
    t.pensize(3)
    t.speed(5)
    t.color("red")
    for i in range (80):
        t.fd(200),
        t.left(170)   
    exitonclick()

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for heart, 2 for sun)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_heart()
        elif a == 2:
            draw_sun()
        else:
            print("Please input the value in [1,2]")
    except:
        print("Please input the value in [1,2]")
