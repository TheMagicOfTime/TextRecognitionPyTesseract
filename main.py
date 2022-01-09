import numpy as np
import pyautogui
import cv2
import pytesseract
import keyboard
import mouse
from googletrans import Translator

while 1 == 1:
	if keyboard.read_key('left alt'):
		CoordinatesBeg = mouse.get_position()
		keyboard.wait('left alt')
		CoordinatesEnd = mouse.get_position()
		x1 = CoordinatesBeg[0]
		x2 = CoordinatesEnd[0]
		if x1 > x2:
			x1, x2 = x2, x1
		y1 = CoordinatesBeg[1]
		y2 = CoordinatesEnd[1]
		if y1 > y2:
			y1, y2 = y2, y1
		print(CoordinatesBeg, CoordinatesEnd)
		image = pyautogui.screenshot(region=(x1,y1, x2 - x1, y2 - y1))
		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
		cv2.imwrite("pic.png", image)

		# Путь для подключения tesseract
		pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
		# Подключение фото
		img = cv2.imread('pic.png')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# Будет выведен весь текст с картинки
		config = r'--oem 3 --psm 6'
		RecognitionText = pytesseract.image_to_string(img, config=config)
		if len(RecognitionText) > 2:
			translator = Translator()
			result = translator.translate(RecognitionText, src='en', dest='ru')
			print(result.text)