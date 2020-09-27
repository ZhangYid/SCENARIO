import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.pyplot import MultipleLocator       #从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
#mport numpy as np
#from pylab import mpl
from matplotlib.font_manager import FontProperties

plt.figure(figsize=(24,8))
plt.subplot(121)
# 设置图框的大小
data1 = pd.read_csv('few1_v.csv',header=0)
data2 = pd.read_csv('few1_t.csv',header=0)
data1=data1.T
data2=data2.T
a = ['MRR','Hits@10','Hits@5','Hits@1']

plt.plot(a,   # x轴数据
         data1[0], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#E87BC0', # 折线颜色
         marker = 'v', # 点的形状
         markersize = 8, # 点的大小
         markeredgecolor='#E87BC0', # 点的边框色
         markerfacecolor='#E87BC0', # 点的填充色
         label = 'RESCAL') # 添加标签


plt.plot(a,   # x轴数据
         data1[1], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#7cd6cf', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 8, # 点的大小
         markeredgecolor='#7cd6cf', # 点的边框色
         markerfacecolor='#7cd6cf', # 点的填充色
         label = 'TransE') # 添加标签

plt.plot(a,   # x轴数据
         data1[2], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#c97937', # 折线颜色
         marker = '+', # 点的形状
         markersize = 8, # 点的大小
         markeredgecolor='#c97937', # 点的边框色
         markerfacecolor='#c97937', # 点的填充色
         label = 'DistMult') # 添加标签


plt.plot(a,   # x轴数据
         data1[3], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#9192ab', # 折线颜色
         marker = 'h', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#9192ab', # 点的边框色
         markerfacecolor='#9192ab', # 点的填充色
         label = 'ComplEx') # 添加标签

plt.plot(a,   # x轴数据
         data1[4], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#CC66CC', # 折线颜色
         marker = 'D', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#CC66CC', # 点的边框色
         markerfacecolor='#CC66CC', # 点的填充色
         label = 'Gmatching (RESCAL)') # 添加标签

plt.plot(a,   # x轴数据
         data1[5], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#7898e1', # 折线颜色
         marker = '*', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#7898e1', # 点的边框色
         markerfacecolor='#7898e1', # 点的填充色
         label = 'Gmatching (TransE)') # 添加标签

plt.plot(a,   # x轴数据
         data1[6], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#00BFFF', # 折线颜色
         marker = 's', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#00BFFF', # 点的边框色
         markerfacecolor='#00BFFF', # 点的填充色
         label = 'Gmatching (DistMult)') # 添加标签

plt.plot(a,   # x轴数据
         data1[7], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#FFA500', # 折线颜色
         marker = 's', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#FFA500', # 点的边框色
         markerfacecolor='#FFA500', # 点的填充色
         label = 'Gmatching (ComplEx)') # 添加标签

plt.plot(a,   # x轴数据
         data1[8], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#EE0000', # 折线颜色
         marker = 's', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#EE0000', # 点的边框色
         markerfacecolor='#EE0000', # 点的填充色
         label = 'Our_Method') # 添加标签
# plt.grid()
# 添加标题和坐标轴标签
plt.xlabel('Metrics', fontdict={'family' : 'Times New Roman', 'size'   : 40,'style':'italic'})
plt.ylabel('', fontdict={'family' : 'Times New Roman', 'size'   : 32})

# x轴 y轴 刻度字体设置
#plt.title('One-shot (valid)', fontdict={'family' : 'Times New Roman', 'size'   : 32},pad=12)
plt.yticks(fontproperties = 'Times New Roman', size = 28)
plt.xticks(fontproperties = 'Times New Roman', size = 28)
plt.legend(ncol=5,prop={'family' : 'Times New Roman', 'size'   : 24},loc=2,bbox_to_anchor=(-0.02,1.3))
#plt.legend()
# 设置坐标轴刻度
# x_major_locator = [3,6,12,24]
# y_major_locator = MultipleLocator(0.2)     #把y轴的刻度间隔设置为0.1，并存在变量里
  # ax为两条坐标轴的实例

# ax.xaxis = [3,6,12,24]
# ax.yaxis.set_major_locator(y_major_locator)   #把y轴的主刻度设置为0.1的倍数

plt.ylim(0, 0.35)

