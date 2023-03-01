import numpy as np
from math import factorial

np.random.seed(1)
n = 60
b = np.random.randint(1, 7, n)
# print(b)
# [6 4 5 1 2 4 6 1 1 2 5 6 5 2 3 5 6 3 5 4 5 3 5 6 3 5 2 2 1 6 2 2 6 2 2 1 5
# 2 1 1 6 4 3 2 1 4 6 2 2 4 5 1 2 4 5 3 5 1 6 4]
a = b[b == 3]
# print(a)
# [3 3 3 3 3 3]
m = len(a)
# print(m)
# 6
# Теперь можем вычислить относительную частоту событий А

W = m/n
# print(W)
# 0.1


# Смоделируем ситуацию, когда бросают две игральные кости одновременно 360 раз.
# Посчитаем относительную частоту события, когда на одной кости выпадает 1, а на другой 2

n = 360
np.random.seed(1)
c = np.random.randint(1, 7, size=n)
d = np.random.randint(1, 7, size=n)
# print(c,d)
a = c[(c == 1) & (d == 2)]
# print(a)
m = len(a)
# print(m)
W = m/n
# print(W)
# 0.03333333333333333

# Сколькими способами можно выбрать из колоды, состоящей из 36 карт, 4 карты?
def combinations(n, k):
    return np.math.factorial(n)//(np.math.factorial(k)*np.math.factorial(n-k))

# print(combinations(36, 4))

# В магазине 20 покупателей. Сколькими способами они могут образовать очередь из 5 человек?
def arrangements(n, k):
    return np.math.factorial(n)//np.math.factorial(n-k)

# print(arrangements(20, 5))

# Сколькими способами 5 покупателей могут образовать очередь?
def permutations(n):
    return np.math.factorial(n)

# print(permutations(5))