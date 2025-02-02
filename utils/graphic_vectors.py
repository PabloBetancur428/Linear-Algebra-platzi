import numpy as np
import matplotlib.pyplot as plt
def graph_vecs(vecs, cols, alpha = 1):

    plt.figure()
    plt.axvline(x=0, color='gray', zorder=0)
    plt.axhline(y=0, color='gray', zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0,0], vecs[i]]) #start at 0,0
        plt.quiver([x[0]],
                [x[1]],
                [x[2]],
                [x[3]],
                angles='xy', scale_units='xy', scale=1, color=cols[i], alpha=alpha)