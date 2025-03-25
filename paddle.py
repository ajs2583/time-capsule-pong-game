from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        new_y = self.ycor() + 22
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 22
        self.goto(self.xcor(), new_y)
