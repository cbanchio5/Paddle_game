from distutils.dep_util import newer_pairwise
from turtle import Turtle
POSITION_LEFT_PADDLE=(350,0)
POSITION_RIGHT_PADDLE=(-350,0)
MOVE_DISTANCE=20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.clear()
        self.shape("square")
        self.right(90)
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.shapesize(1,5,1)
        self.goto(position)


    def move_up(self):
        
        self.forward(-1*MOVE_DISTANCE)  
        


    def move_down(self):
        
        self.forward(MOVE_DISTANCE)  
        