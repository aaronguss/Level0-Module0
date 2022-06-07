import turtle
if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    tooty = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    tooty.shape('turtle')
    # Set your turtle's speed using .speed(2)
    tooty.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    tooty.color('green')
    tooty.pencolor('blue')
    # Move your turtle forward using .forward(100)
    for i in range(4):
        print(i)
        tooty.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        tooty.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    tooty.goto(5, 8)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    tooty.begin_fill()
    tooty.circle(radius=250, steps=15)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle

    # and .end_fill() below
    tooty.end_fill()
    # Draw 3 more shapes with different fill colors!
    tooty.fillcolor('blue')
    tooty.begin_fill()
    tooty.circle(radius=35, steps=3)
    tooty.end_fill()
    tooty.fillcolor('pink')
    tooty.begin_fill()
    tooty.circle(radius=100, steps=5)
    tooty.end_fill()
    tooty.fillcolor('aquamarine')
    tooty.begin_fill()
    tooty.circle(radius=180, steps=8)
    tooty.end_fill()


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
