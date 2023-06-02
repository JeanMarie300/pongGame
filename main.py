from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))



screen.onkey(r_paddle.headUP, "Up")
screen.onkey(r_paddle.headDown, "Down")

screen.onkey(l_paddle.headUP, "w")
screen.onkey(l_paddle.headDown, "s")

ball = Ball()

scoreboard = ScoreBoard()

start = True

while start :
    screen.update()
    time.sleep(ball.current_speed)
    ball.move()
    if ball.xcor() > 365 :
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -365 :
        ball.reset_position()
        scoreboard.r_point()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) :
        ball.bounce_x()





screen.exitonclick()