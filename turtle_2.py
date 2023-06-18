import turtle
import random

'''
                |
      t1        |       t0
                |
                |
________________|________________
                |
                |
       t2       |       t3
                |
________________|_


'''

t0=turtle.Turtle()
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()

t0.speed(10)
t1.speed(10)
t2.speed(10)
t3.speed(10)

t0.hideturtle()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

t0.setpos(100,100)
t1.setpos(-100,100)
t2.setpos(-100,-100)
t3.setpos(100,-100)

t0.pencolor('red')
t1.pencolor('purple')
t2.pencolor('brown')
t3.pencolor('blue')

def function_t0():
    if random.randrange(7)==0:
        t0.clear()
        t1.clear()
        t2.clear()
        t3.clear()
        t0.setpos(100,100)
        t1.setpos(-100,100)
        t2.setpos(-100,-100)
        t3.setpos(100,-100)
    else:
        t0.dot(random.randrange(100))
        t0.forward(random.randrange(100))
        t1.circle(random.randrange(200))
        t2.setpos(random.randrange(100),random.randrange(100))
        t2.forward(20)
        t2.dot(random.randrange(20))
        t3.fd(random.randrange(100))
        t3.circle(random.randrange(100))
while(1):
    function_t0()
   # turtle.ontimer(function_t0,t=1000)#1000ms后执行fuction
   # t1.dot(random.randrange(20),'red')
    '''
for i in range(300):
    turtle.ontimer(function_t0,t=10000)#1000ms后执行fuction

#t0.clear()
#t1.clear()
'''