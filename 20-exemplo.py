import cv2

imagem = cv2.imread('imagens/imagem.jpg')

(b, g, r) = cv2.split(imagem)

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Azul", b)
cv2.imshow("Imagem Verde", g)
cv2.imshow("Imagem Vermelho", r)

cv2.waitKey(0)