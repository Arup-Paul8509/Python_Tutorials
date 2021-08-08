'''
***Python Tkinter place() method***

The place() geometry manager organizes the widgets to the specific x and y coordinates.

Syntax : widget.place(options)  

A list of possible options is given below.

1.Anchor: It represents the exact position of the widget within the container. The default 
    value (direction) is NW (the upper left corner)
2.bordermode: The default value of the border type is INSIDE that refers to ignore the 
    parent's inside the border. The other option is OUTSIDE.
3.height, width: It refers to the height and width in pixels.
4.relheight, relwidth: It is represented as the float between 0.0 and 1.0 indicating the 
    fraction of the parent's height and width.
5.relx, rely: It is represented as the float between 0.0 and 1.0 that is the offset in 
    the horizontal and vertical direction.
6.x, y: It refers to the horizontal and vertical offset in the pixels.
'''

from tkinter import *  
top = Tk()  
top.geometry("300x300")  
name = Label(top, text = "Name")
name.place(x = 30,y = 50)  
email = Label(top, text = "Email")
email.place(x = 30, y = 90)  
password = Label(top, text = "Password")
password.place(x = 30, y = 130)  
e1 = Entry(top)
e1.place(x = 95, y = 50)  
e2 = Entry(top)
e2.place(x = 95, y = 90)  
e3 = Entry(top)
e3.place(x = 95, y = 130)  
btn=Button(top,text="Submit")
btn.place(x=110,y=170)
top.mainloop() 