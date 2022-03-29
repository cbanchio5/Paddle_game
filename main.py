import turtle
import time
from paddles import Paddle
from create_line import Line
from ball import Ball
SPEED=0.1

from scoreboard import Scoreboard
POSITION_LEFT_PADDLE=(350,0)
POSITION_RIGHT_PADDLE=(-350,0)

screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")


screen.tracer(0)
paddle_left=Paddle(POSITION_LEFT_PADDLE)
paddle_right=Paddle(POSITION_RIGHT_PADDLE)
score=Scoreboard()
ball=Ball()



screen.listen()
screen.onkey(paddle_left.move_up,"Up")
screen.onkey(paddle_left.move_down, "Down")
screen.onkey(paddle_right.move_up,"w")
screen.onkey(paddle_right.move_down, "s")


game_is_on=True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.change_direction()
        

    if (ball.distance(paddle_left)<40 and ball.xcor()>320) or (ball.distance(paddle_right)<40 and ball.xcor()<-320):
        ball.change_direction_1()
        


    if ball.xcor()>380:
        score.l_point()
        ball.reset()   

    if ball.xcor()<-380:
        score.r_point()
        ball.reset()       

    

    

            
    
   
    
   





screen.exitonclick()