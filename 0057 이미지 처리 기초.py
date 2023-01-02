# -*- coding: utf-8 -*-
"""
□ 이미지 처리 기초 이해(학습), 학습이외의 목적은 無
□ 참고: https://datascienceschool.net/03%20machine%20learning/03.02.01%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%B2%98%EB%A6%AC%20%EA%B8%B0%EC%B4%88.html
□ 도시군기본계획의 도시군 기본구상도 shp구축을 위한 첫 단계
"""
#%%
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)  # UserWarning 제거
warnings.simplefilter(action='ignore', category=FutureWarning)  # UserWarning 제거
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False # 음수(마이너스) 깨짐
#%%
import scipy as sp

img_gray = sp.misc.face(gray=True)
img_gray.shape
sns.heatmap(img_gray[:15, :15], annot=True, fmt="d", cmap=plt.cm.bone)
plt.axis("off")
plt.show()
#%%
from sklearn.datasets import load_sample_images

dataset = load_sample_images()
img_rgb = dataset.images[1]
img_rgb.shape

plt.figure(figsize=(10, 2))

plt.subplot(141)
plt.imshow(img_rgb[50:200, 50:200, :])
plt.axis("off")
plt.title("RGB 이미지")

plt.subplot(142)
plt.imshow(img_rgb[50:200, 50:200, 0], cmap=plt.cm.bone)
plt.axis("off")
plt.title("R 채널")

plt.subplot(143)
plt.imshow(img_rgb[50:200, 50:200, 1], cmap=plt.cm.bone)
plt.axis("off")
plt.title("G 채널")

plt.subplot(144)
plt.imshow(img_rgb[50:200, 50:200, 2], cmap=plt.cm.bone)
plt.axis("off")
plt.title("B 채널")

plt.show()
#%%
from matplotlib.colors import hsv_to_rgb

V, H = np.mgrid[0:1:100j, 0:1:360j]
S = np.ones_like(V)

HSV_S100 = np.dstack((H, S * 1.0, V))
RGB_S100 = hsv_to_rgb(HSV_S100)
HSV_S20 = np.dstack((H, S * 0.2, V))
RGB_S20 = hsv_to_rgb(HSV_S20)

HSV_S20.shape
#%%
# 색상(Hue)
HSV_S20[:4, :5, 0]
# 채도(Saturation)
HSV_S20[:4, :5, 1]
# 명도(Value)
HSV_S20[:4, :5, 2]
#%%
plt.subplot(211)
plt.imshow(RGB_S100, origin="lower", extent=[0, 360, 0, 1], aspect=80)
plt.xlabel("색상(Hue)")
plt.ylabel("명도(Value)")
plt.title("채도(Saturation) 100일 때의 색공간")
plt.grid(False)

plt.subplot(212)
plt.imshow(RGB_S20, origin="lower", extent=[0, 360, 0, 1], aspect=80)
plt.xlabel("색상(Hue)")
plt.ylabel("명도(Value)")
plt.title("채도(Saturation) 20일 때의 색공간")
plt.grid(False)

plt.tight_layout()
plt.show()
#%%
from PIL import Image

img_logo_png = Image.open("./logo.png")
img_logo_png.size
img_logo_png.save("./logo.bmp")
img_logo_bmp = Image.open("./logo.bmp")
#%%
img_logo_array = np.array(img_logo_bmp)
plt.imshow(img_logo_array)
plt.axis("off")
plt.show()
#%%
Image.fromarray(img_logo_array)
img_logo_png2 = img_logo_png.resize((300, 100))
img_logo_png2
#%%
img_logo_thumbnail = img_logo_png.copy()
img_logo_thumbnail.thumbnail((150, 50))
img_logo_thumbnail
#%%
img_logo_rotated = img_logo_png.rotate(45)
img_logo_rotated
#%%
img_logo_cropped = img_logo_png.crop((10, 10, 200, 200))
img_logo_cropped
#%%
import skimage.data

img_astro = skimage.data.astronaut()
img_astro.shape

skimage.io.imsave("astronaut.png", img_astro)
img_astro2 = skimage.io.imread("astronaut.png")
#%%
from skimage import color

plt.subplot(131)
plt.imshow(img_astro)
plt.axis("off")
plt.title("RGB")

plt.subplot(132)
plt.imshow(color.rgb2gray(img_astro), cmap=plt.cm.gray)
plt.axis("off")
plt.title("그레이 스케일")

plt.subplot(133)
plt.imshow(color.rgb2hsv(img_astro))
plt.axis("off")
plt.title("HSV")

plt.show()
#%%
