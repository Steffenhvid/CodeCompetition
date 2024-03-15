test = ""

for i in range(1,200000):
    test += str(i)

print(int(test[0])*int(test[9])*int(test[99])*int(test[999])*int(test[9999])*int(test[99999])*int(test[999999]))
