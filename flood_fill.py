import numpy as np
import matplotlib.pyplot as plt

def connected_components(img):
    num_rows, num_cols = img.shape
    img_rotulo = np.zeros((num_rows, num_cols), dtype=int)
    current_label = 1        # rótulo atual a ser associado a um novo componente

    for row in range(num_rows):
        for col in range(num_cols):
            if img[row, col] == 1 and img_rotulo[row, col] == 0:
                fila = []
                fila.append((row, col))
                
                # Flood fill
                while(len(fila) > 0):
                    current_index_row, current_index_col = fila.pop(0)
                    img_rotulo[current_index_row, current_index_col] = current_label
                    
                    vizinhanca = [
                        (current_index_row, current_index_col + 1),
                        (current_index_row + 1, current_index_col),
                        (current_index_row, current_index_col - 1),
                        (current_index_row - 1, current_index_col),
                    ]
            
                    for v in vizinhanca:
                        if v[0] >= 0 and v[1] >= 0 and \
                           v[0] < num_rows and v[1] < num_cols:
                           
                           if img[v] == 1 and img_rotulo[v] == 0 and fila.count(v) == 0:
                               fila.append(v)

                current_label += 1
                
    return img_rotulo
                
img_test = np.array([[0, 0, 1, 1],
                     [0, 1, 0, 1],
                     [1, 1, 1, 0]])
img_rotulo = connected_components(img_test)
print(img_rotulo)

img = plt.imread('componentes.tiff')
# Objetos possuem valor 255 na imagem lida, o comando abaixo torna
# a imagem binária, com valores True e False (equivalentemente, 0 e 1)
img = img>0     
img_rotulo = connected_components(img)

plt.imshow(img_rotulo)
print(np.unique(img_rotulo))
plt.show()