import turtle

t1=turtle.Turtle()

def fuc():
    print("left button was clicked")
    t1.fd(100)
    t1.lt(90)
    t1.circle(100,60)
    

turtle.onclick(fuc,btn=1,add=None)
turtle.onrelease(fuc,btn=2,add=None)
turtle.ondrag(fuc,btn=1,add=None)


#t1.fd(100)
#t1.lt(90)
#t1.circle(100,60)

turtle.ontimer(fuc,1000)





turtle.mainloop()



