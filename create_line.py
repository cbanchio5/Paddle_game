from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__
        self.pencolor("red")
        self.pendown()
        self.pensize(10)
        self.goto(0, 400)
        
