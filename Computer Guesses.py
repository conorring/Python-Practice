#I am thinking of a number between 1 and 100.
#The computer has to guess
#I will give it higher or lower clues

maximum=100
minimum=1
guesses=0
print('Think of a number between one and one hundred')
while True:
    guesses+=1
    guess=int((maximum+minimum)/2)
    ans=input('My guess is %d. Too high, too low, or just right?' %guess)
    if ans.lower() == 'just right':
        print('Hahaha I won')
        break
    elif ans.lower() == 'too low':
        if guess == 99:
            guesses+=1
            print('Your number is 100')
            break
        minimum=int((maximum+minimum)/2)
    else:
        maximum=int((maximum+minimum)/2)

print("I took",guesses,"guesses. Not bad.")

input=("Press enter to exit.")





