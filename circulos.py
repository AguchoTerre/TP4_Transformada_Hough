import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
img = cv2.imread('Imagen_a_identificar.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque para reducir el ruido
gray = cv2.medianBlur(gray, 5)

# Detectar circunferencias con la transformada de Hough
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 
                           dp=1, 
                           minDist=50, 
                           param1=100, 
                           param2=30, 
                           minRadius=8, 
                           maxRadius=100)

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
