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
def mileconverter(value_km):
    value_miles = value_km * 0.621371
    print("Your value in miles: ", value_miles, "\n")


def kmconverter(value_mile):
    value_inkm = value_mile / 0.621371
    print("Your value in km: ", value_inkm, "\n")


def decide(unit):
    if unit.lower() == "km":
        value_km = float(input("Please give the value in km: \n"))
        mileconverter(value_km)
    elif unit.lower() == "mile":
        value_mile = float(input("Please give me the value in mile:"))
        kmconverter(value_mile)


print("This is a unit converter program. You can convert km to miles and backwards!")
unit = input("Please give me the unit(KM/MILE): ")
decide(unit)


while True:
    convert_Again = input("Would you like to convert again? Y/N")
    if convert_Again.lower() != "y":
        break
    unit = input("Please give me the unit(KM/MILE): ")
    decide(unit)
    # value_km = float(input("Please give the value in km again: \n"))
    # mileconverter(value_km)


