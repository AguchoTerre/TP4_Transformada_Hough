import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
img = cv2.imread('Lineas_Circulos.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Transformada de Hough para rectas
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Dibujar las rectas detectadas
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        x2 = int(x0 - 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar la imagen utilizando matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Ocultar los ejes
plt.show()
