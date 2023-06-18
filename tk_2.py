import tkinter 
from tkinter import *
from tkinter import messagebox
a=100
b=200
root=Tk()## 创建窗口：实例化一个窗口对象。

def function():
    print("print sth")
    #tkinter.messagebox.Message(master=None)
    tkinter.messagebox.showinfo(title="message",message="message")
    #tkinter.messagebox.showerror(title="message",message="message")

root.geometry("600x400")#传入的是"宽x高",号是小写的英文字母x,调整窗口的大小；
root.geometry("600x400+100+200")#100,200表示的是窗口顶点，距离电脑左上角的坐标
root.title("my title")

#-----------添加标签控件，并定位
#label=Label(root)
label = Label(root,text="签名",font=("宋体",25),fg="red")
label.grid(row=0,column=0)

#------------输入框
entry=Entry(root,font=("宋体",25),fg='red')
'''第一个参数传入的就是实例化的那个root窗口对象；第二个参数可写可不写，指的是我们输入的
字体的字体样式和字体大小；第三个参数同样可写可不写，表示的是我们输入的字体的颜色。'''
#entry.grid()#只有调用grid()方法，定位后，才会真正显示这个输入框.
entry.grid(row=0,column=1)#row=0,column=1表示我们将输入框控件，放在第1行第2列的位
txt=entry.get()#适用get()获取输入框内容
#txt.focus()#使输入框获取焦点
#-----------组合框
from tkinter.ttk import *
combo=Combobox(root)
combo['values']=(1,2,3,4,5,'text')
combo.current(1)
combo.grid(row=0,column=1)
chosen=combo.get()#获取选择的组合框内容
#-----------复选框
chk=Checkbutton(root,text='chosen')
chk_state=BooleanVar()
chk_state.set(True)
chk_state.set(False)
'''
chk_state=IntVar()
chk_state.set(1)
chk_state.set(0)
'''
chk.grid(row=0,column=1)

#-----------单选框
rad_1=Radiobutton(root,text='rad_1',value=1)
rad_2=Radiobutton(root,text='rad_2',value=2,command=function)
rad_1.grid(row=2,column=0)
rad_2.grid(row=2,column=1)

selected=IntVar()#建立IntVar()类型
rad_3=Radiobutton(root,text='rad_3',value=3,variable=selected)
text=selected.get()#获取选择值

#-----------文本区
from tkinter import scrolledtext
txtFrame=scrolledtext.ScrolledText(root,width=40,height=10)#指定一个文本区的宽度和高度，否则它会占住整个窗口
txtFrame.grid(row=3,column=0)
txtFrame.insert(INSERT,'text inserted')#插入文本
txtFrame.delete(1.0,END)#全部删除

#-----------Spinbox
spin_1=Spinbox(root,from_=0,to=100,width=5)#指定输入范围值
spin_2=Spinbox(root,values=(3,8,11),width=5)#指定特定的值,只会显示3个数字即3，8，11
spin_1.grid(row=4,column=0)
spin_2.grid(row=4,column=1)

var=IntVar()
var.set(36)
spin_3=Spinbox(root,from_=0,to=100,width=5,textvariable=var)#设定默认值为36

#-----------进度条
from tkinter.ttk import Progressbar
bar=Progressbar(root,length=200)
bar['value']=70#设置进度值
bar.grid(row=5,column=0)

#改变进度条类型
#style=ttk.Style()
#Style.theme_use('default')
#Style.configure('black.Horizontal.Tprogressbar',background='black')
#bar_1=Progressbar(root,lenth=200,style='black.Horizontal.Tprogresbar')
#bar_1.grid(row=5,column=1)
'''
#-----------文本对话框
from tkinter import filedialog
file=filedialog.askopenfilename()#file存储该文件路径
files=filedialog.askopenfilenames()#files存储多个文件路径
file_1=filedialog.askopenfilename(filetypes=('text files','*.txt'))#用filetypes 参数指定文件对话框的文件类型

dir=filedialog.askdirectory()#让我们请求目录

'''


#-----------添加点击按钮
#button=Button(root,text='签名设计',font=('宋体',10),bg='orange',fg='blue')
#button.grid(row=0,column=2)

def function():
    print("print sth")
    #tkinter.messagebox.Message(master=None)
    tkinter.messagebox.showinfo(title="message",message="message")
    tkinter.messagebox.showerror(title="message",message="message")
    
    
#button_fuc=Button(root,text='button_func',font=('宋体',10),fg='blue',command=function)
#button_fuc.grid(row=2,column=0)

#-----------菜单
menu=tkinter.Menu(root)
submenu=tkinter.Menu(menu,tearoff=0)
submenu.add_command(label="open")
submenu.add_command(label="save")
submenu.add_command(label="close")
menu.add_cascade(label="file",menu=submenu)
submenu=tkinter.Menu(menu,tearoff=0)
submenu.add_command(label="copy")
submenu.add_command(label="cut")
root.config(menu=menu)



root.mainloop()## 显示窗口

