'''
Generate a number and tell to the user to guess it.
He should keep guessing until find the number you generate at the beginning.
'''
import random 
def guess():
  count=1
  random_number = random.randint(1, 11)
  print("Let's play a game. Try to guess the number on my mind.")
  print('But be careful. You can try only 5 times!! ')
  print('-----------------')
  
  for i in range (5): 
    her_guess = int(input('Guess a number between 1 and 10: '))

    if her_guess > random_number: 
      print(f'{her_guess}? Nope. You just missed it. Enter a smaller one.')
    elif her_guess < random_number:
      print(f'You just missed it. It is not {her_guess}. Enter a bigger one.')
    else:
      print('-----------------')
      print('Hey hey!!!!!')
      print('You nailed it! Congrats!')
      print('You found it on your {}th guess! '.format(count))
      break
    count+=1

  print('The number was {}.' .format(random_number))
guess()