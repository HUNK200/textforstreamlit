import numpy as np
import matplotlib.pyplot as plt
import pdb
import time

"旅行商问题 ( TSP , Traveling Salesman Problem )"
coordinates = np.array([[49, 49], [37, 52], [52, 64], [20, 26], [40, 30],[21, 47], [17, 63], [31, 62], [52, 33], [51, 21]])

#得到距离矩阵的函数
def SA():
    def getdistmat(coordinates):
        #shape计算维数的长度
        num = coordinates.shape[0] #52个坐标点
        # 返回给定大小的以0填充的数组
        distmat = np.zeros((52,52)) #52X52距离矩阵
        for i in range(num):
            for j in range(i,num):
                # 求范数
                distmat[i][j] = distmat[j][i]=np.linalg.norm(coordinates[i]-coordinates[j])
        return distmat

    def initpara():
        alpha = 0.99
        t = (1,100)
        markovlen = 1000

        return alpha,t,markovlen
    num = coordinates.shape[0]
    distmat = getdistmat(coordinates) #得到距离矩阵

    #arange返回长度为num的步长为1的数组
    solutionnew = np.arange(num)
    #valuenew = np.max(num)

    solutioncurrent = solutionnew.copy()
    valuecurrent =99000  #np.max这样的源代码可能同样是因为版本问题被当做函数不能正确使用，应取一个较大值作为初始值
    #print(valuecurrent)

    solutionbest = solutionnew.copy()
    valuebest = 99000 #np.max

    alpha,t2,markovlen = initpara()
    t = t2[1]
    cnt = 0
    result = [] #记录迭代过程中的最优解
    while t > t2[0]:
        for i in np.arange(markovlen):
            cnt += 1
            #下面的两交换和三角换是两种扰动方式，用于产生新解
            if np.random.rand() > 0.5:# 交换路径中的这2个节点的顺序
                # np.random.rand()产生[0, 1)区间的均匀随机数
                while True:#产生两个不同的随机数
                    loc1 = np.int(np.ceil(np.random.rand()*(num-1)))
                    loc2 = np.int(np.ceil(np.random.rand()*(num-1)))
                    ## print(loc1,loc2)
                    if loc1 != loc2:
                        break
                solutionnew[loc1],solutionnew[loc2] = solutionnew[loc2],solutionnew[loc1]
            else: #三交换
                while True:
                    loc1 = np.int(np.ceil(np.random.rand()*(num-1)))
                    loc2 = np.int(np.ceil(np.random.rand()*(num-1)))
                    loc3 = np.int(np.ceil(np.random.rand()*(num-1)))

                    if((loc1 != loc2)&(loc2 != loc3)&(loc1 != loc3)):
                        break

                # 下面的三个判断语句使得loc1<loc2<loc3
                if loc1 > loc2:
                    loc1,loc2 = loc2,loc1
                if loc2 > loc3:
                    loc2,loc3 = loc3,loc2
                if loc1 > loc2:
                    loc1,loc2 = loc2,loc1

                #下面的三行代码将[loc1,loc2)区间的数据插入到loc3之后
                tmplist = solutionnew[loc1:loc2].copy()
                solutionnew[loc1:loc3-loc2+1+loc1] = solutionnew[loc2:loc3+1].copy()
                solutionnew[loc3-loc2+1+loc1:loc3+1] = tmplist.copy()

            valuenew = 0
            for i in range(num-1):
                valuenew += distmat[solutionnew[i]][solutionnew[i+1]]
            valuenew += distmat[solutionnew[0]][solutionnew[9]]
           # print (valuenew)
            if valuenew<valuecurrent: #接受该解
                # print (t) #程序运行时间较长，打印t来监视程序进展速度
                #更新solutioncurrent 和solutionbest
                valuecurrent = valuenew
                solutioncurrent = solutionnew.copy()

                if valuenew < valuebest:
                    valuebest = valuenew
                    solutionbest = solutionnew.copy()
            else:#按一定的概率接受该解
                if np.random.rand() < np.exp(-(valuenew-valuecurrent)/t):
                    valuecurrent = valuenew
                    solutioncurrent = solutionnew.copy()
                else:
                    solutionnew = solutioncurrent.copy()
        t = alpha*t
        result.append(valuebest)
    return cnt, solutionbest, valuebest, result
# time_end = time.time()
# #用来显示结果
# plt.plot(np.array(result))
# plt.ylabel("bestvalue")
# plt.xlabel("t")
# plt.show()
# print(cnt)
# print(valuebest)
# print("time：{}".format(time_end - time_start))
# print(solutionbest)