import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=Tk()## 创建窗口：实例化一个窗口对象。

root.geometry("600x400")#传入的是"宽x高",号是小写的英文字母x,调整窗口的大小；
root.geometry("600x400+100+200")#100,200表示的是窗口顶点，距离电脑左上角的坐标
root.title("my title")

def draw_line():
    canvas.create_line(0, 0,100,200)
    line1=w.create_line(0,100,400,100,fill='orange')#起点的x/y，终点的x/y：距离root窗口左上角的距离
    line2=w.create_line(200,0,200,200,fill="red",dash=(4,4))
    rectange_1=w.create_rectangle(10,5,100,15,fill='blue')

w=Canvas(root,width=400,height=200,background='yellow')

w.pack()



canvas = tk.Canvas(root, width=300, height=300)
canvas.bind("<Button-1>", draw_line)
canvas.pack()


#------menu

def function():
    print("print sth")
    #tkinter.messagebox.Message(master=None)
    tk.messagebox.showinfo(title="message",message="message")
   # tk.messagebox.showerror(title="message",message="message")

menubar = tk.Menu(root) 
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=function)
filemenu.add_command(label="Open",command=draw_line)
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Cut")
editmenu.add_command(label="Paste")
editmenu.add_command(label="显示问候")

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()