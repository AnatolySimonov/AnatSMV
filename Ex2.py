import random
print('Welcome to Casino')
balance = 10000
bid = 1000
attempt = 0
print('Your balance:', balance)
print('Bet:', bid)
print('Guess the lucky number between 2 and 12!')
while balance >= bid:
    player_number = int(input())
    sys_number = random.randrange(2, 12)
    if player_number > 12 or player_number < 2:
        print('No, this number is not correct. Choose one from 2 to 12.')
    else:
        attempt = attempt + 1
        print('Lucky number is', sys_number, '!')
        if player_number == sys_number:
            print('Congratulations! You won!')
            balance = balance + 1000
            print('Your new balance is', balance,)
            journal = ['Recent Lucky number:', sys_number, 'Your number:', player_number, 'Attempts:', attempt, 'Balance:', balance]
            print('Another one?')
            print(journal[0:])
        else:
            print('You lost!')
            balance = balance - 1000
            print('Your new balance is', balance,)
            journal = ['Recent Lucky number:', sys_number, 'Your number:', player_number, 'Attempts:', attempt, 'Balance:', balance]
            print('Try again!')
            print(journal[0:])
else:
    print('You are broke. Maybe try refreshing this page?')
