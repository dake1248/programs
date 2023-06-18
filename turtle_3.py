import turtle
import random
t0=turtle.Turtle()
t0.speed(10)
t0.color('red', 'yellow')

def function():
	t0_fd=random.randrange(100,600)
	t0.begin_fill()
	#while True:
	for i in range(72):
		t0.forward(t0_fd)
		t0.left(175)
		#if abs(t0.pos()) < 1:
		#	break
	t0.end_fill()

while(1):
	t0.penup()
	t0.setposition(random.randrange(600),random.randrange(200))
	t0.pendown()
	function()
