from Lesson_13.BasketballPlayer import BasketballPlayer



kevin = BasketballPlayer("Kevin", "Lebron", 201, 118, 7.2, 7.4, 8.1)

print("Create a Player with the following details:")
kevin.first_name = input("First name of the player: ")
kevin.last_name = input("Last name of the player: ")
kevin.height_cm = input("Height: ")
kevin.weight_kg = input("Weight: ")

print("Your created Player:", kevin.first_name, kevin.last_name, kevin.height_cm, kevin.weight_kg)



