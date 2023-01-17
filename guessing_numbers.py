import random
number = random.randint(1, 10)

print("I am guessing a number between 1-10. You have 5 tries.")
number_of_tries = 0

while number_of_tries < 5:
    guess = int(input())
    number_of_tries += 1
    if guess < number:
        print("Your guess is greater than the number.")
    if guess > number:
        print("Your guess is less than the number.")
    if guess == number:
     break

if guess == number:
    print("Congrats! You've guessed the number. It took this many tries: ") 
    print(number_of_tries)
if guess is not number:
    print ("You couldn't guess the number, the number is: ")
    print(number)