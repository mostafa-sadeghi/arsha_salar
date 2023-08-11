from turtle import Screen, Turtle
from random import randint
from time import sleep

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

def change_position(object):
    x = randint(-270, 270)
    y = randint(-270, 230)
    object.goto(x,y)

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

def go_up():
    snake_head.direction = "up"

def go_down():
    snake_head.direction = "down"

def go_right():
    snake_head.direction = "right"

def go_left():
    snake_head.direction = "left"
main_screen = create_screen()
snake_head = create_turtle("square","green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)

main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_up, "w")

main_screen.onkeypress(go_down, "Down")
main_screen.onkeypress(go_down, "s")

main_screen.onkeypress(go_right, "Right")
main_screen.onkeypress(go_right, "d")

main_screen.onkeypress(go_left, "Left")
main_screen.onkeypress(go_left, "a")

running = True
while running:
    main_screen.update()
    move()
    sleep(0.2)