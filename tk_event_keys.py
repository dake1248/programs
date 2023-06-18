import tkinter as tk

root=tk.Tk()
root.geometry("600x400")
root.title("title")

def function(event):
	print("functional")

#root.bind('<keyPress>',function)
root.bind("<KeyPress-A>", function)

'''
1. KeyPress 键盘的按键被按下时激活
2. KeyRelease 键盘的按键按下后松开时激活
3. Button 点击⿏标时激活
4. ButtonRelease 点击⿏标后松开时激活
5. Motion ⿏标的光标在控件上移动时激活
6. Enter ⿏标光标进⼊控件时激活
7. Leave ⿏标光标离开控件时激活
8. MouseWheel ⿏标滑轮滚动时激活
9. FocusIn 控件获得焦点时激活，例如⿏标点击输⼊控件开始进⾏输出
10. FocusOut 控件失去焦点时激活，例如⿏标离开了输⼊框
11. Configure 控件的配置发⽣改变，例如⼤⼩变化时激活

------键盘
在Tkinter库中，常⽤的键盘事件如下。
· <KeyPress-A>：表⽰按下A键，可⽤其他字⺟键代替。
· <Alt-KeyPress-A>：表⽰同时按下Alt键和A键。
· <Control-KeyPress-A>：表⽰同时按下Control键和A键。
· <Shift-KeyPress-A>：表⽰同时按下Shift键和A键。
· <Double-KeyPress-A>：表⽰快速地按两下A键。
· <Lock-KeyPress-A>：表⽰先按下CapsLock键再按下A键。
在上述键盘事件中，还可以使⽤Alt键、Control键和Shift的组合键。例如<Alt-Control-
Shift- KeyPress-B>表⽰同时按下Alt键、Control键、Shift键和B键。其中，KeyPress
可以使⽤KeyRelease替换，表⽰当按键释放时触发事件。
输入的字母要区分大小写
-------窗口
· FocusOut：当控件失去焦点时触发。
· Map：当控件由隐藏状态变为显⽰状态时触发。
· Property：当窗体的属性被删除或改变时触发。
· Unmap：当控件由显⽰状态变为隐藏状态时触发。
· Visibility：当控件变为可视状态时触发。

'''

root.mainloop()