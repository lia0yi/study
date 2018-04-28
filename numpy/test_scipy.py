import numpy as np  
from scipy.misc import imread, imresize  
import matplotlib.pyplot as plt  
  
img = imread('D:/py_t/study/numpy/assets/cat_tinted.jpg')  
img_tinted = img * [1, 0.95, 0.9]  
  
# 显示原始图片  
plt.subplot(1, 2, 1)  
plt.imshow(img)  
  
# 显示调色后的图片  
plt.subplot(1, 2, 2)  
plt.imshow(np.uint8(img_tinted))  
  
plt.show()  