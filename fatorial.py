valor =int(input("Digite um número natural n: "))

fatorial = 1
contador = 1

while contador <= valor and valor > 0:
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)