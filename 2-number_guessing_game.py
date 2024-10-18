import random

top_of_range = input ("Type a number: ")
#verify if user input is a number
# after confirminig number transform default string user input into number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
#check that inputed number is not smaller than zero
    if top_of_range <= 0:
        print('please type a number bigger than zero next time.')
        quit()
 #input is not a number, tell user           
else:
    print('Please type a number next time.')
    quit()
    
#making a random number
random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print('You are above the number!')
    else:
        print('You are below the number!')
    
print('You got it in', guesses, 'guesses.')