import random
from art import logo

def deal_card(cards):
  return random.choice(cards)

def calculate_score(list):
  if  len(list) ==2 and sum(list) ==21:
    return 0
  if sum(list) > 21 and 11 in list:
    list.remove(11)
    list.append(1)
  return sum(list)

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def game():
  print(logo)
  user_cards = []
  computer_cards = []
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  is_gameover = False

  for _ in range(2):
    t = deal_card(cards)
    cards.remove(t)
    user_cards.append(t)
    
    t = deal_card(cards)
    cards.remove(t)
    computer_cards.append(t)

  while not is_gameover:
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f"Your Cards : {user_cards} and Your score:{user_score}")
    print(f"Dealers first card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_gameover = True
    else:
      choice = input('type "y" to take a card, "n" to pass:').lower()
      if choice == "y":
        t = deal_card(cards)
        cards.remove(t)
        user_cards.append(t)
      else:
        is_gameover = True

  while computer_score != 0 and computer_score < 17:
    t = deal_card(cards)
    cards.remove(t)
    computer_cards.append(t)
    computer_score = calculate_score(computer_cards)

  print(f"Your hands : {user_cards} , final score:{user_score}")
  print(f"Computer hands : {computer_cards} , final score:{computer_score}")
  print(compare(user_score,computer_score))

replay = True
while replay:
  game()
  choice = input("Do you want play again , 'y' for continue , 'n' for exit:").lower()
  if choice == "y":
    game()
  else:
    replay = False