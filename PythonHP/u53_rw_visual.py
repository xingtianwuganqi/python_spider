import matplotlib.pyplot as plt
from u52_random_walk import RandomWalk

rw = RandomWalk(10000)
rw.fill_walk()

# plt.scatter(rw.x_values,rw.y_values,s = 10)
# 给点着色
point_number = list(range(rw.number_points))
plt.scatter(rw.x_values,rw.y_values,c = point_number,cmap=plt.cm.Blues,edgecolors='none',s=10)
# 突出起点和终点
plt.scatter(0,0,c = 'green',edgecolors='none',s = 15)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors='none',s = 15)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# 设置窗口大小
plt.figure(figsize=(10,6))

plt.show()