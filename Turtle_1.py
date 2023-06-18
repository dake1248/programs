import turtle
t=turtle.Turtle()

t.speed(0)
count=0
while(1):
    for i in range(10):
        t.rt(30)
        t.circle(100)
    count=count+1
    if count==20:
        break
