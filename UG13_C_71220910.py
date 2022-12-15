import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor('green')
t.color('white')
t.pensize(10)
t.penup()
t.left(180)
t.forward(200)
t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.circle(-50,180)

t.penup()
t.right(180)
t.forward(100)
t.pendown()
t.left(90)
t.forward(100)

t.penup()
t.right(90)
t.forward(50)
t.pendown()
t.forward(50)
t.left(180)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

#angka 0
t.penup()
t.left(90)
t.forward(80)
t.pendown()
t.circle(-50,360)
t.penup()

#angka 9
t.goto(-75,250)
t.penup()
t.pendown()
t.right(360)
t.penup()
t.forward(70)
t.pendown()
t.left(180)
t.forward(50)
t.circle(30,-360)
t.right(180)
t.forward(60)
t.circle(-30,180)








turtle.done()