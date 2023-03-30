# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-pytorch-13/, https://wikidocs.net/60002
□ 기능 : Multiclass Classification / softmax
□ 목적 : Multiclass Classification / softmax 학습
"""
#%%
import torch
import pandas as pd
from torch import nn
import torch.nn.functional as F
from torch import optim
from torch.utils.data import Dataset, DataLoader
print(torch.__version__)  # 2.0.0
print(torch.cuda.is_available())  # True
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)  # cuda:0
#%%
class CustomDataset(Dataset):
    def __init__(self, file_path):
        df = pd.read_csv(file_path)
        self.a = df.iloc[:, 0].values
        self.b = df.iloc[:, 1].values
        self.c = df.iloc[:, 2].values
        self.y = df.iloc[:, 3].values
        self.y = list(map(self.string_to_vector, self.y))
        self.length = len(df)

    def string_to_vector(self, value):
        data = {"acute triangle": 0, "right triangle": 1, "obtuse triangle": 2}
        return data.get(value, None)

    def __getitem__(self, index):
        x = torch.FloatTensor(sorted([self.a[index], self.b[index], self.c[index]]))
        y = torch.LongTensor(self.y)[index]
        return x, y

    def __len__(self):
        return self.length

class CustomModel(nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()

        self.layer = nn.Sequential(
            nn.Linear(3, 3)
        )

    def forward(self, x):
        x = self.layer(x)
        return x
#%%
import os
os.chdir("C:/Users/big7/PycharmProjects/TIL/pytorch")

train_dataset = CustomDataset("./dataset_mulit.csv")
train_dataloader = DataLoader(train_dataset, batch_size=128, shuffle=True, drop_last=True)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = CustomModel().to(device)
criterion = nn.CrossEntropyLoss().to(device)
optimizer = optim.SGD(model.parameters(), lr=0.001)

for epoch in range(10000):
    cost = 0.0

    for x, y in train_dataloader:
        x = x.to(device)
        y = y.to(device)

        output = model(x)
        loss = criterion(output, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        cost += loss

    cost = cost / len(train_dataloader)

    if (epoch + 1) % 1000 == 0:
        print(f"Epoch : {epoch + 1:4d}, Cost : {cost:.3f}")

with torch.no_grad():
    model.eval()
    classes = {0: "acute triangle", 1: "right triangle", 2: "obtuse triangle"}
    inputs = torch.FloatTensor([
        [9.02, 9.77, 9.96],  # 0 | acute triangle
        [8.01, 8.08, 8.32],  # 0 | acute triangle
        [3.55, 5.15, 6.26],  # 1 | right triangle
        [3.32, 3.93, 5.14],  # 1 | right triangle
        [4.39, 5.56, 9.99],  # 2 | obtuse triangle
        [3.01, 3.08, 9.98],  # 2 | obtuse triangle
        [5.21, 5.38, 5.39],  # 0 | acute triangle
        [3.85, 6.23, 7.32],  # 1 | right triangle
        [4.16, 4.98, 8.54],  # 2 | obtuse triangle
    ]).to(device)
    outputs = model(inputs)

    print('---------')
    print(outputs)
    print(torch.round(F.softmax(outputs, dim=1), decimals=2))
    print(outputs.argmax(1))
    print(list(map(classes.get, outputs.argmax(1).tolist())))
#%%
