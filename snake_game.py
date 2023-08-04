from turtle import Screen, Turtle

def create_screen():
    my_window = Screen()
    my_window.title("Snake Game")
    my_window.setup(600, 600)
    my_window.bgcolor("black")
    return my_window

def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed('fastest')
    return my_turtle

main_screen = create_screen()
snake_head = create_turtle("square","blue")

running = True
while running:
    main_screen.update()