from tkinter import *

window = Tk() # the class for the window

# create a label widget
text1 = Label(window, text="Hello world!")

# Shoving it onto the window 
text1.pack()


# main loop to show the window repeatedly maybe
window.mainloop()