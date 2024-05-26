import turtle

def draw_house():
    # Setup the turtle
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    house_turtle = turtle.Turtle()
    house_turtle.speed(5)

    # Draw the base of the house
    house_turtle.penup()
    house_turtle.goto(-100, -100)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("yellow")
    for _ in range(4):
        house_turtle.forward(200)
        house_turtle.left(90)
    house_turtle.end_fill()

    # Draw the roof
    house_turtle.begin_fill()
    house_turtle.color("red")
    house_turtle.goto(-100, 100)
    house_turtle.goto(0, 200)
    house_turtle.goto(100, 100)
    house_turtle.goto(-100, 100)
    house_turtle.end_fill()

    # Draw the door
    house_turtle.penup()
    house_turtle.goto(-25, -100)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("brown")
    for _ in range(2):
        house_turtle.forward(50)
        house_turtle.left(90)
        house_turtle.forward(80)
        house_turtle.left(90)
    house_turtle.end_fill()

    # Draw a window
    house_turtle.penup()
    house_turtle.goto(30, 0)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("white")
    for _ in range(4):
        house_turtle.forward(50)
        house_turtle.left(90)
    house_turtle.end_fill()

    # Draw window panes
    house_turtle.color("black")
    house_turtle.penup()
    house_turtle.goto(30, 25)
    house_turtle.pendown()
    house_turtle.forward(50)
    house_turtle.penup()
    house_turtle.goto(55, 0)
    house_turtle.pendown()
    house_turtle.left(90)
    house_turtle.forward(50)

    # Hide the turtle and display the window
    house_turtle.hideturtle()
    turtle.done()

# Call the function to draw the house
draw_house()
