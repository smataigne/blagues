# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 19-20
# Problème 3
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 
  
import numpy as np
from approximation import approximation
 
#
# -1- Données discrètes à approximer
#     construites à partir de la fonction u(x,y) = x*(x-2)*(y-0.2)*(y+3)/10.0 + pertubations
#
#     amplitudePerturbation = 0    : l'approximation doit devenir une interpolation (si, si !)
#                           = 0.1  : qu'observe-t-on ?
#                           = 0.25 : et maintenant ?
#                           = 1.00 : et ensuite...

n = 50
amplitudePerturbation = 0.25

X = np.random.rand(n)*2-1
Y = np.random.rand(n)*2-1
E = np.random.rand(n)*2-1
U = X*(X-2)*(Y-0.2)*(Y+3)/10.0 + E * amplitudePerturbation

#
# -2- Calcul de l'approximation u_h(x) sur une grille régulière
#

x,y = np.meshgrid(np.arange(-1.0,1.0,0.1),np.arange(-1.0,1.0,0.1))
a,uh = approximation(X,Y,U,x,y)
print(" Computed coefficients are : ",end=""); print(a)

#
# -3- Calcul de la fonction exacte u(x) sur la même grille
#

u = x*(x-2)*(y-0.2)*(y+3)/10.0

#
# -4- Un joli plot dans l'espace :-)
#     Trouver les options dans matplotlib est parfois un peu tricky, je sais :-)
#

import matplotlib.pyplot as plt
import matplotlib 
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams['toolbar'] = 'None'
fig = plt.figure("Approximation biquadratique")

ax=plt.axes(projection='3d')
ax.plot_surface(x,y,u, rstride=1,cstride=1,alpha=0.4,linewidth=0.5,edgecolors='k',color='b')
ax.plot_surface(x,y,uh,rstride=1,cstride=1,alpha=0.4,linewidth=0.5,edgecolors='k',color='g')
ax.scatter(X,Y,U,color='r',s=40,alpha=1)
ax.set_axis_off()
plt.show()










