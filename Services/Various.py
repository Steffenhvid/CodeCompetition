from unittest import TestCase
from collections import Counter

def obtain_max_number(lst):
    data = dict(Counter(lst))
    while any(x > 1 for x in data.values()):
        tmp =dict(data)
        for key in data.keys():
            if data[key] > 1:
                new_value = key*2
                tmp[new_value] = tmp.get(new_value, 0) + 1
                tmp[key] -= 2
        data = tmp
    return max([key for key in data.keys() if data[key] == 1])    

def basic_test_cases():
        print(obtain_max_number([2, 4, 8, 1, 1, 15]),16)
        print(obtain_max_number([2, 2, 4, 8, 1, 1, 15]),16)
        print(obtain_max_number([2, 4, 8, 1, 1, 15, 15, 7, 7, 7, 7, 7, 7, 7]),30)
        print(obtain_max_number([2, 4, 8, 1, 1, 30, 30, 15, 15, 7, 7]), 60)
        print(obtain_max_number([2, 4, 8, 1, 1, 119, 30, 30, 15, 15, 7, 7]), 119)
        print(obtain_max_number([2, 4, 8, 1, 1, 32, 8, 8, 64, 30, 30, 15, 15, 7, 7]), 128)

def count_a_z(strng:str) -> dict:
    '''
    Returns a dict, with the count of all letters in string, if letter in a..z
    '''
    result = {}
    for c in strng:
        if c <= 'z' and c >= 'a':
            if c not in result.keys():
                result[c] = 1
            else:
                result[c] += 1
    return result

def Mix(s1:str, s2:str):
    '''
    Counts the chars in a-z that two strings have in common.
    Ignoring the cases when the char is only occuring once.
    '''
    fd = count_a_z(s1)
    sd = count_a_z(s2)

    keys = set(sorted(fd) + sorted(sd))

    result = []
    for key in keys:
        if key in fd.keys() and key in sd.keys():
            if fd[key] == sd[key]:
                result.append(["=:",key,fd[key]])
            elif fd[key] > sd[key]:
                result.append(["1:",key,fd[key]])
            else:
                result.append(["2:",key,sd[key]])
        elif key in fd.keys() and key not in sd.keys():
            result.append(["1:",key,fd[key]])
        elif key not in fd.keys() and key in sd.keys():
            result.append(["2:",key,sd[key]])

    values = set(map(lambda x:x[2], result))
    values.remove(1)
    newlist = [[[y[0],y[1], y[2]] for y in result if y[2]==x] for x in values]
    newlist.reverse()
    new_result = []
    for lst in newlist:
        if len(lst) == 1:
            new_result.append(lst[0][0]+lst[0][1]*lst[0][2])
        else:
            lst.sort(key = lambda row: (row[0],row[1]))
            for i in range(len(lst)):
                new_result.append(lst[i][0]+lst[i][1]*lst[i][2])

    return "/".join(new_result)

class chaining_routes:
    def __init__(self):
        self.Basic_tests = [
        ([('one','two')], 'one, two'),
        ([('one','two'), ('two','three')], 'one, two, three'),
        ([('two','three'), ('one','two')], 'one, two, three'),
    ]

    def extract_entries(self, arr, entry):
        return set(list(zip(*arr))[entry])

    def extract_destination(self, arr, entry):
        return list(filter(lambda x: x[0] == entry, arr))[0][1]

    def find_routes(self, routes):
        if len(routes) == 1:
            return f"{routes[0][0]}, {routes[0][1]}"
        
        A = self.extract_entries(routes,0)
        B = self.extract_entries(routes,1)

        start_location = A-B
        end_location = B-A

        current = list(start_location)[0]
        end_location_string = list(end_location)[0]
        result = ""
        while current != end_location_string:
            result += current + ", "
            current = self.extract_destination(routes, current)

        result += end_location_string
        return result
    
    def run_tests(self):
        for test_case, expected in self.Basic_tests:
            if self.find_routes(test_case) != expected:
                raise ValueError("Test failed")


from itertools import product

def get_possible_digits(n):
    match int(n):
        case 0:
            return [0,8]
        case 1:
            return [1,2,4]
        case 2:
            return [1,2,3,5]
        case 3:
            return [2,3,6]    
        case 4:
            return [1,4,5,7]
        case 5:
            return [2,4,5,6,8]
        case 6:
            return [3,5,6,9]
        case 7:
            return [4,7,8]
        case 8:
            return [5,7,8,9,0]
        case 9:
            return [6,8,9]
        case _:
            return [-1]

def tuple_to_string(tuple_name):
    result = ''.join(map(str, tuple_name))
    return result

def get_pins(observed):
    individual_digits = list(observed)
    possible_digits = map(get_possible_digits, individual_digits)
    result = list(map(tuple_to_string,product(*possible_digits)))
    result.sort()
    return result

test_cases = [
        ('8', ['5','7','8','9','0']),
        ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', [
            "339","366","399","658","636","258","268","669","668","266","369","398",
            "256","296","259","368","638","396","238","356","659","639","666","359",
            "336","299","338","696","269","358","656","698","699","298","236","239"
        ])
    ]