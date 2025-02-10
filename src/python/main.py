from biolink import Matrix
from parser import get_images

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    '''
    data = np.array([
        [20, 1, 30, 1, 5],
        [12, 2, 30, 1, 5],
        [31, 1.5, 3, 1, 5],
        [10, 2.3, 3, 1, 5],
    ])
    '''
    
    data = get_images(3000)
    m = Matrix(data)

    m.normalize(1e4)
    m.clear_matrix(0.1, 8, 1)
    m.remove_dependence(240)
    m.pca(2)
    
    print(m.to_array())
    print(f'{ m.cols }x{ m.rows }')
    array_2d = m.to_array()
    
    plt.figure(figsize=(8, 6))
    plt.scatter(array_2d[:, 0], array_2d[:, 1], marker='o', color='blue')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Кластеризация")
    plt.grid(True)

    plt.show()
    

