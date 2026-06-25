from os import name

import art
import game_data
import random

def format_information(selection):
    '''Function to change the random selected list to clear information'''
    formatted_information = selection ["name"]
    formatted_information += ", a "
    formatted_information += selection ["description"]
    formatted_information += ", from "
    formatted_information += selection ["country"]
    return formatted_information

def compare_followers(user_selection, other_choice):
    user_selection_followers = user_selection["follower_count"]
    other_choice_followers = other_choice["follower_count"]
    if user_selection_followers < other_choice_followers:
        return "Sorry, that's wrong. Final score:"

    elif user_selection_followers > other_choice_followers:
        return "You're right! Current score:"


game_over = False

def game():
    print(art.logo)
    a = random.choice(game_data.data)
    while not game_over :

        b = random.choice(game_data.data)

        #Debug to know which one is higher
        print(a["follower_count"])
        print(b["follower_count"])

        print(f"Compare A: {format_information(a)}")

        print(art.vs)

        print(f"Against B: {format_information(b)}")

        choice = input("Who has more followers? Type 'A' or 'B': ")

        print(art.logo)
        if choice == "A":
            print("\n" * 20)
            print(art.logo)
            print(compare_followers(a, b))
        elif choice == "B":
            print("\n" * 20)
            print(art.logo)
            print(compare_followers(b, a))





game()