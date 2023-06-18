from tkintertable import TableCanvas, TableModel
from tkinter import *
import random
import tkinter
#from collections import OrderedDict

class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x500+200+100')
        self.main.title('Test')

        label=tkinter.Label(text="LABEL")
        label.pack()

        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)

        data = {
            'row1': {'col1':'', 'col2': '状态1', 'col3': '状态2', 'col4': '状态3', 'col5': '状态4'},
            'row2': {'col1': '眉毛', 'col2': 'b1', 'col3': 'b2', 'col4': 'b3', 'col5': '/'},
            'row3': {'col1': '眨眼', 'col2': 'e1', 'col3': 'e2', 'col4': 'e3', 'col5': '/'},
            'row4': {'col1': '嘴巴', 'col2': 'm1', 'col3': 'm2', 'col4': '/', 'col5': '/'},
            'row5': {'col1': '头部姿态', 'col2': 'h1', 'col3': 'h2', 'col4': 'h3', 'col5': 'h4'},
            # 'row5': {'头部姿态': "", 'col2': 108.79, 'label': '2'}
            }
        
        table = TableCanvas(f,data=data)
        
        '''
        #---------------set table values---------------
        data=table.model.data
        table.model.setValueAt(123,3,4)
        table.model.setValueAt('hahaha',2,4)
        table.model.setValueAt(repr(type('haha')),1,4)
        '''

        print (table.model.columnNames)
        table.show()

        #--------------insert rows and columns
        for i in range(3):        
            table.addColumn('add%d'%i)
        for i in range(4):
            table.addRow()
        print (table.model.columnNames)

        '''
        #add with automatic key
table.addRow()
#add with named key, other keyword arguments are interpreted as column values
table.addRow(keyname, label='abc')
#same as above with dict as column data
table.addRow(keyname, **{'label'='abc'})
table.addColumn(colname)
#delete Rows
table.deleteRows(range(0,2))
#delete Column
table.deleteColumn(colIndex)
------------order--------------
#by column name
table.sortTable(columnName='label')
#by column index
table.sortTable(columnIndex=1) 
        
        '''

        return

app=TestApp()
app.mainloop()
