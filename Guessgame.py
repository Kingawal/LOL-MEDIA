done = False
import random
computer = random.randint(1, 30)
guess_count = 0
while not done:
    print('You have made', guess_count, 'trial(s)')
    guess = int(input('Guess a number between 1 and 30 :'))
    guess_count += 1
    if guess == computer:
        print('correct!!!')
        done = True
    else:
        if guess_count == 5:
            print('Gameover!💔💔💔💔')
            print('Correct number is', computer)
            print('Try next time!')
            done = True
        
