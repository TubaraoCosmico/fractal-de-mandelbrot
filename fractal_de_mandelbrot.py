import sys
import numpy as np
import matplotlib.pyplot as plt

def definindo_cores(cor):
    global imagem
    # Color map https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

    plt.xlabel("AX=" + argumentos[1] + " AY=" + argumentos[2])
    plt.ylabel("BX=" + argumentos[3] + " BY=" + argumentos[4])

    if cor == "hot":
        plt.imshow(imagem,cmap=cor)
    elif cor == "RdBu":
        plt.imshow(imagem,cmap=cor)
    elif cor == "xkcd":
        plt.imshow(imagem)
        plt.xkcd()
    elif cor == "magma":
        plt.imshow(imagem,cmap=cor)
    elif cor == "plasma":
        plt.imshow(imagem,cmap=cor)
    elif cor == "cividis":
        plt.imshow(imagem,cmap=cor)
    elif cor == "inferno":
        plt.imshow(imagem,cmap=cor)
    else:
        plt.imshow(imagem)

    plt.colorbar()
    plt.savefig(nomeArquivo + ".jpg")
    print("Imagem salvada: " + nomeArquivo + ".jpg")
    plt.show()


def atual_datahora(modo):
    from datetime import datetime
    resultado = datetime.today()
    if modo == 1:
        resultado = resultado.strftime('%d-%m-%Y_%H-%M-%S-%f')
    else:
        resultado = resultado.strftime('%d/%m/%Y %H:%M:%S:%f')
    return resultado


def iteracoes(c):
    z = complex(0,0)  # valor inicial do z 
    i = 0 
    while i < 127 and abs(z*z) <= 2:
        z = z*z + c
        i = i + 1
    return i


def Imagem(rx, ry, ie, sd):
    hx = (sd.real - ie.real) / rx
    hy = (sd.imag - ie.imag) / ry 
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
    # print( np.matrix(matriz))
    # np.savetxt(nomeArquivo + ".txt", np.matrix(matriz), fmt='%.0f')
    return np.matrix(matriz)    


# Opcionalmente você pode escolher o modo de cor
# Verificando se todos os argumentos  foram passados 
if len(sys.argv) >= 7:
    argumentos = sys.argv
    # argumentos[0] = nome do arquivo python
    # argumentos[1] = ax (parte real do ponto inferior esquerdo)
    # argumentos[2] = ay (parte imaginária do ponto inferior esquerdo)
    # argumentos[3] = bx (parte real do ponto superior direito)
    # argumentos[4] = by (parte imaginária do ponto superior direito)
    # argumentos[5] = resolução em x 
    # argumentos[6] = resolução em y
    # argumentos[7] = Modo de cor (opcional) 
    nomeArquivo = atual_datahora(1) + "__ax=" + argumentos[1] + "__ay=" + argumentos[2] + "__bx=" + argumentos[3] + "__by=" + argumentos[4]
    a = complex(float(argumentos[1]), float(argumentos[2]))
    b = complex(float(argumentos[3]), float(argumentos[4]))
    r = [int(argumentos[5]), int(argumentos[6])]
    imagem = Imagem(r[0], r[1], a,b)
    # print("Gerado arquivo de saida: " + nomeArquivo + ".txt")
    # imagem = np.loadtxt(nomeArquivo + ".txt")
    if len(sys.argv) == 8:
        definindo_cores(argumentos[7])
    else:
        definindo_cores("padrao")
else:
    print("Você não informou todos os argumentos")
