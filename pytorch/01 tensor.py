# -*- coding: utf-8 -*-
"""
□ 참고 : https://076923.github.io/posts/Python-pytorch-2/
□ 기능 : tensor
□ 목적 : tensor 학습
"""
#%%
import torch
print(torch.__version__)
print(torch.cuda.is_available())  # True
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)  # cuda:0
#%%
# tensor
print(torch.tensor([1, 2, 3]))
print(torch.Tensor([[1, 2, 3], [4, 5, 6]]))
print(torch.LongTensor([1, 2, 3]))
print(torch.FloatTensor([1, 2, 3]))
#------------------------------------------
# tensor 속성
tensor = torch.rand(3, 2)

print(tensor)
print(tensor.shape)
print(tensor.dtype)
print(tensor.device)
#------------------------------------------
# tensor 차원 변경
tensor = torch.rand(2, 3)
print(tensor)
tensor = tensor.reshape(3, 2)
print(tensor)
#------------------------------------------
# 연산 장치 설정
device = 'cuda' if torch.cuda.is_available() else 'cpu'

cpu = torch.FloatTensor([1, 2, 3])
gpu = torch.cuda.FloatTensor([1, 2, 3])
tensor = torch.rand((1, 1), device=device)

print(device)
print(cpu)
print(gpu)
print(tensor)
#------------------------------------------
# 연산 장치 변경
cpu = torch.FloatTensor([1, 2, 3])
gpu = cpu.cuda()
gpu2cpu = gpu.cpu()

print(cpu)
print(gpu)
print(gpu2cpu)
#------------------------------------------
# numpy 변환
import numpy as np

print(torch.tensor(np.array([1, 2, 3], dtype=np.uint8)))
print(torch.Tensor(np.array([1, 2, 3], dtype=np.uint8)))
print(torch.from_numpy(np.array([1, 2, 3], dtype=np.uint8)))

# tensor 변환
tensor = torch.cuda.FloatTensor([1, 2, 3])
ndarray = tensor.detach().cpu().numpy()
print(ndarray)
#%%