from turtle import Turtle
import random
tim = Turtle()
def draw_shapes(sides_polygon):
    angle = 360/sides_polygon
    for _ in range(sides_polygon):
     tim.forward(100)
     tim.right(angle)
colors = ["CornflowerBlue" , "DarkOrchid" , "IndianRed" , "DeepSkyBlue" , "LightSeaGreen" , "wheat" , "SlateGray" , "SeaGreen"]    
for shape_side_n in range(3 , 11):
 tim.color()
 draw_shapes(shape_side_n)    
 tim.color(random.choice(colors))