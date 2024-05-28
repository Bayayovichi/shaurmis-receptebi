print("day 0 homework")
from turtle import *


#we want to paint a house
speed(10)
#step 1: draw a square
width(7)
color ("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#drawning a door

forward (70)
color("yellow")
begin_fill()
left (90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto (200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows

#left window

color("purple")
left(30)
forward(70)

left(90)
forward(7)

color("white")
forward(13)

color("blue")
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(180)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)

#left window
penup()
goto (200, 200)
pendown()

color("purple")
right(90)
forward(70)
right(90)
forward(7)

color("white")
forward(13)

color("blue")
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(180)

forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)


#floor fix
color("purple")
penup()
goto (0, 0)
left(180)
forward(200)
#failed



exitonclick()

