from turtle import *

#we want to paint a house

#step 1: draw a aquare

width(7)
color("lime")

forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)

#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward (120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right (150)
forward(200)
left(120)
forward(200)
end_fill()

color("lime")
left(30)
forward (20)
color("blue")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(200, 200)
pendown()

color("lime")
left(90)
forward (20)
color("blue")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




exitonclick()