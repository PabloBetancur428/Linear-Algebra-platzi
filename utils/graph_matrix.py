import numpy as np
import matplotlib.pyplot as plt
from .graphic_vectors import graph_vecs as graph_vectors 


def graph_matrix(matrix, vectorCol = ['red', 'blue']):

    #Unit circle
    x = np.linspace(-1, 1, 100000)
    y = np.sqrt(1-(x**2)) #represents circle

    #Transformed unit circle
    x1 = matrix[0,0]*x + matrix[0,1]*y
    y1 = matrix[1,0]*x + matrix[1,1]*y
    x1_neg = matrix[0,0]*x - matrix[0,1]*y
    y1_neg = matrix[1,0]*x - matrix[1,1]*y

    #Vectors
    u1 = [matrix[0,0], matrix[1,0]]
    v1 = [matrix[0,1], matrix[1,1]]

    graph_vectors([u1, v1], cols = [vectorCol[0], vectorCol[1]])

    plt.plot(x1, y1, 'green', alpha = 0.7)
    plt.plot(x1_neg, y1_neg, 'green', alpha = 0.7)