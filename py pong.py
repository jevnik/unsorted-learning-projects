import turtle as tr
import random as rand

sc = tr.Screen()
sc.setup(1000,600)

def ply_one_up():
    ply_one.sety(ply_one.ycor() + 10) 

def ply_one_down():
    ply_one.sety(ply_one.ycor() - 10) 

def ply_two_up():
    ply_two.sety(ply_two.ycor() + 10) 

def ply_two_down():
    ply_two.sety(ply_two.ycor() - 10) 

ply_one = tr.Turtle()
ply_one.color("blue")
ply_one.speed(0)
ply_one.penup()
ply_one.goto(-400, 0)
ply_one.shape("square")
ply_one.shapesize(stretch_wid = 10, stretch_len=2)

ply_two = tr.Turtle()
ply_two.color("red")
ply_two.speed(0)
ply_two.penup()
ply_two.goto(400, 0)
ply_two.shape("square")
ply_two.shapesize(stretch_wid = 10, stretch_len=2)

ball = tr.Turtle()
ball.penup()
ball.shape("circle")
ball.speed(0)
ball.goto(0,0)
ball.velx = 5
ball.vely = 0


bodovanje = tr.Turtle()
bodovanje.penup()
bodovanje.hideturtle()
bodovanje.goto(-50, 250)


ply_one.score = 0
ply_two.score = 0

bodovanje.write("Player One: {}    Player Two: {}".format(ply_one.score, ply_two.score) )
ball.vely = ((ball.vely + 1) + (rand.random() - rand.random()))* 10*rand.random()

while True:
    tr.listen()
    
    #loptica kretanje


    ball.setx(ball.xcor() + ball.velx)
    ball.sety(ball.ycor() + ball.vely)
    
    #kontrole
    
    tr.onkeypress(ply_one_up,"w")
    tr.onkeypress(ply_one_down,"s")
    tr.onkeypress(ply_two_up,"Up")
    tr.onkeypress(ply_two_down,"Down") 
    
    #granice igraca
    
    if ply_one.ycor() > 200:
        ply_one.sety(200)
    if ply_one.ycor() < -200:
        ply_one.sety(-200)

    if ply_two.ycor() > 200:
        ply_two.sety(200)
    if ply_two.ycor() < -200:
        ply_two.sety(-200)

    #odbijanje od igraca
    
    if ball.xcor() < -370 and (ball.ycor() < ply_one.ycor()+100) and (ball.ycor() > ply_one.ycor() - 100):

        ball.velx = ball.velx * -1
        ball.velx *= 1.5
        print(ball.vely)
    
    if ball.xcor() > 370 and (ball.ycor() < ply_two.ycor()+100) and (ball.ycor() > ply_two.ycor() - 100):

        ball.velx = ball.velx * -1
        ball.velx *= 1.5
        print(ball.vely)

    #odbijanje od ruba
    
    if ball.xcor() > 490:
        ball.setx(0)
        ball.vely = ((ball.vely + 1) + rand.randint(-2,2))
        ply_one.score = ply_one.score + 1
        bodovanje.clear()
        bodovanje.write("Player One: {}    Player Two: {}".format(ply_one.score, ply_two.score) )
        ball.velx = 5
        ball.velx = ball.velx * -1
        

    if ball.xcor() < -490:
        ball.setx(0)
        ball.vely = ((ball.vely + 1) + rand.randint(-2,2))
        ply_two.score = ply_two.score + 1
        bodovanje.clear()
        bodovanje.write("Player One: {}    Player Two: {}".format(ply_one.score, ply_two.score) )
        ball.velx = 5
        ball.velx = ball.velx * -1
        
    
    if ball.ycor() > 300:
        ball.sety(300)
        ball.vely = ball.vely * -1
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.vely = ball.vely * -1

tr.exitonclick()