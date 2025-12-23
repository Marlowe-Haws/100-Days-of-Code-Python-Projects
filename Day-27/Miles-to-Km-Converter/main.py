from tkinter import *

# Miles to Kilometers Project Section

window = Tk()
window.title("Miles to Km Converter")
window.minsize(300, 200)
# You can add padding around edges of whole window from widgets
window.config(padx=50, pady=50)

miles_entry = Entry(width=9)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to:")
equals_label.grid(row=1, column=0)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def button_clicked():
    miles = float(miles_entry.get())
    km = round((miles * 1.60934), 2)
    km_value_label.config(text=km)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=2, column=1)

window.mainloop()

## Learning Section

# Label
# my_label = Label(text="I am a label.", font=("Arial", 24))
# You can add padding to individual widgets.
# my_label.config(padx=5, pady=5)
# You can use .place to put widgets at specific x,y coords.
# In tkinter setup, 0,0 is at top left of screen.
# my_label.place(x=100, y=200)

# You can use .grid to put widgets in defined rows/columns.
# These are all relative, there will be only as many rows/columns
# as there are widgets.
# You can't mix grid with pack though.
# my_label.grid(column=0, row=0)

# There's multiple ways to set options for tkinter objects.
# my_label["text"] = "Text from keyword input."
# my_label.config(text="Text from config input.")

# Button

# button_clicks = 1
# def button_clicked():
#     # global button_clicks
#     # my_label["text"] = f"Button got clicked {button_clicks} times."
#     # button_clicks += 1
#     my_label.config(text=input.get())
#
# button = Button(text="Click Me", command=button_clicked)
# button.config(padx=5, pady=5)
# button.grid(column=1, row=1)
#
# button2 = Button(text="I'm a second button")
# button2.config(padx=5, pady=5)
# button2.grid(column=2, row=0)
#
# # Entry
# entry = Entry(width=10)
# entry.grid(column=3, row=2)
