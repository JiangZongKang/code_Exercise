from matplotlib import pyplot as plt 
import random

x = range(0,120)
y = [random.randint(20,35) for x in range(120)]


plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

# 调整x轴的刻度
plt.show()