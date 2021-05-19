from tkinter import *


window = Tk() # the class for the window

# function to exit:
def exit():
    window.destroy()


################
myButton = Button(window, text="Click me")
myButton.pack()

# Create a buton to exit:
Button(window, width=12, command=exit, bg="red", text="Close", fg="black").pack() #.grid(row=0, column=0)

# main loop to show the window repeatedly maybe
window.mainloop()