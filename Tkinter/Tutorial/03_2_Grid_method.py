'''
***Python Tkinter grid() method***

The grid() geometry manager organizes the widgets in the tabular form. We can specify the 
rows and columns as the options in the method call. We can also specify the column span (
width) or rowspan(height) of a widget.

This is a more organized way to place the widgets to the python application. The syntax to
 use the grid() is given below.

Syntax:widget.grid(options)  

A list of possible options that can be passed inside the grid() method is given below.

1.Column
The column number in which the widget is to be placed. The leftmost column is represented by 0.
2.Columnspan
The width of the widget. It represents the number of columns up to which, the column is expanded.
3.ipadx, ipady
It represents the number of pixels to pad the widget inside the widget's border.
4.padx, pady
It represents the number of pixels to pad the widget outside the widget's border.
5.row
The row number in which the widget is to be placed. The topmost row is represented by 0.
6.rowspan
The height of the widget, i.e. the number of the row up to which the widget is expanded.
7.Sticky
If the cell is larger than a widget, then sticky is used to specify the position of the 
widget inside the cell. It may be the concatenation of the sticky letters representing 
the position of the widget. It may be N, E, W, S, NE, NW, NS, EW, ES.
'''

from tkinter import *
root=Tk()

id=Label(root,text="User Id : ")
id.grid(row=0,column=0)

e1=Entry(root)
e1.grid(row=0,column=1)

password=Label(root,text="Password : ")
password.grid(row=1,column=0)

e2=Entry(root)
e2.grid(row=1,column=1)

btn=Button(root,text="Log in")
btn.grid(row=4,column=0)

root.mainloop()