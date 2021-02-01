import matplotlib.pyplot as plt
from math import *
from random import *

'''
城市坐标
1 37 52
2 49 49
3 52 64
4 20 26
5 40 30
6 21 47
7 17 63
8 31 62
9 52 33
10 51 21
解：
[0 2 1 7 6 5 3 4 9 8]
[3, 4, 9, 8, 0, 2, 1, 7, 6, 5]
160.64938606730001
[4, 9, 3, 1, 0, 8, 6, 2, 7, 5]
160.64938606730001
'''

# 城市距离
city = [[49, 49], [37, 52], [52, 64], [20, 26], [40, 30],[21, 47], [17, 63], [31, 62], [52, 33], [51, 21]]
N = 10
initT = 100  # 初始温度
u = 0.9# 成功降温因子
v = 0.999  # 失败降温因子
k = 100  # 单次迭代上限
seq = [i for i in range(0, N)]  # 路径序列
seq_best = []
lowt = 1e-9
ans = 0

best = 1000000
res = []
# 计算点之间的距离
def dis(a, b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


# 能量计算
def energy_count(t):
    global city
    temp = 0
    for i in range(1, len(t)):
        temp += dis(city[t[i]], city[t[i - 1]])
    temp += dis(city[t[0]], city[t[len(t) - 1]])
    return temp


# Metropolis准则
def metro(f1, f2, t, s):
    # 新状态小于旧状态则直接接受
    global best
    global seq_best
    if f2 < f1:
        if f2 < best:
            best = f2
            seq_best = s

        return True
    # 可接受概率
    p = exp(-(f2 - f1) / t)
    r = random()
    if r < p:
        return True
    return False


def initgen():
    vis = [0 for x in range(0, N)]
    s = [0 for x in range(0, N)]

    for i in range(0, N):
        s[i] = randint(0, N - 1)
        while v[s[i]]:
            s[i] = randint(0, N - 1)
        v[s[i]] = True
    return s


# 随机交换一组
def rangen1(s):
    global seq

    ti = randint(0, N - 1)
    tj = ti
    while ti == tj:
        tj = randint(0, N - 1)
    for i in range(0, N):
        s[i] = seq[i]
    s[ti], s[tj] = s[tj], s[ti]


# 随机交换两组
def rangen2(s):
    global seq
    ti = randint(0, N - 1)
    tj = ti
    tk = ti
    while ti == tj:
        tj = randint(0, N - 1)
    while ti == tj or tj == tk or ti == tk:
        tk = randint(0, N - 1)
    for i in range(0, N):
        s[i] = seq[i]
    s[ti], s[tj] = s[tj], s[ti]
    s[tk], s[tj] = s[tj], s[tk]


# 随机交换三组
def rangen3(s):
    global seq
    ti = randint(0, N - 1)
    tj = ti
    tm = randint(0, N - 1)
    tn = ti
    while ti == tj:
        tj = randint(0, N - 1)
    while tm == tn:
        tn = randint(0, N - 1)
    for i in range(0, N):
        s[i] = seq[i]
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

# def SA():
#     global cnt
#     global ans
#     global seq
#     t = initT
#     # seq = [i for i in range(0, N)]
#     seq_t = seq
#     new_energy = 1
#     old_energy = energy_count(seq)
#     while t > 1:
#         cnt += 1
#         for i in range(100):
#             gen(seq_t)
#             # print(seq_t)
#             # print(seq)
#             new_energy = energy_count(seq_t)
#             if metro(old_energy, new_energy, t, seq_t):
#                 seq = seq_t
#                 ans = new_energy
#                 old_energy = new_energy
#             else:
#                 seq_t = seq
#         t *= u
#         # print(t)



def SA():
    cnt = 0
    global ans
    global res
    t = initT
    seq_t = []
    for i in range(0, N):
        seq[i] = i
        seq_t.append(i)
    new_energy = 1
    old_energy = 0
    while t > 1 and abs(new_energy - old_energy) > lowt:
        t_k = k
        seq_tt = [0 for i in range(0, N)]
        while t_k > 0 and abs(new_energy - old_energy) > lowt:
            cnt += 1
            rangen1(seq_tt)
            new_energy = energy_count(seq_tt)
            old_energy = energy_count(seq_t)
            if metro(old_energy, new_energy, t, seq_tt):
                for i in range(0, N):
                    seq_t[i] = seq_tt[i]
        new_energy = energy_count(seq_t)
        old_energy = ans
        if metro(old_energy, new_energy, t, seq_t):
            for i in range(0, N):
                seq[i] = seq_t[i]
            ans = energy_count(seq)
            t *= u
        else:
            t *= v
        res.append(best)
    ans = energy_count(seq)
    return cnt

# print(seq)
# SA()
# print(cnt)
# print(seq_best)
# print(ans)
# s = [i for i in range(0, N)]
# plt.figure()
# for i in range(1, N):
#     plt.plot(city[i][0], city[i][1], 'o')
#     plt.plot([city[s[i]][0], city[s[i - 1]][0]], [city[s[i]][1], city[s[i - 1]][1]])
# plt.plot(city[0][0], city[0][1], 'o')
# plt.plot([city[s[0]][0], city[s[N - 1]][0]], [city[s[0]][1], city[s[N - 1]][1]])
# plt.show()
# plt.figure()
# for i in range(1, N):
#     plt.plot(city[i][0], city[i][1], 'o')
#     plt.plot([city[seq[i]][0], city[seq[i - 1]][0]], [city[seq[i]][1], city[seq[i - 1]][1]])
# plt.plot(city[0][0], city[0][1], 'o')
# plt.plot([city[seq[0]][0], city[seq[N - 1]][0]], [city[seq[0]][1], city[seq[N - 1]][1]])
# plt.show()