
primnumbers = []
sexyprimsdict = {}

for i in range(2, 101):
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
    if isprime:
        primnumbers.append(i)

print(primnumbers)

for x in primnumbers:
    for y in primnumbers:
        if x + 6 == y:
            sexyprimsdict.update({x: y})

print(sexyprimsdict)
