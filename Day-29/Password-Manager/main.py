from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip
import json


# --------------------------- SEARCH FUNCTION ------------------------------ #
def search():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "Database is empty.")
    else:
        try:
            messagebox.showinfo(f"{website}", f"Email/Username: {data[website]['name']}"
                                              f"\nPassword: {data[website]['password']}")
        except KeyError:
            messagebox.showerror("Error", f"Website: {website} not found in database.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entries():
    website_entry.delete(0, END)
    name_entry.delete(0, END)
    name_entry.insert(END, "@gmail.com")
    password_entry.delete(0, END)

def add_password():
    website = website_entry.get()
    name = name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "name": name,
            "password": password,
        }
    }

    if not website or not name or not password:
        messagebox.showerror("Error", "Please fill all the fields.")
    else:
        confirmed = messagebox.askokcancel(title="Entry Confirmation", message=f"Website: {website}\n\nUsername/Email: "
                                                                               f"{name}\n\nPassword: {password}\n\n "
                                                                               f"Confirm Entry?")

        if confirmed:
            try:
                with open("passwords.json", "r") as f:
                    # Read old data.
                    data = json.load(f)
                    # Update the data.
                    data.update(new_data)

            except FileNotFoundError:
                # If no existing file, write a new one.
                with open("passwords.json", "w") as f:
                    json.dump(new_data, f, indent=4)

            else:
                with open("passwords.json", "w") as f:
                    # Write the new data.
                    json.dump(data, f, indent=4)

            finally:
                clear_entries()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
POOL = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    password_entry.delete(0, END)
    length = secrets.choice([16, 17, 18])
    generated_password = "".join(secrets.choice(POOL) for i in range(length))
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="white")

frame = Frame(window, bg="white")
frame.grid(column=0, row=0, padx=50, pady=50)

logo = PhotoImage(file="logo.png")

canvas = Canvas(frame, width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(frame, text="Website:", bg="white")
website_label.grid(column=0, row=1, padx=1, pady=1, sticky=E)

name_label = Label(frame, text="Email/Username:", bg="white")
name_label.grid(column=0, row=2, padx=1, pady=1, sticky=E)

password_label = Label(frame, text="Password:", bg="white")
password_label.grid(column=0, row=3, padx=1, pady=1, sticky=E)

website_entry = Entry(frame, width=32, relief="solid")
website_entry.grid(column=1, row=1, padx=3, pady=1)
website_entry.focus()

name_entry = Entry(frame, width=51, relief="solid")
name_entry.grid(column=1, row=2, columnspan=2, padx=1, pady=1)
name_entry.insert(END, "@gmail.com")

password_entry = Entry(frame, width=32, relief="solid")
password_entry.grid(column=1, row=3, padx=3, pady=1)

generate_button = Button(frame, text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3, pady=1, padx=3, sticky=W)

add_button = Button(frame, text="Add", width=43, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, padx=1, pady=1)

search_button = Button(frame, text="Search", width=14, command=search)
search_button.grid(column=2, row=1, pady=1, padx=3, sticky=W)

window.mainloop()

# There's a built-in json library with:
# json.dump() for writing
# json.load() for reading
# json.update for updating
