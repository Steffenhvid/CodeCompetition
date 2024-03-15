results = []

for i in range(1, 500000):
    number = ""
    j = 1
    while len(number) < 9:
        number += str(i*j)
        j += 1
    if len(number) == 9 and set(number) == set("123456789"):
        print(number)

results
        