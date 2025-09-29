## 导入 cv2 和 pytesseract
import cv2     # 图像处理
import pytesseract    # 文字OCR

# 图片加载进来 ,保存在image当中
image = cv2.imread(r"C:\Users\ASUS\Desktop\2.png")
#灰度图
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#二值化  cv2.threshold 第一个参数是原图，第二个参数是阈值，第三个参数是最大值，第四个参数是阈值类型
_, binary_image = cv2.threshold(gray_image,10,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)


#调用pytesseract-OCR接口识别文字  阿里云OCR  百度OCR  腾讯OCR  谷歌OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(binary_image, lang='chi_sim')
text = text.replace(' ','')
print(text)
# 摄像头！   开关拍照  识别完了之后  保存在文档里面
# 显示图片
window = cv2.namedWindow('IMAGE')
cv2.imshow('IMAGE',binary_image)
cv2.waitKey()

