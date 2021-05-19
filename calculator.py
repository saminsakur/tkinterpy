from tkinter import *


window = Tk() # the class for the window

# sets window tile
window.title("Simple Calculator")

#Create a entry widget 
e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=15, pady=10) # Columnspan used to span over comuns heres's 3
# e.insert(0, "")

# function for button_add command of button
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


# function for the clear button
def clear():
    e.delete(0, END)


# The buttons for calculator
# Calculator buttons
button_1 = Button(window, text=1, padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text=2, padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text=3, padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text=4, padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text=5, padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text=6, padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text=7, padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text=8, padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text=9, padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text=0, padx=40, pady=20, command=lambda: button_click(0))
button_additon = Button(window, text="+", padx=39, pady=20, command=lambda: add())
button_equal = Button(window, text="=", padx=91, pady=20, command=lambda: equal())
button_clear = Button(window, text="Clear", padx=79, pady=20, command=clear)

######### put the buttons on the screen
######### these gets to third ond row
button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)

######### these gets to third ond row
button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

######### these gets to third ond row
button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_additon.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)



# main loop to show the window repeatedly maybe
window.mainloop()