# Create a turtle that can move in 4 directions
# have an "end goal"
# have visual feedback for reaching the goal

# draw "land"/"sand"
# draw "water"
# move turtle to start
# move turtle when key is pressed
# has turtle reach goal?
# yes -> hide turtle and display visual feedback

from turtle import *
speed(0)
move_distance = 20
width = window_width()
height = window_height()

bgcolor("tan")

color("blue")

penup()
goto(300, height)
pendown()

begin_fill()
goto(width, height)
goto(width, -height)
goto(300, -height)
goto(300, height)
end_fill()

penup()
goto(-300, 0)
shape("turtle")
color("green")

def move_up ():
  setheading(90)
  forward(move_distance)
  check_goal()

def move_down ():
  setheading(270)
  forward(move_distance)
  check_goal()
  
def move_right ():
  setheading(0)
  forward(move_distance)
  check_goal()
  
def move_left ():
  setheading(180)
  forward(move_distance)
  check_goal()
  
def check_goal ():
  if xcor() > 300:
    hideturtle()
    color("white")
    write("YOU WIN!")
    
    onkeypress(None, "Up")
    onkeypress(None, "Down")
    onkeypress(None, "Left")
    onkeypress(None, "Right")
  
onkeypress(move_up, "Up")
onkeypress(move_down, "Down")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")

listen()

done()