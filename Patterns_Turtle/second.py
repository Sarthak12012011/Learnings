from turtle import Turtle
import random

# Set up turtle
t = Turtle()
t.screen.bgcolor("black")
colours = ["#FF5733", "#FFBD33", "#75FF33", "#33FFBD", "#3385FF", "#9B33FF", "#FF33A8"]
colors = [random.choice(colours), random.choice(colours)]

t.penup()
# Start near the edge of the screen
screen_width = t.screen.window_width()
screen_height = t.screen.window_height()
margin = 50  # Margin from screen edges
start_x = -screen_width // 2 + margin
start_y = screen_height // 2 - margin
t.goto(start_x, start_y)
t.pendown()

# Start with a reasonable length
start_length = min(screen_width, screen_height) * 1.2  # 1.2x screen size
for x in range(300, 0, -1):  # Shorten the spiral range
    for colour in colors:
        t.color(colour)
        t.speed(0)
        length = start_length * (x / 300)  # Shrink length smoothly
        t.forward(length)
        t.right(89)

t.screen.mainloop()
