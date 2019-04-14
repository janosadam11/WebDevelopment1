import operator

digits = []
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
addlist = []
checkdigit = 0

isbn = input("Give the first 9 digits for 10 digit ISBN number: ")
digits = [int(i) for i in isbn]
addlist = list(map(operator.mul, digits, numbers))

result = 0
for j in addlist:
    result += j

if result % 11 == 0:
    checkdigit = 0
else:
    checkdigit = (result + (11 - (result % 11))) - result

print("The checkdigit is:", checkdigit)
print("The full ISBN number is: ISBN", isbn,"-", checkdigit)
