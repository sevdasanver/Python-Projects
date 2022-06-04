'''
Play rock-paper-scissors game with user(player).
At the end, tell her who wins. (computer or player)
'''

import random
player_score, computer_score = 0 , 0

def print_result(computer_choice, winner='computer'):
  global computer_score, player_score
  print(f'The choice of computer: {computer_choice}\nWinner:{winner}')

  if winner == 'Computer':
    computer_score+=100
  else:
    player_score +=100

print('Welcome to rock-paper-scissors game! \n' + ('-' *39))

while True:
  print('\n 1-> rock\n 2-> paper\n 3-> scissors\n Or press any other keyword to exit')
  player_choice= int(input('Make your choice: '))
  computer_choice = random.choice([1,2,3])

  if player_choice ==computer_choice:
    print('Same! Play again')
  elif player_choice == 1:
    if computer_choice == 2:
        print_result(computer_choice)
    else:
        print_result(computer_choice,'player')
        player_score+=100

  elif player_choice == 2:
      if computer_choice == 1:
         print_result(computer_choice,'player')
      else:
        print_result(computer_choice)


  elif player_choice == 3:
    if computer_choice == 1:
        print_result(computer_choice)
    else:
        print_result(computer_choice,'player')
  else:
    break

print(f'\nPlayer: {player_score}\nComputer:{computer_score}')

if player_score < computer_score:
    print(f'Computer wins. Score: {computer_score - player_score}')
elif player_score > computer_score:
    print(f'Player wins. Score: {player_score - computer_score}')
else:
    print(f'Same score!')