from turtle import Turtle

class Puddle(Turtle):
    def __init__(self, position):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()
            self.goto(position)

    def goup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def godown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)