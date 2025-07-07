import cv2

imagem = cv2.imread('imagens/imagem.jpg')

largura = imagem.shape[1]
altura = imagem.shape[0]
proporcao = float(altura / largura)

larguraNova = 150;
alturaNova = int(larguraNova * proporcao);

imagem = cv2.resize(imagem, (larguraNova, alturaNova))

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)