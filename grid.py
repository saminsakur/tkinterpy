from tkinter import *


window = Tk() # the class for the window
# function to exit:
def exit():
    window.destroy()

# create a label widget and gridding 
Label(window, text="Hello world!").grid(row=0, column=0)
Label(window, text="My name is Samin Sakur").grid(row=1, column=1)

# Create a buton to exit:
Button(window, width=12, command=exit, bg="red", text="Close", fg="black").grid(row=3, column=0)

# main loop to show the window repeatedly maybe
window.mainloop()