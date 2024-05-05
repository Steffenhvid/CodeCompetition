import sys
sys.path.append(".\\")
from Services.Fractions import reduceFraction

result = []

for i in range(12,100):
    for j in range(11,i):
        a,b = list(str(j))
        k,q = list(str(i))
        if int(a) == 0 or int(b) == 0 or int(k) == 0 or int(q) == 0:
            continue
        stri = list(str(i))
        if a in stri:
            stri.remove(a)
            c = int(stri[0])
            if j/i == int(b)/c:
                result.append([j,i])
        stri = list(str(i))
        if b in stri:
            stri.remove(b)
            c = int(stri[0])
            if j/i == int(a)/c:
                result.append([j,i])

result2 = []
for x in result:
    result2.append(reduceFraction(x[0],x[1]))

o = 1
p = 1
for y in result2:
    o *= y[0]
    p *= y[1]
    
print(reduceFraction(o,p))