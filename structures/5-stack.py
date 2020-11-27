

all_cards = ['2♦️', '5♥️', '6♣️', 'K♠️', 'A♠️', '3♥️', '2♠️']
print("This is your current stack: ", all_cards)



print("Adding 9♣️")
all_cards.append('9♣️')
print("This is your current stack: ", all_cards)



card = all_cards.pop()
print("Deal this card: ", card)
print("This is your current stack: ", all_cards)