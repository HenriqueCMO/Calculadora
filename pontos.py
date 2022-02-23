# Calcular distância entre dois pontos

import math

x1 = float(input("Digite a coordenada X1: "))
y1 = float(input("Digite a coordenada Y1: "))
x2 = float(input("Digite a coordenada X2: "))
y2 = float(input("Digite a coordenada Y2: "))

distancia = ((x2-(x1))**2)+((y2-(y1))**2)
raiz = math.sqrt(distancia)

if raiz >0 and raiz >=10:
    print("longe")
else:
    print("perto")




