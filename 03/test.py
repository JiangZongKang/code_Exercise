import torch




x = torch.unsqueeze(torch.linspace(-1,1,100),dim=1)

print(x.size())