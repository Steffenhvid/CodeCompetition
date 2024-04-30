import numpy as np

test = [[97, -44, -47, -10129], [23, 64, 17, 119], [-30, -6, 82, 2244]]

def gauss_seidel(coeff_matrix):
    x,y,z = 0,0,0
    
    xe = coeff_matrix[0]
    ye = coeff_matrix[1]
    ze = coeff_matrix[2]


    for i in range(100):
        xc = 1/xe[0] * (y * -1 * xe[1] + z * -1 * xe[2] + xe[3])
        yc = 1/ye[1] * (x * -1 * ye[0] + z * -1 * ye[2] + ye[3])
        zc = 1/ze[2] * (x * -1 * ze[0] + y * -1 * ze[1] + ze[3])

        if ct(xc,x) and ct(yc,y) and ct(zc,z):
            return ([xc,yc,zc], i+1-5)
        else:
            x = xc
            y = yc
            z = zc
    return (x,y,z)

def ct(a,b):
    return np.abs(a-b) <= 0.0001

print(gauss_seidel(test))

# ([3.0167567484114746, 1.9858893605869723, 0.9118159523141861], 7)))
# (3.0167548500881836, 1.9858906525573194, 0.9118165784832449)