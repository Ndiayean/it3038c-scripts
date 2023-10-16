import turtle

window = turtle.Screen()


##This will control the the window
window.bgcolor("white")


##This will draw the custom turtle image on the screen
simpleturtle = turtle.Turtle()
simpleturtle.shape("turtle")
simpleturtle.color("blue", "yellow")


##This will move the turtle
simpleturtle.begin_fill()
simpleturtle.forward(200)
simpleturtle.left(90)
simpleturtle.forward(200)
simpleturtle.left(90)
simpleturtle.forward(200)
simpleturtle.left(90)
simpleturtle.forward(200)
simpleturtle.end_fill()



##This will close the module
window.exitonclick()