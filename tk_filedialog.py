import tkinter as tk
import os

window=tk.Tk()
window.title("window title")
window.geomery(350,200)

def clicked():
	file=filedialog.askopenfilenames()#file 变量将会保存该文件的路径
     dir=filedialog.askdirectory()#函数可以让我们请求目录
     

btn=Button(window,text='Click me",command=clilcked)
btn.grid(column=0,row=0)

window.mainloop()