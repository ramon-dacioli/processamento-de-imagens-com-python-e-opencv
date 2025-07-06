import cv2

# Função de callback do mouse
def mostrar_coordenadas(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        img_copy = imagem.copy()
        b, g, r = imagem[y, x]
        texto = f'X:{x} Y:{y} R:{r} G:{g} B:{b}'
        cv2.rectangle(img_copy, (0, 0), (400, 30), (0, 0, 0), -1)
        cv2.putText(img_copy, texto, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow('Imagem', img_copy)

imagem = cv2.imread('imagens/imagem.jpg')

cv2.namedWindow('Imagem')
cv2.setMouseCallback('Imagem', mostrar_coordenadas)

print(imagem[0][0])

imagem[0][0] = (255, 255, 255)

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)