'''
Python provides the standard library Tkinter for creating the graphical user interface for desktop based applications.

Developing desktop based applications with python Tkinter is not a complex task. An empty Tkinter top-level window can 
be created by using the following steps.

1.import the Tkinter module.
2.Create the main application window.
3.Add the widgets like labels, buttons, frames, etc. to the window.
4.Call the main event loop so that the actions can take place on the user's computer screen.
'''


from tkinter import *
#creating the application main window.  
root=Tk()
#Entering the event main loop  
root.mainloop()