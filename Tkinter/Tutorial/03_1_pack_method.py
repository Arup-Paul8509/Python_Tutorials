'''
***Python Tkinter pack() method***


The pack() widget is used to organize widget in the block. The positions widgets added to 
the python application using the pack() method can be controlled by using the various options 
specified in the method call.

However, the controls are less and widgets are generally added in the less organized manner.

The syntax to use the pack() is given below.

syntax : widget.pack(options)  

A list of possible options that can be passed in pack() is given below.

1.expand: If the expand is set to true, the widget expands to fill any space.
2.Fill: By default, the fill is set to NONE. However, we can set it to X or Y to determine whether 
the widget contains any extra space.
3.side: it represents the side of the parent to which the widget is to be placed on the window.
'''
from tkinter import *
root=Tk()

b1=Button(root,text="Red",fg="Red")
b1.pack(side=TOP)

b1=Button(root,text="Green",fg="Green")
b1.pack(side=BOTTOM)

b1=Button(root,text="Blue",fg="Blue")
b1.pack(side=LEFT)

b1=Button(root,text="Pink",fg="Pink")
b1.pack(side=RIGHT)

root.mainloop()