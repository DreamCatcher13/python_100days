import art, random

def deal_card():
    """Return a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Return the score from cards"""
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0 # blackjack
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(user_score, comp_score):
    """To compare scores"""
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose :("
    if comp_score == 0:
        return "Computer has a blackjack, you lose :("
    elif user_score == comp_score:
        return "Draw"
    elif user_score == 0:
        return  "You have a blackjack, you win :)"
    elif user_score > 21:
        return "You went over. You lose :("
    elif comp_score > 21:
        return "Computer went over. You win :)"
    elif user_score > comp_score:
        return "You win :)"
    else:
        return "You lose :("
    

def play_game():
    print(art.jack)

    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    # user plays
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first cards: {comp_cards[0]}")

        if comp_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # computer plays
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {comp_cards}, final_score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    play_game()