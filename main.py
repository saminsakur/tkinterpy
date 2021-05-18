from tkinter import * # imports tkinter

#key down function
def click():
    entered_text = textentry1.get() # this will get the values from the text box
    output.delete(0.0, END)
    try:
        definition = my_dictionary[entered_text]
    except:
        definition = "Sorry there is no word found to your match, please try again."
    output.insert(END, definition)

window = Tk()

window.title("My cool interface") # sets the window title
window.configure(background="black") ## sets full window background to black

####photo
photo1 = PhotoImage(file="Images\\icon.png") # path of the image
Label (window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

# create label
label1 = Label (window, text="Hello, write anything:", bg="black", fg="white", font="none 12 bold")
label1.grid(row=1, column=0, sticky=W)

# create a text entry
textentry1 = Entry(window, width=20, bg="white")
textentry1.grid(row=2, column=0, sticky=W)
# create a submit button
butn1 = Button(window, text="SUBMIT", width=6, command=click)
butn1.grid(row=3, column=0, sticky=W)

# another label
label2 = Label(window, text="\n Definition", bg="black", fg="white", font="none 12 bold")
label2.grid(column=0, row=4, sticky=W)

#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#a simple dictionary
my_dictionary = {
    'ml': "machine learning, learning algorithm of that kind of stuff like human",
    "bug": "A piece of code that causes a problem to fail",
    "algorith": "Step by step instructions to complete a task"
}
###############
window.mainloop() # main loop to run tk interface repeatedly