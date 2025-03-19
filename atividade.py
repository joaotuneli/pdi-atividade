import cv2
import numpy as np

image = cv2.imread('foto.jpg')

# Gerar a máscara aleatória com RM
rm = 93530
np.random.seed(rm)
mask = np.random.randint(2, size=image.shape[:2], dtype=np.uint8)

processed_image = image * mask[:, :, np.newaxis]

cv2.imwrite('foto_93530.png', processed_image)

cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()