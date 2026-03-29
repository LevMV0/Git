# from random import random
# from random import *

import random as r  #name for module
print(r.randint(10,15)) # from 10 to 15 str
print(r.randrange(10, 19, 2)) # 10, 12, 14, 16, 18 -> random number
print(r.random()) # from 0 to 1 float
print(r.uniform(-10.5, 10.5)) # random float, neg and pos
fruits = ['apple', 'mango', 'banana']
print(r.choice(fruits)) # random symbol from fruits
print(r.choice('hello')) # random symbol from text
print(r.choices(fruits, k=3)) # 3 random, with repetition
print(r.choices(fruits, weights = [0.5, 0.1, 0.2, 0.05, 0.15], k = 3)) # weights - chance to be chosen
print(r.sample(fruits, k = 4)) # 4 random WITHOUT repetition

fruits.sort()
print(fruits)
r.shuffle(fruits) # shuffle elements from fruits
print(fruits)

import math as m
print(m.pi)
print(m.e)
print(m.inf)
m.log(10, 10)
m.log(10)
m.ceil(20.6) # round up
m.floor(20.6) # round down
m.trunc(20.6)
m.fabs(-10.5)
abs(10.6)
m.sqrt(9)
m.factorial(5)
m.atan2() #arctan
m.pow(10.5, 1.5) # power for float
m.gcd(10.5) # greatest common divisor

import string as s
print(s.ascii_letters) # ascii alfabet
print(s.ascii_lowercase) # lower symbols from ascii
print(s.ascii_uppercase) # upper symbols from ascii
s.digits #numbers 0-9
s.hexdigits
s.octdigits
s.punctuation #punctuation symbols
s.whitespace # all space symbols " ", "\n", "\r", "\t"
s.printable 

import turtle as t
t.shape("turtle") # pen cursor shape
t.pensize(5)
t.color("red")
t.color("#2eff25") # color code
t.fillcolor(0.1, 0.4, 0.6) #red, green, blue
t.speed("slowest") # the slowest speed
t.forward(100) # move 100pix
t.right(80) 
t.forward(40)
t.left(50)
t.back(100)
t.begin_fill() # start filling the circle
t.circle(25) # drawing a circle
t.end_fill() # end filling the circle
t.penup() # stop drawing
t.goto(-100, 100) #coordinates (x, y)
t.pendown() # start drawing again
t.circle(150)
screen = t.Screen()
screen.onkey(lambda: t.forward(5), 'w')
screen.onkey(lambda: t.right(5), 'd')
screen.onkey(lambda: t.back(5), 's')
screen.onkey(lambda: t.left(5), 'a')
screen.onclick(lambda x,y: t.goto(x, y))
screen.listen()
t.done
SHAPE = "turtle"
COLOR = ("#692075")
FILL_COLOR = ("#B544C6")
PEN_SIZE = 5
SPEED = "slowest"
