# Mini project to create a star display on a black background
# utilizie randomness for the size and position
# use a for loop to generate a large amount of stars

# set backgrouund to black
# check if stars have been drawn
# if no, generate random x and y coordinate, generate random size, and draw the star
from turtle import *
from random import *

speed(0)

bgcolor("black")
hideturtle()

width = window_width()
height = window_height()

def draw_star(xpos, ypos):
  size = randrange(2, 7)
  penup()
  goto(xpos, ypos)
  pendown()
  dot(size, "white")
  
for x in range(100):
  xpos = randrange(int(-width / 2), int(width / 2))
  ypos = randrange(int(-height / 2), int( height / 2))
  draw_star(xpos, ypos)

done()