import turtle

t=turtle.Turtle()

#------------移动方向


t.right(dist)#t.rt(d)
t.forward(dist)#t.fd(d)	从当前位置向前距离
t.left(dist)#t.lt(d)	从当前位置向左偏转角度
t.backward(dist)#t.bk(d)
t.circle(radius)
t.dot(radius,color)
t.hideturtle()#隐藏画笔箭头
t.setx()#设置海⻳的x 坐标， y 坐标不变
t.setheading()#seth()设置朝向
t.home()
t.goto(0,0)
t.setpos(a,b)#设置画笔位置为(a,b)坐标位置
#--------------判断当前位置
a=t.pos()
if t.pos()>=(100,20)#直角坐标区域分布

turtle.bgclolor('blue')#'red''green',or 输入相应的十六进制码即可，如# 2 8 5 0 7 8
turtle.title("my title")
t.shapsize(0,1,2)#拉伸长度(Stretch length),拉伸宽度(Stretch width) 轮廓宽度(Outline width)

#----------------Changing the Pen Size
t.pensize(5)
t.forward(100)
#----------------Changing the Turtle and Pen Color
t.shapesize(3,3,3)
t.fillcolor('red')
t.pencolor('green')
t.color('green','red')#第一个颜色参数是画笔的颜色，第二个颜色参数是指填充的颜色
#---------------Filling in an Image
#当您使用t . b e g i n _ f i l l ( )时，你是在告诉计算机程序，你将绘制一个需要填充的封闭形状。然后，使用t . e n d _ f i l l ( )表示你已经完成了形状的创建，然后告诉计算机你可以填充它了。
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()
#----------------Changing the Turtle Shape
t.shape("turtle")#'square''triangle''classic'
t.shape("arrow")
t.shape("circle")
#---------------Changing the Pen Speed
t.sp
eed(1)#从0 (最慢的速度)到1 0 (最高的速度)的任何数字  1 最慢， 1 0 快， 0 最快
t.forward(100)
t.speed(10)
t.forward(100)

#---------------Picking the Pen Up and Down
t.penup()#不画
t.pendown()#开始画

t.undo()#你运行的最后一个命令撤消
t.clear()#清理当前的屏幕
t.reset()#屏幕将被清除，海龟的设置将全部恢复到默认参数#会清理当前的屏幕

t.stamp()#即在当前位置印⼀个海⻳的图形.返回⼀个stamp_id 。
t.clearstamp(stampid)#删除一个特定的戳
c=t.clone()#复制多个海龟：
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

#----------定时
turtle.ontimer(function,t=1000)#1000ms后执行fuction
turtle.ontimer(fun, t=0)¶

#----------事件

screen.onkey(function(), "Up")
screen.listen()

turtle.onkeyrelease(fun, key)#• – a function with    	– a string: key (e.g. “a”) or key-symbol (e.g. “space”)
turtle.onkeypress(fun, key=None)
turtle.onclick(fun, btn=1, add=None)
turtle.onscreenclick(function(), btn=1, add=None)
#• – number of the mouse-button, defaults to 1 (left mouse button)
#• – True or False – if True, a new binding will be added, otherwise it will replace a
former binding



cv=turtle.getcanvas()#Return the Canvas of this TurtleScreen. Useful for insiders who know what to do with a Tkinter Canvas.
turtle.bye()#Shut the turtlegraphics window.
turtle.exitonclick()
