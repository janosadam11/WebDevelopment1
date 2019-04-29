import random
import json

import datetime

current_time = datetime.datetime.now()

print(current_time)


secret = random.randint(1, 30)
attempts = 0
wrong_attempts = 0
score_data = {"attempts": attempts, "date": datetime.datetime.now()}

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

eu_cities = ["Vienna", "Malaga", "Budapest", "Cologne", "Zagreb"]
jordan = {"first_name": "Michael", "last_name": "Jordan", "age": 56, "games_played": 1072, "total_points": 32292}

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "wrong attempts": wrong_attempts,
                           "date": str(datetime.datetime.now())})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        score_file.close()
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_attempts += 1
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_attempts += 1


