import tkinter
from tkinter import *
from tkinter import messagebox
a=100
b=200
root=Tk()## 创建窗口：实例化一个窗口对象。

root.geometry("600x400")#传入的是"宽x高",号是小写的英文字母x,调整窗口的大小；
root.geometry("600x400+100+200")#100,200表示的是窗口顶点，距离电脑左上角的坐标
root.title("my title")

#-----------添加标签控件，并定位
#label=Label(root)
label = Label(root,text="签名",font=("宋体",25),fg="red")
label.grid(row=0,column=0)

#------------添加输入框，并定位
entry=Entry(root,font=("宋体",25),fg='red')
'''第一个参数传入的就是实例化的那个root窗口对象；第二个参数可写可不写，指的是我们输入的
字体的字体样式和字体大小；第三个参数同样可写可不写，表示的是我们输入的字体的颜色。'''
#entry.grid()#只有调用grid()方法，定位后，才会真正显示这个输入框.
entry.grid(row=0,column=1)#row=0,column=1表示我们将输入框控件，放在第1行第2列的位

#-----------添加点击按钮
button=Button(root,text='签名设计',font=('宋体',10),fg='blue')
button.grid(row=0,column=2)

def function():
    print("print sth")
    #tkinter.messagebox.Message(master=None)
    tkinter.messagebox.showinfo(title="message",message="message")
    tkinter.messagebox.showerror(title="message",message="message")
    
    
button_fuc=Button(root,text='button_func',font=('宋体',10),fg='blue',command=function)
button_fuc.grid(row=2,column=0)

root.mainloop()## 显示窗口

