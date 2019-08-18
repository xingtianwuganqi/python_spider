import tesserocr
from PIL import Image

# image = Image.open("code.jpg")
# result = tesserocr.image_to_text(image)
# print(result)

img = Image.open('code.jpg')
img = img.convert('L') # 转灰度 有时间应为彩色横线的诱导致使无法正确识别，这个时候就要转灰度
# img.show()
# img = img.convert("1") # 二值化处理
# img.show()

# 设置二值化 的 阈值

threshold = 167
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

img = img.point(table,'1')
img.show()
result1 = tesserocr.image_to_text(img)
print(result1)
