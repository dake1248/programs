
Python Tkinter事件处理 - 知乎https://zhuanlan.zhihu.com/p/358467263?utm_id=0

1. Tkinter事件绑定语法
将事件与控件绑定，需要使⽤bind⽅法，该⽅法有两个参数
1. sequence，⼀个字符串，描述所监听事件的详细信息，格式为<MODIFIERMODIFIER-
TYPE-DETAIL>
2. func 函数，事件被触发后需要执⾏的函数，这个函数不是可以随便定义的，它只有
⼀个参数envent
下⾯的程序演⽰如何为Label控件绑定⿏标点击事件
from tkinter import *
window = Tk()
def mouseClick(event):
    print("点击")

label = Label(window, text="点击我")
label.pack()
label.bind("<Button>", mouseClick)
window.mainloop()
运⾏程序，在Label上点击，控制台会输出“点击⿏标”


2. 事件类型
不同的事件类型，对应着不同的操作，下⾯是Tkinter事件类型的⼀部分
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
-----鼠标
· <Button-1>：表⽰按下⿏标左键，⽽<Button-2>表⽰按下⿏标中键，<Button-3>
表⽰按下⿏标右键。
· <ButtonPress-l>：表⽰按下⿏标左键，与<Button-l>相同。
· <ButtonRelease-l>：表⽰释放⿏标左键。
· <Bl-Motion>：表⽰按住⿏标左键并移动。
· <Double-Button-l>：表⽰双击⿏标左键。
· <Enter>：表⽰⿏标指针进⼊某⼀组件区域。
· <Leave>：表⽰⿏标指针离开某⼀组件区域。
· <MouseWheel>：表⽰⿏标滑轮滚动动作。
在上述⿏标事件中，数字“1”可以替换成2或3。其中数字“2”表⽰⿏标中键，数字
“3”表⽰⿏标右键。
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

3. 事件修饰符
事件装饰符可以修改事件激活的条件，例如要求事件发⽣时，⽐如按下某个按钮才成⽴
1. Control 事件发⽣时需按下Control按钮
2. Alt 事件发⽣时需按下Alt按钮
3. Shift 事件发⽣时需按下Shift按钮
4. Lock 事件发⽣时需处于⼤写锁定状态

4. 事件详情
detail部分，可以对事件做出更详细的规定，例如点击⿏标事件，可以指定是⿏标左
键，还是右键。
label.bind("<Button-1>", mouseClick) # 左键
label.bind("<Button-3>", mouseClick) # 右键
window.bind("<KeyPress-p>", key)
只有按下p按钮时，才会触发KeyPress事件。
5. 事件对象
事件触发后执⾏的函数，只有事件对象⼀个参数，事件对象包含了如下信息
1. keysym 触发事件的键盘按钮
2. keycode 触发基于键盘的事件的键的代码
3. button 返回触发基于⿏标的事件的⿏标按钮（1-5）
4. x, y 事件所在位置的x,y坐标
5. width, height 关联控件的宽与高