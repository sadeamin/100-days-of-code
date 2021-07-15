from turtle import Turtle, Screen

tim = Turtle()

tim.pensize(2)

def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def turn_left():
    tim.left(18)

def turn_right():
    tim.right(18)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()