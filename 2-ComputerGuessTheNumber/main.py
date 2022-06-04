import random

def computer_guess():
    start, end = 1, 100
    back = ''
    
    while back != "c":
        if start <= end:
            guess = random.randint(start, end)
        else:
            guess = start

        back = input(f"If {guess} is greater than the value you have on mind enter h,\n if lower enter l,\n if correct enter c.\n If you want to exit the game, press any key.").lower()
        print("---*---")
        
        if back == 'h':
            end = guess - 1
        elif back == 'l':
            start = guess + 1
        elif back != 'c':
            print("You are leaving the game!")
            break
        
    else:
        print('Congratulations, correct guess!')

computer_guess()