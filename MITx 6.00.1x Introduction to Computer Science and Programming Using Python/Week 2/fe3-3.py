print("Please think of a number between 0 and 100!")

low = 0
high = 100
guess = (low + high)//2
print("Is your secret number {}?".format(guess))
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while ans != 'c':
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    else:
        print("Sorry, I did not understand your input.")

    if ans == 'h' or ans == 'l':
        guess = (low + high)//2
        
    print("Is your secret number {}?".format(guess))    
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: {}".format(guess))
