#etch-a-sketch
#W to move forwards
#S to move backwards
#A to move leftwards
#D to move right
#C to clear the drawing
from turtle import Turtle , Screen
import random
colors = ["CornflowerBlue" , "DarkOrchid" , "IndianRed" , "DeepSkyBlue" , "LightSeaGreen" , "wheat" , "SlateGray" , "SeaGreen"] 
screen = Screen()
jim = Turtle()
jim.pensize(3)
jim.color(random.choice(colors))
def move_forwards():
    jim.forward(10)
screen.listen()
screen.onkey(key = "w" , fun = move_forwards)
def move_backwards():
    jim.backward(10)
screen.listen()
screen.onkey(key = "s" , fun = move_backwards)
def move_leftwards():
  new_position =  jim.heading() + 10
  jim.setheading(new_position)
  jim.forward(10)
screen.listen()
screen.onkey(key = "a" , fun = move_leftwards)
def move_right():
    new_head = jim.heading() - 10
    jim.setheading(new_head)
    jim.forward(10)
screen.listen()
screen.onkey(key = "d" , fun = move_right)
def clear_screen():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()
screen.listen()
screen.onkey(key = "space" , fun = clear_screen)





 
screen.exitonclick()
