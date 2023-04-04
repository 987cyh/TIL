# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/55580
□ 기능 : Logistic Regression
□ 목적 : Logistic Regression 학습
"""
#%%
import torch
import pandas as pd
from torch import nn
from torch import optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, TensorDataset
print(torch.__version__)  # 2.0.0
print(torch.cuda.is_available())  # True
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)  # cuda:0
#%%
torch.manual_seed(1)

x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)
#%%
W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

hypothesis = torch.sigmoid(x_train.matmul(W) + b)  # 1 / (1 + torch.exp(-(x_train.matmul(W) + b)))
print(hypothesis)
print(y_train)
#%%
losses = -(y_train * torch.log(hypothesis) + (1 - y_train) * torch.log(1 - hypothesis))
print(losses)
cost = losses.mean()
print(cost)

F.binary_cross_entropy(hypothesis, y_train)
#%%
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

# 모델 초기화
W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# optimizer 설정
optimizer = optim.SGD([W, b], lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs + 1):

    # Cost 계산
    hypothesis = torch.sigmoid(x_train.matmul(W) + b)
    cost = -(y_train * torch.log(hypothesis) +
             (1 - y_train) * torch.log(1 - hypothesis)).mean()

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(
            epoch, nb_epochs, cost.item()
        ))
#%%
hypothesis = torch.sigmoid(x_train.matmul(W) + b)
print(hypothesis)

prediction = hypothesis >= torch.FloatTensor([0.5])
print(prediction)

print(W)
print(b)
#%%