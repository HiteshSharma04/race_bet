from turtle import Turtle, Screen
import random
screen = Screen()
screen.listen()
bet = screen.textinput(title="make your bet", prompt="select Your Turtle who WIN THE RACE? Color: ")
screen.setup(width=900, height=700)
colors = ["red","green","blue","orange","yellow","pink","brown"]
race = False
# H = Turtle(shape="turtle")
# H.penup()
# H.goto(x=-430, y=-150)
# H.color(colors[0])

# M = Turtle(shape="turtle")
# M.penup()
# M.goto(x=-430, y=-100)
# M.color(colors[1])

# D = Turtle(shape="turtle")
# D.penup()
# D.goto(x=-430, y=-50)
# D.color(colors[2])

# S = Turtle(shape="turtle")
# S.penup()
# S.goto(x=-430, y=0)
# S.color(colors[3])

# C = Turtle(shape="turtle")
# C.penup()
# C.goto(x=-430, y=50)
# C.color(colors[4])

# T = Turtle(shape="turtle")
# T.penup()
# T.goto(x=-430, y=100)
# T.color(colors[5])

# A = Turtle(shape="turtle")
# A.penup()
# A.goto(x=-430, y=150)
players = []
y  = [-150,-100,-50,0,50,100,150]

for i in range(0,7):
    H = Turtle(shape="turtle")
    H.penup()
    H.goto(x=-430, y=y[i])
    H.color(colors[i])
    players.append(H)
if bet:
    race = True

while race:
    for i in players:
        if i.xcor() > 420:
            race = False
            win = i.pencolor()
            if win == bet:
                print(f"YOU WON! & {win} is the WINNER")
            else:
                print(f"YOU LOOSE! & {win} is the WINNER")

        i.forward(random.randint(0,20))

screen.exitonclick()