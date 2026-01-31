from tkinter import *
import pandas as pd
import random
import os

LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

# You can use this to flip the card after a delay,
# but I liked the user choosing when to flip the card.
# You'd also need to adjust the function for that purpose,
# and put this inside the new_card function.
# Also, putting it in a variable would contain it,
# so it isn't counting between function calls.
# flip_timer = window.after(3000, func=unknown)

# First check if we've run the program before,
# and load from that file if so.
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')

vocab = df.to_dict(orient='records')

# You can use next(iter(iterable)) to grab the first item
# from an iterable using a generator instead of saving to memory.
# If you save this to a variable and call next again, it will
# give you the next item.
# You can also use: from itertools import islice,
# then call next(islice(iterable, index, None))
# to grab an item at a specific index.
# The first argument 'index', tells it where to start,
# the second argument 'None' tells it where to stop,
# in this case, it won't stop until you hit the end.
# If you provide only 1 argument (leave out None-- the stop index),
# it will be treated as the stop argument instead.
# There's also an optional final argument: islice(iterable, start, stop, step).
# Note, in both cases, calling next will 'consume' the item,
# you can't access it again after the first call.

# unlearned = vocab
# current_card = random.choice(unlearned)
# card_iter = iter(current_card)
# f_language = next(card_iter)
# f_word = current_card[f_language]
# b_language = next(card_iter)
# b_word = current_card[b_language]

# Initialize first card.
unlearned = vocab
current_card = random.choice(unlearned)

# Track whether the user knew the answer or not before getting new card.
# Start with True, so the first card isn't removed.
is_flipped = True

# We'll access globals and remove cards that were known,
# then find next card.
def next_card():
    global is_flipped, unlearned, current_card
    if not is_flipped:
        unlearned.remove(current_card)
    # Check if unlearned isn't empty first.
    if unlearned:
        # The unpacking method is easier than the iter approach here.
        current_card = random.choice(unlearned)
        f_language, b_language = current_card.keys()
        canvas.itemconfig(back_lang_canv, text=b_language)
        canvas.itemconfig(back_word_canv, text=current_card[b_language])
        canvas.itemconfig(front_lang_canv, text=f_language)
        canvas.itemconfig(front_word_canv, text=current_card[f_language])
        canvas.tag_raise("front")
        is_flipped = False
    # If it's empty, then display final message and delete file.
    else:
        canvas.itemconfig(front_lang_canv, text="Congratulations!\n All words learned!")
        canvas.itemconfig(front_word_canv, text="Progress reset.")
        canvas.tag_raise("front")
        wrong_button.config(state="disabled")
        correct_button.config(state="disabled")
        file_path = "data/words_to_learn.csv"
        # For safety, make sure file exists before deleting.
        if os.path.exists(file_path):
            os.remove(file_path)

# I chose to add everything in the next_card() function,
# then simply reveal the back with this function.
def unknown():
    global is_flipped
    canvas.tag_raise("back")
    is_flipped = True

# This is a function to save unlearned vocab upon exitting.
def save_and_exit():
    global unlearned
    # Check if unlearned isn't empty first.
    if unlearned:
        new_data = pd.DataFrame(unlearned)
        new_data.to_csv('data/words_to_learn.csv', index=False)
    window.destroy()

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# The order in which you place objects on a canvas determines
# which is placed on top, starting from the bottom up.
# If you need to move one up or down afterward,
# use .tag_raise(item_id) or .tag_lower(item_id)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img_canv = canvas.create_image(0, 0, anchor=NW, image=back_image, tags="back")
back_lang_canv = canvas.create_text(400, 150, text="", fill="white", font=LANGUAGE_FONT, tags="back")
back_word_canv = canvas.create_text(400, 263, text="", fill="white", font=WORD_FONT, tags="back")
front_img_canv = canvas.create_image(0, 0, image=front_image, anchor=NW, tags="front")
front_lang_canv = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT, tags="front")
front_word_canv = canvas.create_text(400, 263, text="", font=WORD_FONT, tags="front")
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(window, image=wrong_image, highlightthickness=0, command=unknown)
wrong_button.grid(row=1, column=0)

correct_button = Button(window, image=correct_image, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=1)

# Draw the first card.
next_card()

# We can have the program save the unlearned vocab right before the user exits.
window.protocol("WM_DELETE_WINDOW", save_and_exit)

window.mainloop()
