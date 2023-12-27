import numpy as np
import matplotlib.pyplot as plt

        
        
## Affichage simple pour la solution      
def afficher(list_x,list_y):
    for j,absic in enumerate(list_x):
        plt.plot(absic,list_y[j],'x-',linewidth=2.0)
    plt.show()

## Affichage en log pour la coordonnee y pour les courbes de convergence    
def afficherConv(list_x,list_y, legend):
    for j,absic in enumerate(list_x):
        plt.plot(absic,list_y[j],'x-',linewidth=2.0)
    plt.yscale('log')
    plt.ylabel("Residual")
    plt.xlabel("Iteration")
    plt.legend(legend)
    plt.show()
