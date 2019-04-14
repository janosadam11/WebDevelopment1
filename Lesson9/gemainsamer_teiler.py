first = int(input("First number: "))
second = int(input("Second number: "))
divider = 1

while divider:
    divider = first % second
    first = second
    second = divider
print(first, "is the greater divider")