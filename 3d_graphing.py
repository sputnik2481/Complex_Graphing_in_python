import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace

#3d graphing of complex functions!

#initlialization of my XY and Z axes. Y is already complex based on personal preference
x = linspace(-5,5,100)
y = linspace(-5j,5j,100)
X,Y = np.meshgrid(x,y)
z = X + Y

#input for this is a function with respect to z. An example would be graph_3D_complex_functions(z**2)
def graph_3D_complex_functions(function):
    # for readability as typically Z is used
    if isinstance(function, int):
        Z = function + 0*X + 0*Y

    else:
        Z = function

    fig = plt.figure('3D Complex Function', figsize=(5,4.), dpi = 100)
    ax = fig.add_subplot(projection='3d')

    #colorful gradient for easy visulizations of magnitude changes
    ax.plot_surface(X.real, Y.imag, Z.real, rstride=5, cstride=5,
                    cmap='viridis')

    #allows the extreme points to be much more clear than the generic bounds, the very small addition just allows for bypassing of an error that pops up when a plane is inputted
    ax.set_zlim3d(np.amin(Z[30]).real, np.amax(Z[70]).real+0.000000000000001)

    plt.show()
