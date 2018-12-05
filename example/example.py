import sys
sys.path.append('../')
import cv2
from object_detector_cocossd import classifyImg
import base64

#------------------------ДЛЯ ПРИМЕРА------------------------------
#Переводим картинку в base64

#Загрузить картинку из файла
#Конвертировать закодированную jpg картинку в base64
#Преобразовать последовательность байт в строку
with open("bill.jpg", "rb") as image_file:
	base64data = base64.b64encode(image_file.read())
	base64data = "".join(map(chr, base64data))
#-----------------------------------------------------------------

print(classifyImg(base64data)[0]) #Объекты

print(classifyImg(base64data)[1]) #Лица
