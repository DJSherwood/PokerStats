'''
7-Card Stud is a poker game where each player has 7 cards.
3 are down
4 are up
The order of play is
    1. Card down, Card down, Card up, Bet
    2. Card up, Bet
    5. Card up, Bet
    6. Card up, Bet
    6. Card down, Bet

This script mimics the game.
'''
import shuffle_cards as sc
import player as p

# create a deck - view cards with created_deck.mycardset
created_deck = sc.ShuffleCards()
# shuffle the new deck - view cards with created_deck.mycardset
created_deck.shuffle()
# create 4 players
p1, p2, p3, p4 = p.player(), p.player(), p.player(), p.player()
# deal 2 cards down and 1 card up to every player
# round 1
p1.receive_hidden(created_deck.popCard())
p2.receive_hidden(created_deck.popCard())
p3.receive_hidden(created_deck.popCard())
p4.receive_hidden(created_deck.popCard())
# round 2
p1.receive_hidden(created_deck.popCard())
p2.receive_hidden(created_deck.popCard())
p3.receive_hidden(created_deck.popCard())
p4.receive_hidden(created_deck.popCard())
# round 3
p1.receive_shown(created_deck.popCard())
p2.receive_shown(created_deck.popCard())
p3.receive_shown(created_deck.popCard())
p4.receive_shown(created_deck.popCard())
# evaluate ?
