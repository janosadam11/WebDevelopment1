# import random
# #
# # secret = random.randint(1, 10)
# # print(secret)
# # guess_Anzahl = 0
# # guess = 0
# # while secret != guess:
# #     guess = int(input("Guess the secret number between 1-10? \n"))
# #     guess_Anzahl += 1
# #     if secret == guess:
# #         print("Congratulations! You won the game :)")
# #         guess_Anzahl += 1
# #         break
# #     elif secret > guess:
# #         print("Guess greater!")
# #         guess_Anzahl += 1
# #     elif secret < guess:
# #         print("Guess smaller!")
# #         guess_Anzahl += 1
# #     else:
# #         print("Guess again!")
# #         guess_Anzahl += 1
# #
# # print(range(0,10,5))

import sys

#Unit converter
def mileconverter(again):
    value_miles = value_km * 0.621371
    print("Your value in miles: ", value_miles, "\n")

def kmconverter(again):
    value_inkm = value_mile / 0.621371
    print("Your value in km: ", value_inkm, "\n")


print("This is a unit converter program. You can convert km to miles and backwards!")
unit = input("Please give me the unit(km/mile): "))
if unit == "km":
    value_mile = float(input("Please give the value in km: \n"))
    mileconverter(value_mile)
elif unit == "mile":
    value_km = float(input("Please give me the value in mile:"))
    kmconverter(value_km)


while True:
    convert_Again = input("Would you like to convert again? y/n")
    if convert_Again != "y":
        break
    value_km = float(input("Please give the value in km again: \n"))
    mileconverter(value_km)


