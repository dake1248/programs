import tkinter as tk

def show_selection(event):
	selection=event.widget.curselection()
	print("selection is:",event.widget.get(selection))
	
root=tk.Tk()

listbox=tk.Listbox(root)
listbox.insert("end","option_1")
listbox.insert("end","option_2")
listbox.bind("<<ListboxSelect>>",show_selection)

listbox.pack()

root.mainloop()