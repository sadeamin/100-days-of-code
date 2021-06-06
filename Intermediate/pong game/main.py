from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position[0], position[1])


    def go_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(350, self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(350, self.new_y)

        screen.listen()
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_down, "Down")


r_paddle = Paddle((350, 0))

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

