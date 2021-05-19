from tkinter import *

window = Tk() # the class for the window

# create a label widget
text1 = Label(window, text="Hello world!")
text2 = Label(window, text="My name is Samin Sakur")
text3 = Label(window, text="I'm a student of class 7")

# gridding labels
text1.grid(row=0, column=0)
text2.grid(row=1, column=1)
text3.grid(row=2, column=3)

# main loop to show the window repeatedly maybe
window.mainloop()