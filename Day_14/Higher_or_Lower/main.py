import art
from game_data import data
import random
import copy

# A function to select a random option from the game_data list.
# Save the option, remove it from the list to prevent reuse, and return it.
# First filter to see if no options remain, which will return False.
def select_option(my_list):
    if not my_list:
        return False
    index = random.randint(0, len(my_list) - 1)
    selected_option = my_list[index]
    del my_list[index]
    return selected_option

# A function to display the comparison.
def comparison():
    print(f"A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}.")
    print(art.vs)
    print(f"B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}.")

# A function to get the user's answer and catch exceptions.
def get_user_answer():
    """Requests user input, filters out invalid inputs, and returns a or b"""
    while True:
        user_response = input("\nWho has more followers on Instagram? Type 'A' or 'B': ").strip().lower()
        if not user_response.isalpha():
            print("Please only enter 'A' or 'B'.")
            continue
        if user_response == "a":
            return "a"
        elif user_response == "b":
            return "b"
        else:
            print("Please only enter 'A' or 'B'.")

# A function to test whether the user's answer is correct.
def check_answer(user_str, a_dict, b_dict):
    """Accepts 3 arguments: user's answer, option A, and option B.
    Returns True if the user's answer is correct, False otherwise."""
    a_followers = int(a_dict["follower_count"])
    b_followers = int(b_dict["follower_count"])
    if a_followers > b_followers:
        return user_str == "a"
    else:
        return user_str == "b"

# A function to cheat for testing purposes.
def cheat_result(a_dict, b_dict):
    a_followers = int(a_dict["follower_count"])
    b_followers = int(b_dict["follower_count"])
    if a_followers > b_followers:
        return "a"
    else:
        return "b"

# A function to ask the user if they want to play again.
def play_again():
    while True:
        keep_playing = input("Do you want to play again? Type 'y' or 'n': ").strip().lower()
        if not keep_playing.isalpha():
            print("Please only enter 'y' or 'n'.")
            continue
        elif keep_playing == "y":
            break
        elif keep_playing == "n":
            print("Goodbye!")
            exit()
        else:
            print("Please only enter 'y' or 'n'.")
            continue

# Initialize the score, high score, and data_copy for the first run.
score = 0
data_copy = [1]
high_score = 0

# Main game loop.
# It will conclude when options run out.
# For the first run and restarts (score = 0), it will regenerate the data_copy and initialize the first options.
# Upon restarting, a high score will be saved and updated on subsequent runs.
while len(data_copy) > 0:
    if score == 0:
        data_copy = copy.deepcopy(data)
        option_a = select_option(data_copy)
        option_b = select_option(data_copy)
    print("\n" * 50)
    print(art.logo)
    if high_score > 0:
        print(f"High score: {high_score}.")
    #print(cheat_result(option_a, option_b))
    if score > 0:
        print(f"That's correct! Current score: {score}.\nNext question.\n")
    else:
        print("Welcome to Higher or Lower!\nCompare option A to option B.\n")
    comparison()
    user_answer = get_user_answer()
    check_result = check_answer(user_answer, option_a, option_b)
    if check_result:
        score += 1
        option_a = option_b
        option_b = select_option(data_copy)
    else:
        print(f"\nSorry, that was wrong! Game over.\nFinal score: {score}.")
        high_score = max(score, high_score)
        score = 0
        play_again()
    if score == 48:
        print(f"\nYou answered every question correctly! Incredible!\nFinal score: {score}.")
        high_score = 48
        score = 0
        data_copy = [1]
        play_again()
