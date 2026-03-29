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