import math

def GenerateBinaryAsString(n:int) -> str:
    b = ["0"] * (math.floor(math.log2(n)) + 1)
    for i in range(len(b)):
        t = len(b)-i - 1
        d = math.pow(2,t)
        if(d <= n):
            b[i] = "1"
            n = n - d
        else:
            continue

    return "".join(b)
