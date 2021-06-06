from random import randint, choice
from turtle import Turtle


COLOR = ["red", "blue", "green", "white", "yellow"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(choice(COLOR))
        self.speed("fastest")
        self.random_x = randint(-280, 280)
        self.random_y = randint(-280, 280)
        self.goto(self.random_x, self.random_y)
        self.refresh()

    def refresh(self):
        self.random_x = randint(-280, 280)
        self.random_y = randint(-280, 280)
        self.goto(self.random_x, self.random_y)
        self.color(choice(COLOR))