import streamlit as st
import main as m
import matplotlib.pyplot as plt
import time
import SA2 as m2
import SA as m3
# print(m.seq)
st.title("模拟退火算法求解tsp")
st.subheader("求解前")
s = [i for i in range(0, m.N)]
p1 = plt.figure()
for i in range(1, m.N):
    plt.plot(m.city[i][0], m.city[i][1], 'o')
    # plt.plot([m.city[s[i]][0], m.city[s[i - 1]][0]], [m.city[s[i]][1], m.city[s[i - 1]][1]])
plt.plot(m.city[0][0], m.city[0][1], 'o')
# plt.plot([m.city[s[0]][0], m.city[s[m.N - 1]][0]], [m.city[s[0]][1], m.city[s[m.N - 1]][1]])
st.pyplot(p1)

st.subheader("求解后")

# print(m.cnt)
# m.seq
# m.seq_best
if st.button("SA1"):
    time_start = time.time()
    cnt = m.SA()
    time_end = time.time()
    p2 = plt.figure()
    for i in range(1, m.N):
        plt.plot(m.city[i][0], m.city[i][1], 'o')
        plt.plot([m.city[m.seq[i]][0], m.city[m.seq[i - 1]][0]], [m.city[m.seq[i]][1], m.city[m.seq[i - 1]][1]])
    plt.plot(m.city[0][0], m.city[0][1], 'o')
    plt.plot([m.city[m.seq[0]][0], m.city[m.seq[m.N - 1]][0]], [m.city[m.seq[0]][1], m.city[m.seq[m.N - 1]][1]])
    st.pyplot(p2)
    st.text("最优顺序：")
    m.seq_best
    st.text("最优值：{}".format(m.best))
    st.text("总迭代次数：{}" .format(cnt))
    st.text("总时间：{}".format(time_end - time_start))

    p3 = plt.figure()
    plt.plot(m.res)
    st.pyplot(p3)
if st.button("SA2"):
    time_start = time.time()
    c, t, value, res = m2.SA()
    time_end = time.time()
    p4 = plt.figure()
    for i in range(1, m.N):
        plt.plot(m.city[i][0], m.city[i][1], 'o')
        plt.plot([m.city[t[i]][0], m.city[t[i - 1]][0]], [m.city[t[i]][1], m.city[t[i - 1]][1]])
    plt.plot(m.city[0][0], m.city[0][1], 'o')
    plt.plot([m.city[t[0]][0], m.city[t[m.N - 1]][0]], [m.city[t[0]][1], m.city[t[m.N - 1]][1]])
    st.pyplot(p4)
    st.text("最优顺序：")
    t
    st.text("最优值：{}".format(value))
    st.text("总迭代次数：{}".format(c))
    st.text("总时间：{}".format(time_end - time_start))
    p5 = plt.figure()
    plt.plot(res)
    st.pyplot(p5)
if st.button("SA3"):
    time_start = time.time()
    c, t, value, res = m3.SA()
    time_end = time.time()
    p6 = plt.figure()
    for i in range(1, m.N):
        plt.plot(m.city[i][0], m.city[i][1], 'o')
        plt.plot([m.city[t[i]][0], m.city[t[i - 1]][0]], [m.city[t[i]][1], m.city[t[i - 1]][1]])
    plt.plot(m.city[0][0], m.city[0][1], 'o')
    plt.plot([m.city[t[0]][0], m.city[t[m.N - 1]][0]], [m.city[t[0]][1], m.city[t[m.N - 1]][1]])
    st.pyplot(p6)
    st.text("最优顺序：")
    t
    st.text("最优值：{}".format(value))
    st.text("总迭代次数：{}".format(c))
    st.text("总时间：{}".format(time_end - time_start))
    p7 = plt.figure()
    plt.plot(res)
    st.pyplot(p7)