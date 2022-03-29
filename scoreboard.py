from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto(-100,200)
        self.write(f"{self.l_score}",False, "center", ("courier", 80, "normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",False, "center", ("courier", 80, "normal"))


    def l_point(self):
        self.clear()
        self.l_score+=1 
        self.goto(-100,200)
        self.write(f"{self.l_score}",False, "center", ("courier", 80, "normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",False, "center", ("courier", 80, "normal"))   
    
    def r_point(self):
        self.clear()
        self.r_score+=1 
        self.goto(-100,200)
        self.write(f"{self.l_score}",False, "center", ("courier", 80, "normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",False, "center", ("courier", 80, "normal"))     