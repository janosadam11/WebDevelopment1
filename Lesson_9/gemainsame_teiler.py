first = int(input("First number: "))
second = int(input("Second number: "))
divider = 0

while True:
    divider = first % second
    if divider == 0:
        print(second, "is the greater divider")
        break
    else:
        first = second
        second = divider

