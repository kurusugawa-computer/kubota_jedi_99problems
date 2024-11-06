# P01
input = [1, 1, 2, 3, 5, 8]
# print(input[-1])

# P05
# print(input[::-1])
# list(reversed([1,2,3]))

# P06
# print(input[::-1] == input)

# import itertools
# l_2d = [[0, 1], [2, [3,4]]]
# print(list(itertools.chain.from_iterable(l_2d)))
# exit()
# [0, 1, 2, 3]

# P07
input = [[1, 1], 2, [3, [5, 8]]]
def fun_07(x):
    output = []
    for i in x:
        if isinstance(i, list):
            output += fun_07(i)
        else:
            output.append(i)
    return output

# print(fun_07(input))

# P08
input = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
def fun_08(x):
    tmp = ''
    output = []
    for i in x:
        if i == tmp:
            continue
        else:
            output.append(i)
            tmp = i
    return output

# print(fun_08(input))

# P09
input = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
def fun_09(x):
    tmp = x[0]
    tmp_list = []
    output = []
    for i in x:
        if i != tmp:
            output.append(tmp_list)
            tmp_list = []
            tmp = i
        tmp_list.append(i)
    output.append(tmp_list)
    return output

# print(fun_09(input))

# P11
input = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
def fun_11(x):
    tmp = x[0]
    counter = 0
    output = []
    for i in x:
        if i != tmp:
            output.append((counter, tmp) if counter > 1 else tmp)
            counter = 0
            tmp = i
        counter += 1
    output.append((counter, tmp) if counter > 1 else tmp)
    return output

# print(fun_11(input))

import itertools
input = ['a', 'b', 'c', 'c', 'd']
# print([i for i in input for _ in range(2)])
# print([x for x in range(2) for i in input])


# P15
input = ['a', 'b', 'c', 'd']
def fun_15(x, n):
    output = []
    for i in x:
        output += [i] * n
    return output

print(fun_15(input, 3))


input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
