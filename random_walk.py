#random walk
import turtle as t 
import random
timmy = t.Turtle()
colors = ["CornflowerBlue" , "DarkOrchid" , "IndianRed" , "DeepSkyBlue" , "LightSeaGreen" , "wheat" , "SlateGray" , "SeaGreen"] 
timmy.pensize(5)
direction = [0 , 90 , 180 , 270]
for _ in range(150):
   timmy.forward(55)
   timmy.setheading(random.choice(direction))
   timmy.color(random.choice(colors))
screen = Screen()
screen.exitonclick()