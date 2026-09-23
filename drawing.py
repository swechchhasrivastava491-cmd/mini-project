#wap to ask user to draw the shape they want to make
#asking the choice of user

import turtle

def sqaure():
    screen=turtle.Screen()
    screen.bgcolor("lightyellow")
    t=turtle.Turtle()
    t.pensize(3)
    t.speed(1)
    t.color("grey")
    for i in range(4):
        t.forward(100)
        t.right(90)
    #turtle.done()

def triangle():
    screen=turtle.Screen()
    screen.bgcolor("lightyellow")
    t=turtle.Turtle()
    t.pensize(3)
    t.speed(1)
    t.color("pink")
    for i in range(3):
        t.forward(100)
        t.left(120)
    #turtle.done()

def star():
    screen=turtle.Screen()
    screen.bgcolor("lightyellow")
    t=turtle.Turtle()
    t.pensize(3)
    t.speed(1)
    t.color("red")
    for i in range(5):
        t.forward(100)
        t.right(144)
    #turtle.done()

def circle():
    screen=turtle.Screen()
    screen.bgcolor("red")
    t=turtle.Turtle()
    t.pensize(3)
    t.speed(1)
    t.color("grey")
    t.circle(100)
    
    #turtle.done()
print("Welcome! to turtle drawing app")
user=input('choose the shape you want to draw (sqaure,triangle,star,cirle):')
if(user=='sqaure'):
    sqaure()

elif(user=='triangle'):
    triangle()

elif(user=='star'):
    star()

else:
    circle()



turtle.done()