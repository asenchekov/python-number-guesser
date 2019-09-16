# terminal based game in Python
from random import randint

print('Terminal based number guessing game')
while True:
    try:
        numberOfGames = int(input('Please choose how many games you want to play ---> '))
    except:
        print('Only numbes accepted')
        continue
    if (numberOfGames > 0 and numberOfGames < 10):
        break;

randomNumbers = []

for i in range(numberOfGames):
    randomNumbers.append(randint(1, 10))

for index, number in enumerate(randomNumbers):
    print('Game %i' %(index + 1))
    guess = 0
    attempts = 0
    while (guess != number):
        try:
            guess = int(input('Guess the number ---> '))
        except Exception as e:
            print('Only numbers accepted')
            continue
        if (guess > number):
            print('Your number is bigger!')
        else:
            print('Your number is smaller!')
        attempts += 1
    print('Great you guessed it! Attempts %i' %attempts)
    attempts = 0
