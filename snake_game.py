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
    object.goto(x, y)


def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)


def go_up():
    snake_head.direction = "up"


def go_down():
    snake_head.direction = "down"


def go_right():
    snake_head.direction = "right"


def go_left():
    snake_head.direction = "left"


def reset(snake_tails):
    global score
    score = 0
    snake_head.goto(0, 0)
    snake_head.direction = ""
    for tail in snake_tails:
        tail.ht()
    snake_tails.clear()


main_screen = create_screen()
snake_head = create_turtle("square", "green")
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
main_screen.tracer(False)
score = 0
high_score = 0
scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()

snake_tails = []


def on_close():
    global running
    running = False


root = main_screen._root
root.protocol("WM_DELETE_WINDOW", on_close)


running = True
while running:
    scoreboard.clear()
    scoreboard.write(f"Score:{score}, HighScore: {high_score}", font=("arial", 22),
                     align="center")

    main_screen.update()
    if snake_head.distance(snake_food) < 20:
        score += 1

        change_position(snake_food)
        new_tail = create_turtle("square", "green")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i - 1].xcor()
        y = snake_tails[i - 1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        if score > high_score:
            high_score = score
        reset(snake_tails)

    move()

    for tail in snake_tails:
        if tail.distance(snake_head) < 20:
            reset(snake_tails)

    sleep(0.2)
