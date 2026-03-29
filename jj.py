import turtle as t
t.shape("turtle") # pen cursor shape
t.pensize(5)
t.color("red")
t.color("#2eff25") # color code


# t.donet.fillcolor(0.1, 0.4, 0.6) #red, green, blue
t.speed("slowest") # the slowest speed
# t.forward(100) # move 100pix
# t.right(80) 
# t.forward(40)
# t.left(50)
# t.back(100)
# t.begin_fill() # start filling the circle
# t.circle(25) # drawing a circle
# t.end_fill() # end filling the circle
# t.penup() # stop drawing
# t.goto(-100, 100) #coordinates (x, y)
# t.pendown() # start drawing again
# t.circle(150)
screen = t.Screen()
screen.onkey(lambda: t.forward(5), 'w')
screen.onkey(lambda: t.right(5), 'd')
screen.onkey(lambda: t.back(5), 's')
screen.onkey(lambda: t.left(5), 'a')
screen.onclick(lambda x,y: t.goto(x, y))
screen.listen()
t.done()