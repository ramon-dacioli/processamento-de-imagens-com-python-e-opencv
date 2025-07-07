import cv2

imagem = cv2.imread('imagens/imagem.jpg')

fonte = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagem, "Ramon", (50,50), fonte, 2, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)