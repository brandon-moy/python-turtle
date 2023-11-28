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

done()