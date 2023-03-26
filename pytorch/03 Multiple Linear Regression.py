# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-pytorch-7/, https://wikidocs.net/53560
□ 기능 : 다중선형회귀(Multiple Linear Regression)
□ 목적 : 다중선형회귀(Multiple Linear Regression) 학습
"""
#%%
import torch
print(torch.__version__)
print(torch.cuda.is_available())  # True
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)  # cuda:0
#%%
import torch
from torch import nn
from torch import optim
#%%
# 단순 선형 회귀(Simple Linear Regression)

x = torch.FloatTensor([
    [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
    [11], [12], [13], [14], [15], [16], [17], [18], [19], [20],
    [21], [22], [23], [24], [25], [26], [27], [28], [29], [30]
])
y = torch.FloatTensor([
    [0.94], [1.98], [2.88], [3.92], [3.96], [4.55], [5.64], [6.3], [7.44], [9.1],
    [8.46], [9.5], [10.67], [11.16], [14], [11.83], [14.4], [14.25], [16.2], [16.32],
    [17.46], [19.8], [18], [21.34], [22], [22.5], [24.57], [26.04], [21.6], [28.8]
])

model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

for epoch in range(10000):
    output = model(x)
    cost = criterion(output, y)

    # gradient를 0으로 초기화
    optimizer.zero_grad()
    # 비용 함수를 미분하여 gradient 계산
    cost.backward()
    # W와 b를 업데이트
    optimizer.step()

    if (epoch + 1) % 1000 == 0:
        print(f"Epoch : {epoch+1:4d}, Model : {list(model.parameters())}, Cost : {cost:.3f}")
#%%
# 다변량 다중 선형 회귀(Multivariate Multiple Linear Regression)

x = torch.FloatTensor([
    [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]
])
y = torch.FloatTensor([
    [0.1, 1.5], [1.0, 2.8], [1.9, 4.1], [2.8, 5.4], [3.7, 6.7], [4.6, 8.0]
])

model = nn.Linear(2, 2)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)

for epoch in range(10000):
    output = model(x)
    cost = criterion(output, y)

    # gradient를 0으로 초기화
    optimizer.zero_grad()
    # 비용 함수를 미분하여 gradient 계산
    cost.backward()
    # W와 b를 업데이트
    optimizer.step()

    if (epoch + 1) % 1000 == 0:
        print(f"Epoch : {epoch+1:4d}, Model : {list(model.parameters())}, Cost : {cost:.3f}")
#%%