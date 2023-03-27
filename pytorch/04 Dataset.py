# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-pytorch-8/, https://wikidocs.net/53560
□ 기능 : Dataset
□ 목적 : Dataset 학습
"""
#%%
import torch
from torch import nn
from torch import optim
from torch.utils.data import TensorDataset, DataLoader
print(torch.__version__)  # 2.0.0
print(torch.cuda.is_available())  # True
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)  # cuda:0
#%%
# TensorDataset
train_x = torch.FloatTensor([
    [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]
])
train_y = torch.FloatTensor([
    [0.1, 1.5], [1, 2.8], [1.9, 4.1], [2.8, 5.4], [3.7, 6.7], [4.6, 8]
])

train_dataset = TensorDataset(train_x, train_y)  # TensorDataset
train_dataloader = DataLoader(train_dataset, batch_size=2, shuffle=True, drop_last=True)

model = nn.Linear(2, 2, bias=False)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

for epoch in range(20000):
    cost = 0.0

    for batch in train_dataloader:
        x, y = batch
        output = model(x)

        loss = criterion(output, y)

        # gradient를 0으로 초기화
        optimizer.zero_grad()
        # 비용 함수를 미분하여 gradient 계산
        cost.backward()
        # W와 b를 업데이트
        optimizer.step()

        cost += loss

    cost = cost / len(train_dataloader)

    if (epoch + 1) % 1000 == 0:
        print(f"Epoch : {epoch + 1:4d}, Model : {list(model.parameters())}, Cost : {cost:.3f}")
#%%