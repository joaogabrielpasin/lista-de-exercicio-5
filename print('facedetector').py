import numpy as np
import cv2
classificador =cv2.CascadeClassifier('D:\Microsoft VS Code\py\opencv\haarcascades\haarcascade_frontalface_default.xml')
imagem = cv2.imread('D:\Microsoft VS Code\py\opencv\img.jpeg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
facesDetectadas = classificador.detectMultiScale(imagemCinza)
print(len(facesDetectadas))
print((facesDetectadas))
for (x, y, l, a) in facesDetectadas:
    print (x, y, l, a)
cv2.rectangle(imagem, (x,y), (x + l, y + a), (0, 0, 255), 2)
cv2.imshow("Faces Encontradas", imagem)