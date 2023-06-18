import tkinter as tk

global x0
global y0

x0=0
y0=0

def draw(event):
	canvas.create_line(0,0,event.x,event.y)
	x0=event.x
	y0=event.y
	print(x0,'  ',y0)

	
root=tk.Tk()
root.geometry("300x500")

canvas=tk.Canvas(root,width=300,height=300)
canvas.bind("<Button-1>",draw)

canvas.pack()


'''
事件触发后执⾏的函数，只有事件对象⼀个参数，事件对象包含了如下信息
1. keysym 触发事件的键盘按钮
2. keycode 触发基于键盘的事件的键的代码
3. button 返回触发基于⿏标的事件的鼠标按钮（1-5）
4. x, y 事件所在位置的x,y坐标
5. width, height 关联控件的宽与高

'''

root.mainloop()