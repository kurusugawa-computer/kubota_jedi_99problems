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

# print(fun_15(input, 3))

input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


# P18
def fun_18(start, end, x):
    return x[start:end]

# print(fun_18(3, 7, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']))

def fun_19(i, x):
    return x[i:] + x[:i]

# print(fun_19(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']))
# print(fun_19(-2, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']))

def fun_20(i, x):
    x_copy = x.copy()
    r = x_copy.pop(i)
    return(x_copy, r)

# print(fun_20(1, ["a", "b", "c", "d"]))

def fun_21(insert_str, insert_idx, x):
    x_copy = x.copy()
    x_copy.insert(insert_idx, insert_str)
    return x_copy

# print(fun_21('new', 1, ['a', 'b', 'c', 'd']))

# P22
# print(list(range(4,9+1)))


# P23
import random
print(random.sample(['a', 'b', 'c', 'd', 'f', 'g', 'h'], 3))

# P24
# print([random.randint(1, 49) for _ in range(6)])  # これだと重複することがある
print(random.sample(list(range(1, 50)), 6))


# P25
input = ["a", "b", "c", "d", "e", "f"]
def fun_25(x):
    x_copy = x.copy()
    random.shuffle(x_copy)
    return x_copy

print(fun_25(input))

# P26
import itertools

input = ["a", "b", "c", "d", "e", "f"]
comb = list(itertools.combinations(input, 3))
print(comb, len(comb))


# P27
def fun_27(group_num, human_list):
    group_indices = []
    for i, j in enumerate(group_num):
        group_indices += [i for _ in range(j)]
    group_list = []
    for indices in set(itertools.permutations(group_indices)):
        d = {i: [] for i in range(len(group_num))}
        for j, h in zip(indices, human_list):
            d[j].append(h)
        group_list.append(list(d.values()))
    return group_list

human_list = ["Aldo", "Beat", "Carla", "David", "Evi", "Flip", "Gary", "Hugo", "Ida"]
print(fun_27([2,3,4], human_list))
# print()
# print(len(fun_27([2,2,5], human_list)))


# P31
def fun_31(x):
    if x == 1:
        return False
    return sum([x % i == 0 for i in range(2, x+1)]) == 0

print(fun_31(7))

# P32
# -----------------------------------------------------------------------
# ユークリッド互助法を使わずに思いつきで書いたやつ
def prime_factorization_v1(x):
    # もっと早いアルゴリズムありそう。
    # そもそも標準機能として用意されているはず
    return [i for i in range(1, x + 1) if x % i == 0]


def prime_factorization_v2(x):
    # x/2より大きい約数は無いはず
    return [i for i in range(1, x // 2 + 1) if x % i == 0]

def prime_factorization_v2(x):
    # x/2より大きい約数は無いはず
    return [i for i in range(1, x // 2 + 1) if x % i == 0]

import sympy
def prime_factorization_v3(x):
    # sympyモジュールを使えば良いらしい
    # https://ictsr4.com/py/m0120.html
    return sympy.divisors(x)

def fun_32_v0(x1, x2):
    x1_set = set(prime_factorization_v3(x1))
    x2_set = set(prime_factorization_v3(x2))
    return max(list(x1_set & x2_set))
# print(prime_factorization_v1(10))
print(fun_32_v0(36, 63))
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# ユークリッド互助法
def fun_32(x1, x2):
    pass
# -----------------------------------------------------------------------
