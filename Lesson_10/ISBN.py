import operator

digits = []
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
mul_list = []
check_digit = 0

isbn = input("Give the first 9 digits for 10 digit ISBN number: ")
digits = [int(i) for i in isbn]
mul_list = list(map(operator.mul, digits, numbers))

result = 0
for j in mul_list:
    result += j

if result % 11 == 0:
    check_digit = 0
else:
    check_digit = (result + (11 - (result % 11))) - result

print("The checkdigit number is:", check_digit)
print("The full ISBN number is: ISBN", isbn,"-", check_digit)
