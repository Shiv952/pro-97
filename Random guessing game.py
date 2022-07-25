import random

numofguesses = 0

print("Hello!! What is your name?")
name = input()

number = random.randint(1,20)
print("The number i am guessing of is between 1 and 20" ,name)

while numofguesses < 6:
    guess = input()
    guess = int(guess)
    numofguesses = numofguesses + 1
    if guess < number:
          print("Just a little up" ,name)
    if guess > number:
          print("Lower" ,name, "Lower")
    if guess == number:
          break
if guess == number:
        numofguesses = str(numofguesses)
        print("well well!!" ,name ,"you guessed it right in just:" ,numofguesses, "guesses")

if guess != number:
            number = str(number)
            print ("Wrong! the number was:" ,number)
