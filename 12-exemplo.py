import cv2

imagem = cv2.imread('imagens/imagem.jpg')

branco = (255,255,255)

for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][0] == 255: #alterar o valor azul para branco
            imagem[i][j] = branco

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)