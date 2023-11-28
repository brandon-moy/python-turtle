# Mini project to create a star display on a black background
# utilizie randomness for the size and position
# use a for loop to generate a large amount of stars

# set backgrouund to black
# check if stars have been drawn
# if no, generate random x and y coordinate, generate random size, and draw the star
from turtle import *
from random import *

bgcolor("black")
hideturtle()

def draw_star(xpos, ypos):
  penup()
  goto(xpos, ypos)
  pendown()
  dot(20, "white")
  
draw_star(0, 0)

done()