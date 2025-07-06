import cv2

imagem = cv2.imread('imagens/imagem.jpg')

cv2.imshow("Imagem", imagem)

for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        for h in range(0, 3):
            print(imagem[i][j][h])