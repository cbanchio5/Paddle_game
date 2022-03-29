from turtle import Turtle

ANGLE=-40

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move=10 
        self.y_move=10
        self.move_speed=0.1
        
        
       
        


    def move_ball(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def change_direction(self):
        self.y_move *= -1

    def change_direction_1(self):
        self.x_move *= -1
        self.move_speed*=0.9   

    def reset(self):
        self.goto(0,0)
        self.change_direction_1()
        self.move_speed=0.1    
        

    
