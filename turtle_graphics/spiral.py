from turtle import Turtle

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('orange')

for i in range(1,20 + 1):
    my_turtle.forward(8 * i)
    my_turtle.left(60)
