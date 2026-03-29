# 1
import turtle as t
t.shape("turtle") # pen cursor shape
t.pensize(5)
t.speed("slowest")
# square
t.color("red")
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
# equilateral triangle
t.penup()
t.goto(-50, 50)
t.right(90)
t.pendown()
t.color("green")
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
# pentagon
t.penup()
t.goto(-100, 100)
t.color("blue")
t.right(98)
t.pendown()
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.left(72)
t.forward(50)
t.done

# 2
import turtle as t
t.shape("turtle") # pen cursor shape
t.pensize(5)
t.speed("slowest")
# squere
t.color("yellow")
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
# triangle
t.color("red")
t.fillcolor("orange")
t.begin_fill()
t.right(90)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
t.end_fill()
t.done

# 3
import random as r
import turtle as t
count = 0
goal = 36
while count != goal:
    t.shape("turtle") # pen cursor shape
    t.pensize(5)
    t.speed("fastest")
    red = r.random()
    green = r.random()
    blue = r.random()
    t.color(red, green, blue)
    t.forward(50)
    t.right(90)
    red = r.random()
    green = r.random()
    blue = r.random()
    t.color(red, green, blue)
    t.forward(50)
    t.right(90)
    red = r.random()
    green = r.random()
    blue = r.random()
    t.color(red, green, blue)
    t.forward(50)
    t.right(90)
    red = r.random()
    green = r.random()
    blue = r.random()
    t.color(red, green, blue)
    t.forward(50)
    t.right(10)
    t.done
    count += 1