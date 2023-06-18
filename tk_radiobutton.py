import tkinter as tk

def show_selection():
	print("selection is:",var.get())
	
root=tk.Tk()

var=tk.StringVar()

radiobutton_1=tk.Radiobutton(root,text='option_1',variable=var,value=1,command=show_selection)
radiobutton_2=tk.Radiobutton(root,text='option_2',variable=var,value=2,command=show_selection)

radiobutton_1.pack()
radiobutton_2.pack()


root.mainloop()