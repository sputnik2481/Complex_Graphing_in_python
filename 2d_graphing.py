import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace

# graphing for 2D complex infinite lines

x = np.linspace(-100j,100j)

def complex_coordinates_planar(function, graph_color = 'black', point_colors = ['lightseagreen','aquamarine', 'springgreen']):
    #these two loops just check if theres a color gradient for the line
    if isinstance(graph_color, list):
        for i in range(len(graph_color)):
            plt.plot(function.real[i], function.imag[i], color=graph_color[i])
    else:
        plt.plot(function.real, function.imag, color=graph_color)

    for i in range(len(point_colors)):
        plt.plot(function.real[20+i*5],function.imag[20+i*5], color=point_colors[i], marker = 'o')

    plt.show()


complex_coordinates_planar(x+0j)