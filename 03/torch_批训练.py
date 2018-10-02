import torch
import torch.utils.data as data

Batch_size = 8

x = torch.linspace(1,10,10)
y = torch.linspace(10,1,10)

torch_dataset = data.TensorDataset(x,y)
loader = data.DataLoader(
    dataset=torch_dataset,
    batch_size=Batch_size,
    shuffle=True, # 打乱数据的排列顺序
    # num_workers=2
)

for epoch in range(3):
    for step,(batch_x,batch_y) in enumerate(loader):
        print('Epoch:',epoch,'|Step:',step,'|batch_x:',batch_x.numpy(),'|batch_y:',batch_y.numpy())