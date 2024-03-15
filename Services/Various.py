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