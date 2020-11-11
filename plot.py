import sys
import numpy as np
import matplotlib.pyplot as plt

argumentos = sys.argv
# argumentos[0] = nome do arquivo python
# argumentos[1] = nome do arquivo contendo os valores

imagem = np.loadtxt(argumentos[1])
#Cor padrão 
#plt.imshow(imagem)
#plt.colorbar()
#plt.show()

#Cor 1 
#plt.imshow(imagem,cmap='hot')
#plt.colorbar()
#plt.show()

#Cor 2 
#plt.imshow(imagem,cmap='RdBu')
#plt.colorbar()
#plt.show()

#xkcd 
plt.xkcd()
plt.imshow(imagem,cmap='magma')
plt.colorbar()
plt.show()

#Color map 
#https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html