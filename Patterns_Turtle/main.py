from turtle import Turtle
import random 


t = Turtle()
t.screen.bgcolor("black")
colours = ["#FF5733", "#FFBD33", "#75FF33", "#33FFBD", "#3385FF", "#9B33FF", "#FF33A8"]
colors=[random.choice(colours),random.choice(colours)]

for x in range(530):
        for colour in colors:
            t.color(colour)
            t.speed(x+1000000000000000)
            t.forward(x)
            t.right(89)
t.screen.mainloop()