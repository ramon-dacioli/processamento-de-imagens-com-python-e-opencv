import cv2

imagem = cv2.imread('imagens/imagem.jpg')

imagemrotacionada = imagem[::-1, :]

cv2.imshow("Imagem", imagem)
cv2.imshow("Imagemrotacionada", imagemrotacionada)
cv2.waitKey(0)