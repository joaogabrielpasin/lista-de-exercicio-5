import numpy as np
import cv2
print(cv2.__version__)
imagem = cv2.imread('D:\Microsoft VS Code\py\opencv\img.jpeg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", imagem)
cv2.imshow("Cinza", imagemCinza)
cv2.waitKey()