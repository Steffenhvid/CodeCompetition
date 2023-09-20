
def origo_in_trianglespace(x1, y1, x2, y2, x3, y3) -> bool:
    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)

    direction = cross_product(vector(A, B), vector(A, C))

    if(direction >= 0):
        C1 = cross_product(vector(A, B), vector(A, (0 ,0)))
        C2 = cross_product(vector(B, C), vector(B, (0 ,0)))
        C3 = cross_product(vector(C, A), vector(C, (0 ,0)))
    else:
        C1 = cross_product(vector(A, C), vector(A, (0 ,0)))
        C2 = cross_product(vector(C, B), vector(C, (0 ,0)))
        C3 = cross_product(vector(B, A), vector(B, (0 ,0)))


    return 0 < C1 and 0 < C2 and 0 < C3

def cross_product(A:tuple, B:tuple):
    return (A[0] * B[1]) - (A[1] * B[0])

def vector(A:tuple, B:tuple) -> tuple:
    return (B[0] - A[0], B[1] - A[1])