from tkintertable import TableCanvas, TableModel
import tkinter as tk
root=tk.Tk()
label=tk.Label(text="LABEL")
label.pack()
tframe = tk.Frame(root)
tframe.pack()

table = TableCanvas(tframe)
table.show()
model = TableModel()
table = TableCanvas(tframe, model=model)
table = TableCanvas(tframe, model,
            cellwidth=60, cellbackgr='#e3f698',
            thefont=('Arial',12),rowheight=38, rowheaderwidth=30,
            rowselectedcolor='yellow', editable=True)

#data=table.model.data
table.model.setValueAt('123',0,1)
#table.model.setValueAt('hahaha',1,2)
#table.model.setValueAt(repr(type('haha')),1,3)

root.mainloop()
