import cv2

imagem = cv2.imread('imagens/imagem.jpg')

print(imagem.shape[0]) #altura da imagem em pixel
print(imagem.shape[1]) #largura da imagem em pixel
print(imagem.shape[2]) #canais de cores da imagem