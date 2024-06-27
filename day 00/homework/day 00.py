from turtle import *


#we want to paint a house

#step 1:   paint a square
width(7)

color("grey")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()              #end of square

#drawindg a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(110) #height of the door
right(90)
forward(60)
right(90)
forward(110)
end_fill()

penup()
goto(200, 200)
pendown()

color("dark red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60, 140)
pendown()
color("skyblue")
begin_fill()
left(210)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(140, 140)
pendown()
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()








exitonclick()