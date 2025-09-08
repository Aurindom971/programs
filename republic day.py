import turtle


#creating window
win=turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor('black')





#flag
stand=turtle.Turtle()
stand.color('white')
stand.shape('square')
stand.penup()
stand.setposition(-100,-280)
stand.pendown()
stand.goto(-100,280)


flag=turtle.Turtle()
flag.color('white')
flag.penup()
flag.setposition(-100,270)
flag.pendown()

lenght=400
width=80

def rect(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(lenght)
    flag.right(90)
    flag.forward(width)
    flag.right(90)
    flag.forward(lenght)
    flag.right(180)
    flag.end_fill()
rect('orange')
rect('white')
rect('green')
#creating ashoka 

ashoka=turtle.Turtle()
ashoka.color('blue')
ashoka.penup()
ashoka.width(2)
ashoka.goto(100,110)
ashoka.pendown()
ashoka.circle(40)
ashoka.penup()
ashoka.goto(100,150)
ashoka.pendown()
for i in range(24):
    ashoka.forward(38)
    ashoka.backward(38)
    ashoka.right(15)
text=turtle.Turtle()
text.speed(2)
text.hideturtle()


def write(message,pos,color):
    x,y=pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style=('courier',40,'italic')
    text.write(message,font=style)

write('happy',(60,-100),'orangle')
write('rep',(10,-160),'white')
write('ub',(105,-160),'blue')
write('lic',(167,-160),'white')
write('day',(70,-220),'green')





turtle.done()
