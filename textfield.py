from tkinter import *


window = Tk() # the class for the window

# ses window tile
window.title("textfield.py")


# function to exit:
def exit():
    window.destroy()

# function sayHello for myButton:
def sayHello():
    Label(window, text="Hello, " + e.get()).pack()
# Create a Label
Label(window, text="Enter your name")

#Create a entry widget 
e = Entry(window, width=50)
e.pack()

# Create a submit button
myButton = Button(window, text="SUBMIT", command=sayHello)
myButton.pack()

# Create a buton to exit:
Button(window, width=12, command=exit, bg="red", text="Close", fg="black").pack() #.grid(row=0, column=0)

# main loop to show the window repeatedly maybe
window.mainloop()