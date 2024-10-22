import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
img = cv2.imread('Lineas_Circulos.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque para reducir el ruido
gray = cv2.medianBlur(gray, 5)

# Detectar circunferencias con la transformada de Hough
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                        param1=50, param2=50, minRadius=0, maxRadius=0)

# Dibujar las circunferencias detectadas
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# Mostrar la imagen utilizando matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Ocultar los ejes
plt.show()
