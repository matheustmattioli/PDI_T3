import numpy as np
import matplotlib.pyplot as plt

def flood_fill(img):
    num_rows, num_cols = img.shape
    img_rotulo = np.zeros((num_rows, num_cols), dtype=int)
    current_label = 1        # rótulo atual a ser associado a um novo componente

    for row in range(num_rows):
        for col in range(num_cols):
            if img[row, col] == 1 and img_rotulo[row, col] == 0:
                fila = []
                fila.append((row, col))
                
                img_rotulo[row, col] = current_label
                while(len(fila) > 0):
                    current_index = fila.pop(0)
                        
                    vizinhanca = [
                        (current_index[0], current_index[1] + 1),
                        (current_index[0] + 1, current_index[1]),
                        (current_index[0], current_index[1] - 1),
                        (current_index[0] - 1, current_index[1]),
                    ]

                    for v in vizinhanca:
                        if v[0] >= 0 and v[1] >= 0 and v[0] < num_rows and v[1] < num_cols:                        
                            if img[v] == 1 and img_rotulo[v] == 0:
                                img_rotulo[v] = current_label
                                fila.append(v)

                current_label += 1
                
    return img_rotulo
                
img = plt.imread('componentes.tiff')
img = img>0    

img_rotulo = flood_fill(img)

plt.imshow(img_rotulo)
plt.show()