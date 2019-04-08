# Calculator
# first_number = int(input("Give the first number: \n"))
# second_number = int(input("Give the second number: \n"))
# operator = input("What would you like to do with the numbers? (+)(-)(*)(/)")
#
# result = 0
# if operator == "+":
#     result = first_number + second_number
#     print(result)
# elif operator == "-":
#     result = first_number - second_number
#     print(result)
# elif operator == "*":
#     result = first_number * second_number
#     print(result)
# elif operator == "/":
#     result = first_number / second_number
#     print(result)
# else:
#     print("Unsupported operator")

# Guess the number
import random

secret = random.randint(1, 10)

guess_Anzahl = 0
guess = 0
while secret != guess:
    guess_Anzahl = int(input("Guess the secret number? \n"))
    guess += 1
    if secret == guess:
        print("Congratulations! You won the game :)")
        guess_Anzahl += 1
        break
    elif secret > guess:
        print("Guess greater!")
        guess_Anzahl += 1
    elif secret < guess:
        print("Guess smaller!")
        guess_Anzahl += 1
    else:
        print("Guess again!")
        guess_Anzahl += 1
print()
# Moodchecker
# if mood=="happy":
#     print("It is great to see you happy!")
# elif(mood=="nervous"):
#     print("Take a deep breath 3 times.")
# elif(mood=="sad"):
#     print("Im sorry about that :(")
# else:
#     print("Moodless")
