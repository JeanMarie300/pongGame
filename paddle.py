from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.setheading(UP)



    def headUP(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def headDown(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

