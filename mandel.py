import sys
import numpy as np
import matplotlib.pyplot as plt

def iteracoes(c):
    z = complex(0,0)  #valor inicial do z 
    i = 0 
    while( i < 127  and  abs(z*z) <= 2):
        z = z*z + c
        i = i + 1
    return(i)


def Imagem(rx, ry, ie, sd):
    hx = (sd.real - ie.real)/rx
    hy = (sd.imag - ie.imag )/ry 
    matriz = []
    for i in range(rx):
        linha = []
        y = ie.imag + i*hy
        for j in range(ry):
            x = ie.real + j*hx
            cc = complex(x,y)
            valor = iteracoes(cc)
            linha.append(valor)
        matriz.append(linha)
    #print( np.matrix(matriz))
    np.savetxt('saida.txt', np.matrix(matriz), fmt='%.0f')


argumentos = sys.argv
# argumentos[0] = nome do arquivo python
# argumentos[1] = ax  (parte real do ponto inferior esquerdo)
# argumentos[2] = ay (parte imaginária do ponto inferior esquerdo)
# argumentos[3] = bx (parte real do ponto superior direito)
# argumentos[4] = by (parte imaginária do ponto superior direito)
# argumentos[5] = resolução em x 
# argumentos[6] = resolução em y

#Verificando se todos os argumentos  foram passados 
if(len(sys.argv) < 7 ):
    print("Você não informou todos os argumentos")

a = complex(float(argumentos[1]), float(argumentos[2]))
b = complex(float(argumentos[3]), float(argumentos[4]))
r = [int(argumentos[5]), int(argumentos[6])]

Imagem(r[0], r[1], a,b)

