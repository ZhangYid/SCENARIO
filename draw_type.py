import numpy as np

import matplotlib.pyplot as plt

import matplotlib as mpl


np.set_printoptions(suppress=True)

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负

data = [
    [17.60747671,13.14299960],
    [26.35822739,16.88936519],
    [35.23943992,17.47385671],
    [38.38251459,18.30926880]
]
data1 = [
    [6.09497241,5.85802540],
    [12.99302859,9.93767590],
    [23.70753571,15.27280910],
    [38.38351459,18.30926880]
]
data2 = [
    [37.92574408,16.23158030],
    [28.32549800,10.18801832],
    [6.461048293,8.18657550],
    [32.18373839,14.04888710]
]

#ys=['25% nodes(5431)','50% nodes(10863)','75% nodes(16295)','All nodes(21726)']
#ys=['25%','50%','75%','100%']
ys=['Drug','GO Term','miRNA','Phenotype']
mpl.rc('font', family='Times New Roman')
mpl.rcParams.update({'font.size': 35})
def DrawGeoDtaabse(rcount, y):
    ax1 = plt.subplot(2, 1, 1)
    plt.sca(ax1)
    plt.figure(figsize=(10, 10))
    plt.xlabel("Type of Removed Objects")  # X轴标签
    plt.ylabel("Run Time/s")  # Y轴标签
    plt.xticks(fontsize=32)
    #plt.legend()  # 显示图例
    #plt.title("[读取]效率")  # 标题

    x1 = [1, 5, 9, 13]  # x轴点效率位置
    x3=[i+0.5 for i in x1]
    x2 = [i + 1 for i in x1]  # x轴线效率位置
    y1 = [i[1] for i in rcount]  # y轴点效率位置
    y2 = [i[0] for i in rcount]  # y轴线效率位置

    # plt.plot(y,  # x轴数据
    #         y2,  # y轴数据
    #         linestyle='-',  # 折线类型
    #         linewidth=4,  # 折线宽度
    #         color='red',  # 折线颜色
    #         marker='v',  # 点的形状
    #         markersize=14,  # 点的大小
    #         markeredgecolor='red',  # 点的边框色
    #         markerfacecolor='red',  # 点的填充色
    #         label='SCENARIO')  # 添加标签
    # plt.plot(y,  # x轴数据
    #          y1,  # y轴数据
    #          linestyle='--',  # 折线类型
    #          linewidth=4,  # 折线宽度
    #          color='blue',  # 折线颜色
    #          marker='s',  # 点的形状
    #          markersize=14,  # 点的大小
    #          markeredgecolor='blue',  # 点的边框色
    #          markerfacecolor='blue',  # 点的填充色
    #          label='SCENARIO-Single')  # 添加标签

    mpl.rc('hatch',linewidth=2)
    y0 = ["", "", "", ""]
    plt.bar(x1, y1, alpha=0.7, width=1, edgecolor='red', color='red', label="SCENARIO", tick_label=y0)
    plt.bar(x2, y2, alpha=0.7, width=1, edgecolor='blue', color='white', label="SCENARIO-Single", tick_label=y,
            hatch='//',linewidth=2)



    plt.ylim(0, 40)
    # 至此第一行的读取效率绘制完毕,再重复一下第二行的写效率
    plt.rcParams['legend.handlelength'] = 1
    plt.rcParams['legend.handleheight'] = 1.125
    plt.legend(loc='upper center', fontsize=30)
    #plt.legend()
    #plt.show()
    plt.savefig('type.pdf')


DrawGeoDtaabse(data2, ys)

