import cv2

imagem = cv2.imread('imagens/imagem.jpg')

for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        imagem[i][j] = (0,0,0)

fonte = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(imagem, '255', (15, 65), fonte, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagem, '70', (125, 65), fonte, 2, (70, 70, 70), 2, cv2.LINE_AA)
cv2.putText(imagem, '100', (225, 65), fonte, 2, (100, 100, 100), 2, cv2.LINE_AA)
cv2.putText(imagem, '1', (405, 65), fonte, 2, (1, 1, 1), 2, cv2.LINE_AA)

for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][0] != 0:
            imagem[i][j] = (255, 255, 255)

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)