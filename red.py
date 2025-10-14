import turtle
screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.fillcolor("red")  
pen.pensize(2)

pen.begin_fill()
pen.circle(100)  
pen.end_fill()


pen.hideturtle()
turtle.done()
