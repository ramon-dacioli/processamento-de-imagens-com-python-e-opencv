import cv2

imagem = cv2.imread('imagens/imagem.jpg')

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)