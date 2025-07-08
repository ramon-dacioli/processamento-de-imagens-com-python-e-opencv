import cv2

imagem = cv2.imread('imagens/imagem.jpg')

branco = (255,255,255)

for i in range(0, imagem.shape[0], 15):
    for j in range(0, imagem.shape[1], 15):
        imagem[i:i+3, j:j+3] = branco

suave = cv2.medianBlur(imagem, 5)
suave2 = cv2.medianBlur(imagem, 11)

cv2.imshow("Original", imagem)
cv2.imshow("Imagem", suave)
cv2.imshow("Imagem2", suave2)
cv2.waitKey(0)