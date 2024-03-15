import numpy as np

def PushZeroesToEnd(array: list[int]) -> list[int]:
    n = len(array)
    firstZero = 0
    for i in range(n):
        if array[i] == 0:
            if firstZero == 0:
                firstZero = i
            for j in range(i,n):
                if array[j] != 0:
                    array[i] = array[j]
                    array[j] = 0
                    break
    return array

def SortSequence(array: list[int]) -> list[int]:
    '''Split an array on 0, sort the subarrays and concatenate them with 0'''
    splits = []
    n = len(array)
    j = 0
    for i in range(n):
        if array[i] == 0:
            splits.append(sorted(array[j:i]))
            j = i + 1
    splits = sorted(splits, key=sum)
    result = []
    for split in splits:
        result = result + split + [0]
    print(splits)

def MeanSquareError(array_a, array_b):
    n = len(array_a)
    return sum([(array_a[i] - array_b[i]) ** 2 for i in range(n)]) / n


