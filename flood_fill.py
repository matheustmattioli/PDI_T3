import numpy as np
import matplotlib.pyplot as plt

# Função que implementa o flood fill para detecção de componentes conexas em uma imagem
def flood_fill(img):
    # Filtro para trabalharmos com imagens de apenas um canal
    if len(img.shape) > 2:
        img = img[:,:,0]

    num_rows, num_cols = img.shape
    # Imagem que terá as componentes conexas devidamente rotuladas
    img_rotulo = np.zeros((num_rows, num_cols), dtype=int)
    # rótulo atual a ser associado a um novo componente
    current_label = 1       

    # Laço principal para percorrer a imagem
    for row in range(num_rows):
        for col in range(num_cols):
            if img[row, col] == 1 and img_rotulo[row, col] == 0:
                # Se encontrou um objeto que ainda não foi rotulado
                fila = [] # fila de próximos pixels a serem visitados
                fila.append((row, col))
                
                img_rotulo[row, col] = current_label
                # Implementação do flood fill 
                # através de uma busca em largura.
                while(len(fila) > 0):
                    current_index = fila.pop(0)
                    
                    # Escolhemos uma vizinhança de tamanho quatro
                    # visita o leste, sul, oeste e norte do pixel atual.
                    vizinhanca = [
                        (current_index[0], current_index[1] + 1),
                        (current_index[0] + 1, current_index[1]),
                        (current_index[0], current_index[1] - 1),
                        (current_index[0] - 1, current_index[1]),
                    ]

                    for v in vizinhanca:
                        if v[0] >= 0 and v[1] >= 0 and v[0] < num_rows and v[1] < num_cols:                        
                            # Validação para pixel válido, isto é, não estoura os limites da imagem
                            if img[v] == 1 and img_rotulo[v] == 0:
                                # Validação para verificar se o pixel não foi rotulado ainda
                                img_rotulo[v] = current_label
                                fila.append(v)

                current_label += 1
                
    return img_rotulo

# Função de testes
def find_components(imagesStrings):
    for imgObj in imagesStrings:
        separator = "/"
        img = plt.imread("images" + separator + imgObj["name"])
        img = img>0    
        img_rotulo = flood_fill(img)
        print("Labels da imagem " + imgObj["name"] + " : " + str(np.unique(img_rotulo)))
        plt.imshow(img_rotulo)
        plt.savefig("components" + separator + imgObj["name"].split(".")[0] + "_component.jpg")

# testes das imagens da pasta images
imagesStrings = [
    {"name": "componentes.tiff"},
    {"name": "shapes.png"},
    {"name": "squares.png"},
    {"name": "circles.png"},
    {"name": "stars.gif"},
]       

# Encontra as componentes nas imagens selecionadas.
find_components(imagesStrings)