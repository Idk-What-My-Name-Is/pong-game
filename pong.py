#project1

import turtle

#screen setup
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_A = 0
score_B = 0

#playerA
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("white")
playerA.shapesize(stretch_wid=5, stretch_len=1)
playerA.penup()
playerA.goto(-350, 0)

#playerB
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("white")
playerB.shapesize(stretch_wid=5, stretch_len=1)
playerB.penup()
playerB.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

#functions
def pa_up():
    y = playerA.ycor()
    y += 20
    playerA.sety(y)

def pa_down():
    y = playerA.ycor()
    y -= 20
    playerA.sety(y)

def pb_up():
    y = playerB.ycor()
    y += 20
    playerB.sety(y)

def pb_down():
    y = playerB.ycor()
    y -= 20
    playerB.sety(y)


#key binds
wn.listen()
wn.onkeypress(pa_up, "w")
wn.onkeypress(pa_down, "s")
wn.onkeypress(pb_up, "Up")
wn.onkeypress(pb_down, "Down")





#main game loop
while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check if ball hits borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("courier", 24, "normal"))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < playerB.ycor() + 40 and ball.ycor() > playerB.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > playerA.ycor() - 40 and ball.ycor() < playerA.ycor() +40):
        ball.setx(-340)
        ball.dx *= -1

    if score_A == 11:
        pen.clear()
        score_A -= 11
        score_B -= score_B
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("courier", 24, "normal"))

    if score_B == 11:
        pen.clear()
        score_B -= 11
        score_A -= score_A
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("courier", 24, "normal"))