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

user_cards = []
comp_cards = []

for _ in range (2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

user_score = calculate_score(user_cards)
comp_score = calculate_score(comp_cards)

if comp_score == 0:
    print("Computer has a blackjack, you lose :(")
elif user_score == 0:
    print("You have a blackjack, you win :)")
print(f"{user_cards}, {user_score}")
print(f"{comp_cards}, {comp_score}")