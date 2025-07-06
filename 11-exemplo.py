import cv2

imagem = cv2.imread('imagens/imagem.jpg')

branco = (255,255,255)

for i in range(0, imagem.shape[0], 20):
    for j in range(0, imagem.shape[1], 20):
        imagem[i:i+5, j:j+5] = branco

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)