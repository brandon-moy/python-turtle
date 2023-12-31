# Mini project to create an object that will grow until it pops when up key is pressed
# 1. be able to detect inputs
# 2. require multiple inputs to pop the balloon
# 3. utilize variables, conditions and function

# start
# draw the balloon
# has key been pressed?
# yes -> has the balloon reach max size?
#   yes -> clear the balloon and write POP!
#   no -> increase balloon size and redraw balloon
# end

import turtle

diameter = 40
pop_diameter = 100

def draw_balloon ():
    turtle.color("red")
    turtle.dot(diameter)
    
def inflate_balloon ():
    global diameter
    diameter += 10
    draw_balloon()
    
    if diameter >= pop_diameter:
        turtle.clear()
        diameter = 40
        turtle.write("POP!")
    
draw_balloon()
turtle.onkey(inflate_balloon, "Up")
turtle.listen()

turtle.done()