import cv2

imagem = cv2.imread('imagens/imagem.jpg')

imagemrecortada = imagem[100:200, 100:400]

cv2.imshow("Imagem", imagem)
cv2.imshow("ImagemRecortada", imagemrecortada)
cv2.waitKey(0)