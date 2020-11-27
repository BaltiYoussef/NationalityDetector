import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("test.png")
#pytesseract only accept RGB values, and open cv read it BGR, so we have to convert it.
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow('Result',img)
cv2.waitKey(0)
img = cv