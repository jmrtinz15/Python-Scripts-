import random

print('Welcome. What is your name?')
name = input()

# randint allows us to pass in two parameters -> random number between 1 and 20
print('Well, ' + name + ', I am thinking of a number between 1 and 20')
number = random.randint(1, 20) 

#guess will be inputed as a string so we need to convert it to a integer to make the if statement logic work
for guessestaken in range(1, 7): #Basically have 6 tries to guess the number correctly
    print('Take a guess.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        break # This condition is for the correct guess

#If they guess correctly else they run out of guesses
if guess == number:
    print('Good job!, You guessed my number in ' + str(guessestaken) +  'guesses.')
else:
    print('Sorry. The number I was thinking of was' + str(number))






