import torch
import torch.nn.functional as f 
import matplotlib.pyplot as plt 
from torch.autograd import Variable

n_data = torch.ones(100,2)
x0 = torch.normal(2*n_data,1)
y0 = torch.zeros(100)
x1 = torch.normal(-2*n_data,1)
y1 = torch.ones(100)
x = torch.cat((x0,x1),0).type(torch.FloatTensor)
y = torch.cat((y0,y1),).type(torch.LongTensor)


# 用Variable 来修饰这些数据 tensor
x, y = torch.autograd.Variable(x),Variable(y)

# 画图
# plt.scatter(x.data.numpy(),y.data.numpy())
# plt.show()

# 建立神经网络
class Net(torch.nn.Module): # 继承torch 的Module
    def __init__(self,n_feature,n_hidden,n_output):
        super(Net,self).__init__()  # 继承 __init__ 功能
        # 定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_feature,n_hidden) # 隐藏层的线性输出
        self.predict = torch.nn.Linear(n_hidden,n_output) # 输出层的线性输出
    
    def forward(self, x): # 这同时也是Module 中的 forwaed功能
        # 正向传播输入值，神经网络分析输出值
        x = f.relu(self.hidden(x))
        x = self.predict(x)
        return x 

        

net = Net(n_feature=2,n_hidden=10,n_output=2)
print(net)

# 快速搭建神经网络
net2 = torch.nn.Sequential(
    torch.nn.Linear(2,10),
    torch.nn.ReLU(),
    torch.nn.Linear(10,2)
)

# 训练网络
# optimizer 是训练的工具  ----->优化器
optimizer = torch.optim.SGD(net.parameters(),lr=0.02) # 传入 net 的所有参数，学习率
loss_func = torch.nn.CrossEntropyLoss()  # 预测值和真实值的误差计算公式(均方差)

for t in range(100):
    out = net(x)
    loss = loss_func(out,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    pred = torch.max(f.softmax(out),1)[1]
    pred_y = pred.data.numpy().squeeze()
    target_y = y.data.numpy()
    accuracy = sum(pred_y == target_y)/200
    # print(accuracy)


torch.save(net,'net.pkl')

def restore():
    net3 = torch.load('net.pkl')