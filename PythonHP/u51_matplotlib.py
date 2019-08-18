import matplotlib.pyplot  as plt

# 绘制折线图
# input_values = [1,2,3,4,5]
# square = [1,4,9,16,25]
# # plt.plot(square,linewidth=5) # 设置线宽
#
# # 设置标题，并添加标签
# plt.title('Square Number',fontsize=24)
# plt.xlabel('Value',fontsize=14)
# plt.ylabel('Square Value',fontsize=14)
#
# # 设置刻度标记大小
# plt.tick_params(axis='both',labelsize=14)
# plt.plot(input_values,square,linewidth = 5)
#
# plt.show()

# 绘制散点图
# plt.scatter(2,4,s=200)

# 绘制一系列点
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s = 100)

# 自动计算数据
x_values = list(range(1,1001))
y_values = [x**2 for x in list(range(1,1001))]

# plt.scatter(x_values,y_values,c = 'red',edgecolor = 'none',s = 40)
# 颜色映射
plt.scatter(x_values,y_values,c = y_values, cmap=plt.cm.Blues,edgecolors='none',s = 40) # 设置蓝色渐变
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000]) # 设置x轴，y轴

plt.title('Scatter',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Value',fontsize = 14)
# plt.tick_params(axis='both',which = 'major',labelsize = 14)

plt.show()
plt.savefig('square_plog.png',bbox_inches= 'tight')