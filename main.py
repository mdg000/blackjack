# 100 Days of Code 
# Blackjack

import random
from art import logo
from replit import clear

# deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# game variables
player_hand = []
dealer_hand = []
hand = []
player_score = 0
dealer_score = 0
player_won = False
dealer_won = False
game_over = False

# functions

# deals cards to player
def deal(num_cards):
  for card in range(num_cards):
    hand.append(random.choice(cards))
  return hand

# calculates score of combined cards
def check_score(hand):
  score = 0
  for i in hand:
    score += i
  return score

# prints ending result based off of scores
def check_winner(score_1, score_2):
  if player_score > 21:
    return "You went over. You lost."
  elif dealer_score > 21:
    return "Dealer went over. You win."
  elif dealer_score == 21:
    return "You lose, dealer has a Blackjack."
  elif player_score == 21:
    return "Win with a Blackjack."
  elif player_score > dealer_score and player_score < 21:
    return "You win."
  elif player_score < dealer_score and dealer_score < 21:
    return "You lose."
  elif player_score == dealer_score:
    return "Draw."

# game begins
begin = input("Do you want to play a game of Black? Type 'y or 'n': ")

if begin == "y":
  clear()
  print(logo)
  game_loop = True

# setting up first hands
player_hand = deal(num_cards=2)
player_score = check_score(player_hand)
hand = []
dealer_hand = deal(num_cards=2)
dealer_score = check_score(dealer_hand)

print(f"\tYour cards: {player_hand}, current score: {player_score}")
print(f"\tDealer's first card: {dealer_hand[0]}")

# main game loop
while game_loop:
  
  if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':

    hand = player_hand
    player_hand = deal(num_cards=1)
    player_score = check_score(player_hand)

    hand = dealer_hand

    while dealer_score <= 16:
      dealer_hand = deal(num_cards=1)
      dealer_score = check_score(dealer_hand)

    print(f"\tYour cards: {player_hand}, current score: {player_score}")
    print(f"\tDealer's first hand: {dealer_hand}, current score: {dealer_score}")

    if dealer_score >= 21 or player_score >= 21:
      game_over = True

  # final card 
  else:
    print(f"\tYour final hand: {player_hand}, final score: {player_score}")

    while dealer_score <= 16:
      dealer_hand = deal(num_cards=1)
      dealer_score = check_score(dealer_hand)

    print(f"\tDealer's final hand: {dealer_hand}, final score: {dealer_score}")

    game_over = True
  
  if game_over == True:
    game_loop = False
    print(check_winner(score_1=player_score, score_2=dealer_score))
