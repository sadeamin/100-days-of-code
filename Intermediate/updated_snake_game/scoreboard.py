from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()


    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.clear()
        self.write(f"Score : {self.score}  High Score: {self.high_score}", False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
