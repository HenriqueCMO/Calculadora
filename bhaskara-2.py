import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = ((b**2)-(4*a*c))

if delta<0:
    print("esta equação não possui raízes reais")
elif delta==0:
    raiz1 = (-b+math.sqrt(delta))/(2*a)
    raiz2 = (-b-math.sqrt(delta))/(2*a)
    print("a raiz dupla desta equação é", raiz1)
else:
    raiz1 = (-b+math.sqrt(delta))/(2*a)
    raiz2 = (-b-math.sqrt(delta))/(2*a)
    raiz2<raiz1
    aux=raiz2
    raiz2=raiz1
    raiz1=aux
    print("as raízes da equação são", raiz1 ,"e", raiz2)

