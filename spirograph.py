from turtle import Turtle , Screen
import random
tim = Turtle()
colors = ["CornflowerBlue" , "DarkOrchid" , "IndianRed" , "DeepSkyBlue" , "LightSeaGreen" , "wheat" , "SlateGray" , "SeaGreen"]  
tim.speed("fastest")
for _ in range(100):
  tim.color(random.choice(colors)) 
  tim.circle(100)
  current_heading = tim.heading()
  tim.setheading(current_heading + 10)

screen = Screen()
screen.exitonclick()