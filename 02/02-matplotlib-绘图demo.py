from matplotlib import pyplot as plt 

x = range(2,26,2)
y = [15,13,14,5,17,20,25,26,27,22,18,15]

# 设置图片的大小
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.plot(x,y)

# 绘制x轴、y轴的刻度
plt.xticks([x/2 for x in range(4,49,3)])
plt.yticks(range(min(y),max(y)+1))

# 保存
plt.savefig('./t1.png')

# 展示图形
plt.show()