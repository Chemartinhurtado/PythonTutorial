import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def blackjack():
    your_cards = []
    computer_hand = []

    def player_draw_card():
        your_cards.append(random.choice(cards))

    def first_draw():
        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's first card: {computer_hand[0]}")
        your_cards_value = sum(your_cards)
        # print(your_cards_value)

    input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")


    first_draw()

    drawing = True

    want_continue = input("Type 'y' to continue or 'n' to pass: ")
    while drawing:
        player_draw_card()
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's first card: {computer_hand[0]}")
        want_continue = input("Type 'y' to continue or 'n' to pass: ")
        if want_continue == 'n':
            drawing = False


    blackjack()


blackjack()

