# Детектор объектов и лиц
## Использование:

classifyImg(base64 код изображения)[0]; //Объекты

classifyImg(base64 код изображения)[1]; //Лица

## В файле object_detector_cocossd.py.
confidence_objects = 0.5 #минимальный доверительный порог для вывода объектов
confidence_faces = 0.5 #минимальный доверительный порог для вывода лиц