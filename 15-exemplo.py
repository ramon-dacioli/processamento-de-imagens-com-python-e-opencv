import cv2

imagem = cv2.imread('imagens/imagem.jpg')

larguraNova = 200;
alturaNova = 200;

imagem = cv2.resize(imagem, (larguraNova, alturaNova))

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)