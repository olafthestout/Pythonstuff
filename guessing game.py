low = 0
high = 100

guess = high/2

correct = 0

print ('Please think of a number between ' + str(low) + ' and ' + str(high) + '!')

while correct <= 0:
    print('Is your secret number ' + str(guess) + '?')
    print("Enter 'h' to indicate the guess is too high."),
    print("Enter 'l' to indicate the guess is too low."),
    confirm = raw_input("Enter 'c' to indicate I guessed correctly. " )
    
    
    if confirm == 'h':
        high = guess
        guess = (high + low)/2

    
    elif confirm == 'l':
        low = guess
        guess = (high + low)/2

        
    elif confirm == 'c':
        correct = 1
    
    else:
        print('Sorry, I did not understand your input.')
 
    
else:
    print('Game over. Your secret number was: ' + str(guess))
