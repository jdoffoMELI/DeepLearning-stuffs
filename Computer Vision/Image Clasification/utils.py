import numpy as np
import matplotlib.pyplot as plt
from typing import TypeAlias, List, Union

Image: TypeAlias = [float, float, float]

def show_images(imgs: List[Image], nrows: int, ncolumns: int):
    """
    Dibuja una grilla con imagenes al azar.
    Args:
        imgs (Array[Image]):    Conjunto de imagenes. 
        nrows (int):            Cantidad de filas en la grilla.
        ncolumns (int):         Cantidad de columnas en la grilla.
    """
    fig, ax = plt.subplots(nrows, ncolumns, figsize=(10,5))
    for i in range(nrows * ncolumns):
        random_index = np.random.randint(0, len(imgs))
        random_image = imgs[random_index]
        ax[int(i < ncolumns), i % ncolumns].imshow(random_image)
        ax[int(i < ncolumns), i % ncolumns].set_axis_off()
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()

def distribucion_labels(labels):
    """
    Dibuja un histograma con la distribucion de las labels.
    Args:
        labels (Union): Conjunto de labels.
    """
    unique_labels = np.unique(labels)
    plt.hist(label=unique_labels, x=labels, bins=len(unique_labels), density=True, ec="black")
    plt.ylabel("Densidad")
    plt.xlabel("Labels")
    plt.title("Distribucion de las etiquetas")
    plt.show()

