# picprocess
from PIL import Image
import numpy as np
im0 = np.array(Image.open('m.jpeg').convert('L')) #按比例转换为灰度图
im1 = 255 - im0 #反变换
im2 = (100/255)*im0 + 150 #区间变换
im3 = 255*(im1/255)**2 #像素平方处理
pil_im0 = Image.fromarray(np.uint8(im0))
pil_im1 = Image.fromarray(np.uint8(im1))
pil_im2 = Image.fromarray(np.uint8(im2))
pil_im3 = Image.fromarray(np.uint8(im3))
pil_im0.save('100.jpeg')
pil_im1.save('101.jpeg')
pil_im2.save('102.jpeg')
pil_im3.save('103.jpeg')
