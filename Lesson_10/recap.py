
# Guess the number
import random

secret = random.randint(1, 10)

guess_Anzahl = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Highscore: ", str(best_score))
score_file.close()


while True:
    guess = int(input("Guess the secret number:"))
    guess_Anzahl += 1
    if secret == guess:
        if guess_Anzahl < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(guess_Anzahl))
        score_file.close()
        print("Congratulations! You won the game :)")
        break
    elif secret > guess:
        print("Guess greater!")
    elif secret < guess:
        print("Guess smaller!")

with open("score.txt", "w") as score_file:
    score_file.write(str(guess_Anzahl))
    print("Highscore: ", str(best_score))

print("Anzahl: ",guess_Anzahl)

