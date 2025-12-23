from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# Label
my_label = Label(text="I am a label.", font=("Arial", 24))
my_label.pack()

# There's multiple ways to set options for tkinter objects.
my_label["text"] = "Text from keyword input."
# my_label.config(text="Text from config input.")

# Button

# button_clicks = 1
def button_clicked():
    # global button_clicks
    # my_label["text"] = f"Button got clicked {button_clicks} times."
    # button_clicks += 1
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
entry = Entry(width=10)
entry.pack()

# Text box
text = Text(height=5, width=40)
# Focus makes cursor start in box.
text.focus()
# Add default text
text.insert(END, "Default text.")
# Gets current value in textbox at line 1, character 0.
print(text.get("1.0", "end"))
text.pack()

# Spinbox
def spinbox_used():
    # Gets current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbox
def checkbox_used():
    # Prints 1 if on button checked, otherwise 0
    print(checked_state.get())
# Variable to hold checked state
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()

# Radio Button
def radio_used():
    print(radio_state.get())
# Variable for which radio button is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=3)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# This must be at the end of the program.
window.mainloop()
