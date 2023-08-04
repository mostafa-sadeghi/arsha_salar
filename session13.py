import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

sides = int(screen.textinput("userInput","How many sides?"))

for i in range(sides):
    my_turtle.forward(120)
    my_turtle.left(360/sides)


turtle.done()