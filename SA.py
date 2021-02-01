# -*- coding: utf-8 -*-
from math import *
from random import *

city = [[49, 49], [37, 52], [52, 64], [20, 26], [40, 30], [21, 47], [17, 63], [31, 62], [52, 33], [51, 21]]

N = 10

def dis(a, b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


def energy_count(t):
    global city
    temp = 0
    for i in range(1, len(city)):
        temp += dis(city[t[i]], city[t[i - 1]])
    temp += dis(city[t[0]], city[t[len(city) - 1]])
    return temp

def rangen1(s):
    ti = randint(0, N - 1)
    tj = ti
    while ti == tj:
        tj = randint(0, N - 1)
    s[ti], s[tj] = s[tj], s[ti]


# 随机交换两组
def rangen2(s):
    ti = randint(0, N - 1)
    tj = ti
    tk = ti
    while ti == tj:
        tj = randint(0, N - 1)
    while ti == tj or tj == tk or ti == tk:
        tk = randint(0, N - 1)
    s[ti], s[tj] = s[tj], s[ti]
    s[tk], s[tj] = s[tj], s[tk]


# 随机交换三组
def rangen3(s):
    ti = randint(0, N - 1)
    tj = ti
    tm = randint(0, N - 1)
    tn = ti
    while ti == tj:
        tj = randint(0, N - 1)
    while tm == tn:
        tn = randint(0, N - 1)
    s[ti], s[tj] = s[tj], s[ti]
    s[tm], s[tn] = s[tn], s[tm]


# 等概率交换
def gen(s):
    t = randint(0, 2)
    if t == 0:
        rangen1(s)
    elif t == 1:
        rangen2(s)
    else:
        rangen3(s)


def metro(f1, f2, t,list):
    # 新状态小于旧状态则直接接受
    for i in list:
        i = 1
    list = [1, 2, 3, 4]
    if f2 < f1:
        return True
        # f1 = f2
        # old = new
        # if f2 < best:
        #     best = f2
        #     for i in range(len(new)):
        #         seq_best[i] = new[i]
        #     print(seq_best)
    else:
        # 可接受概率
        p = exp(-(f2 - f1) / t)
        r = random()
        if r < p:
            return True
            # f1 = f2
            # old = new
        else:
            return False
            # new = old


def SA():
    N = 10
    seq_best = [0 for i in range(0, N)]
    best = 1000000
    initT = 1000  # 初始温度
    u = 0.998  # 成功降温因子
    v = 0.999  # 失败降温因子
    k = 100  # 单次迭代上限
    seq = [i for i in range(0, N)]  # 当前路径序列
    lowt = 1
    cnt = 0
    # 去极大值作为初值

    res = []
    old_energy = energy_count(seq)
    # 临时状态
    seq_t = seq

    t = initT
    while t > lowt:
        for i in range(k):
            # 产生新状态
            gen(seq_t)
            # print(seq_t)
            new_energy = energy_count(seq_t)
            if metro(old_energy, new_energy, t):
                old_energy = new_energy
                if new_energy < best:
                    best = new_energy
                    for i in range(N):
                        seq_best[i] = seq_t[i]
            # print(seq)
            cnt += 1
        t *= u
        # print(t)
        res.append(best)

    return cnt, seq_best, best, res

# print(SA())
# print(energy_count([4, 9, 3, 1, 0, 8, 6, 2, 7, 5]))
