import tkinter as tk

window=tk.Tk()
window.geometry("600x400")
window.title("title")

def function_key(event):
	print("key motivated:",event.x,event.y)

def function(event):
	print("button-left clicked")

def function_2(event):
	print("button-middle clicked")

def function_3(event):
	print("button-right clicked")

label=tk.Label(window,text="LABEL")
label.pack()

label_2=tk.Label(window,text="LABEL_2")
label_2.pack()

label.bind("<Button-1>",function)
label.bind("<Button-2>",function_2)

label_2.bind("<MouseWheel>",function_key)

window.bind("<Button-3>",function_3)
window.bind("<KeyPress-a>",function_3)
window.bind("<KeyPress-B>",function_key)

'''
-----鼠标
· <Button-1>：表⽰按下鼠标左键，⽽<Button-2>表⽰按下鼠标中键，<Button-3>
表⽰按下⿏标右键。
· <ButtonPress-l>：表⽰按下鼠标左键，与<Button-l>相同。
· <ButtonRelease-l>：表⽰释放鼠标左键。
· <Bl-Motion>：表⽰按住鼠标左键并移动。
· <Double-Button-l>：表⽰双击⿏标左键。
· <Enter>：表鼠标指针进⼊某⼀组件区域。
· <Leave>：表鼠标指针离开某⼀组件区域。
· <MouseWheel>：表鼠标滑轮滚动动作。
在上述⿏标事件中，数字“1”可以替换成2或3。其中数字“2”表鼠标中键，数字
“3”表鼠标右键。
'''

window.mainloop()
