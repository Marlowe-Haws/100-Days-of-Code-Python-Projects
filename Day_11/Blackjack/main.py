import art
import random
import time

# Initialize deck list.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to add a random card to a hand.
def add_card(hand, deck):
    """Input 2 lists. An item will be randomly selected from list 2 and added to list 1."""
    new_card = random.choice(deck)
    hand.append(new_card)

# Function to flip value of aces.
def flip_ace(hand_list, old_ace, new_ace):
    """Input the current hand, 11 for the old ace value, and 1 for the new ace value; the updated hand will be returned."""
    if old_ace in hand_list:
        index = hand_list.index(old_ace)
        hand_list[index] = new_ace
    return hand_list

# Main loop. Handles user input.
while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if play == 'n':
        print("Goodbye!")
        exit()
    elif play == 'y':
        print("\n" * 50)
        print(art.logo)
    else:
        print("Please only enter 'y' or 'n'.")
        continue

# Initialize hands.
    user_cards = random.choices(cards, k=2)
    dealer_cards = random.choices(cards, k=2)

# Check if two aces in starting hands and flip one if so.
    if sum(user_cards) == 22:
        user_cards[0] = 1
    if sum(dealer_cards) == 22:
        dealer_cards[0] = 1

# Bigger inner loop here.
# Check whether the user wants to hit or stand and handle inputs.
# Break if the user busts or continue with the dealer's option.
# For both, check if the sum of a hand is greater than 21, then flip any ace to 1 and recheck.
# Dealer will always hit if under 17, break if bust, or stand if not.
# Finally, compare scores, print the outcome, then break (back to the main loop).
    while True:
        hit_or_stand = input(f"Your hand: {user_cards}, current score: {sum(user_cards)}.\nDealer's first card: {dealer_cards[0]}.\nType 'h' to hit, or 's' to stand: ").strip().lower()
        if hit_or_stand == 'h':
            add_card(user_cards, cards)
            if sum(user_cards) > 21:
                if 11 in user_cards:
                    flip_ace(user_cards, 11, 1)
            if sum(user_cards) > 21:
                print(f"Your hand: {user_cards}, current score: {sum(user_cards)}.")
                print("Bust! You lose.")
                break
            continue
        elif hit_or_stand == 's':
            while sum(dealer_cards) < 17:
                print(f"Dealer's hand: {dealer_cards}, current score: {sum(dealer_cards)}.")
                add_card(dealer_cards, cards)
                print("Dealer hits.")
                time.sleep(1.5)
                if sum(dealer_cards) > 21:
                    if 11 in dealer_cards:
                        flip_ace(dealer_cards, 11, 1)
                if sum(dealer_cards) > 21:
                    print(f"Dealer's hand: {dealer_cards}, current score: {sum(dealer_cards)}.")
                    print("Dealer busts! You win.")
                    break
            if sum(dealer_cards) > 21:
                break
            print(f"Dealer's hand: {dealer_cards}, current score: {sum(dealer_cards)}.")
            print("Dealer stands.")
            time.sleep(1.5)
        else:
            print("Please only enter 'h' or 's'.")
            continue
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}\nDealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}.")
        if sum(user_cards) == sum(dealer_cards):
            print("It's a draw!")
        elif sum(user_cards) > sum(dealer_cards):
            print("You win!")
        else:
            print("You lose!")
        break
      