plt.subplot(122)
plt.plot(a,   # x轴数据
         data2[0], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#E87BC0', # 折线颜色
         marker = 'v', # 点的形状
         markersize = 8, # 点的大小
         markeredgecolor='#E87BC0', # 点的边框色
         markerfacecolor='#E87BC0', # 点的填充色
         label = 'RESCAL') # 添加标签


plt.plot(a,   # x轴数据
         data2[1], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#7cd6cf', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 8, # 点的大小
         markeredgecolor='#7cd6cf', # 点的边框色
         markerfacecolor='#7cd6cf', # 点的填充色
         label = 'TransE') # 添加标签

plt.plot(a,   # x轴数据
         data2[2], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#c97937', # 折线颜色
         marker = '+', # 点的形状
         markersize = 8, # 点的大小
         markeredgecolor='#c97937', # 点的边框色
         markerfacecolor='#c97937', # 点的填充色
         label = 'DistMult') # 添加标签

plt.plot(a,   # x轴数据
         data2[3], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#9192ab', # 折线颜色
         marker = 'h', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#9192ab', # 点的边框色
         markerfacecolor='#9192ab', # 点的填充色
         label = 'ComplEx') # 添加标签

plt.plot(a,   # x轴数据
         data2[4], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#CC66CC', # 折线颜色
         marker = 'D', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#CC66CC', # 点的边框色
         markerfacecolor='#CC66CC', # 点的填充色
         label = 'Gmatching (RESCAL)') # 添加标签

plt.plot(a,   # x轴数据
         data2[5], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#7898e1', # 折线颜色
         marker = '*', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#7898e1', # 点的边框色
         markerfacecolor='#7898e1', # 点的填充色
         label = 'Gmatching (TransE)') # 添加标签

plt.plot(a,   # x轴数据
         data2[6], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#00BFFF', # 折线颜色
         marker = 's', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#00BFFF', # 点的边框色
         markerfacecolor='#00BFFF', # 点的填充色
         label = 'Gmatching (DistMult)') # 添加标签

plt.plot(a,   # x轴数据
         data2[7], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#FFA500', # 折线颜色
         marker = 's', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#FFA500', # 点的边框色
         markerfacecolor='#FFA500', # 点的填充色
         label = 'Gmatching (ComplEx)') # 添加标签

plt.plot(a,   # x轴数据
         data2[8], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#EE0000', # 折线颜色
         marker = 's', # 点的形状
         markersize = 9, # 点的大小
         markeredgecolor='#EE0000', # 点的边框色
         markerfacecolor='#EE0000', # 点的填充色
         label = 'Our_Method') # 添加标签
# plt.grid()
# 添加标题和坐标轴标签
plt.xlabel('Metrics', fontdict={'family' : 'Times New Roman', 'size'   : 40,'style':'italic'})
plt.ylabel('', fontdict={'family' : 'Times New Roman', 'size'   : 32})

# x轴 y轴 刻度字体设置
#plt.title('One-shot (valid)', fontdict={'family' : 'Times New Roman', 'size'   : 32},pad=12)
plt.yticks(fontproperties = 'Times New Roman', size = 28)
plt.xticks(fontproperties = 'Times New Roman', size = 28)

# 设置坐标轴刻度
# x_major_locator = [3,6,12,24]
# y_major_locator = MultipleLocator(0.2)     #把y轴的刻度间隔设置为0.1，并存在变量里
  # ax为两条坐标轴的实例

# ax.xaxis = [3,6,12,24]
# ax.yaxis.set_major_locator(y_major_locator)   #把y轴的主刻度设置为0.1的倍数

plt.ylim(0, 0.35)
# plt.legend(ncol=5,prop={'family' : 'Times New Roman', 'size'   : 24},loc=2,bbox_to_anchor=(-0.8,1.3))
# plt.xlim(0.3, 0.8)
# 显示图例
# plt.legend(['HA','Lridge','LRidge','LSVR'],prop={'family' : 'Times New Roman', 'size'   : 20},loc=2,bbox_to_anchor=(0.05,0.93))
# plt.legend(ncol=2,prop={'family' : 'Times New Roman', 'size'   : 16},loc=2,bbox_to_anchor=(0.0,0.26))
# plt.savefig('新图/solar-rse-1024.png',dpi=1024,bbox_inches = 'tight')
# 显示图形

plt.savefig('1.svg',dpi=1024,bbox_inches='tight')
plt.show()