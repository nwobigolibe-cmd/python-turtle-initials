
#Name: Nwobi Golibe
#This is program that will draw an approximation to the letters of my name on a background of my choice

import turtle #To import the turtle module

window = turtle.Screen()
window.bgcolor("pink")
window.title("My Initials: N G A")
golibe = turtle.Turtle()
golibe.pencolor("black")
golibe.pensize(10)
golibe.pendown()
golibe.speed(10)

# Draw the letter "N"
golibe.penup()
golibe.goto(-300, 50)
golibe.pendown()
golibe.right(90)
golibe.forward(150)
golibe.backward(150)
golibe.left(40)
golibe.forward(190)
golibe.left(142)
golibe.forward(150)

# Move to start 'G'
golibe.penup()
golibe.goto(10, -10)
golibe.pendown()

# Draw 'G'
golibe.penup()
golibe.circle(70,75)
golibe.pendown()
golibe.circle(70, 230)
golibe.setheading(90)
golibe.forward(50)
golibe.right(90)
golibe.forward(20)
golibe.backward(40)

# Move to start 'A'
golibe.penup()
golibe.goto(60, -95)
golibe.pendown()

# Draw 'A'
golibe.left(75)
golibe.forward(150)
golibe.right(150)
golibe.forward(150)
golibe.penup()
golibe.backward(80)
golibe.pendown()
golibe.right(105)
golibe.forward(30)

# Display window
window.mainloop()
