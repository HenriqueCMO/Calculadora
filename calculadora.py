#Projeto minha calculadora em Python 28/01/2022 18:38

import sys
from datetime import date
    
print("===============================")
print("Olá, hoje é dia " + date.today().strftime('%d/%m/%y') + "\n")
print("Seja Bem Vindo a Calculadora! \n")


while True:
    print("As operações possíveis são:")
    print("soma[+]; subtração[-]; multiplicação[*]; divisão[/]  \n\n")

# identificação das variáveis 
    sim = "s"
    não = "n"
    sinal_soma = "+"
    sinal_subtração = "-"
    sinal_multiplicação = "*"
    sinal_divisão = "/"


    numero1 = float(input("Digite o primeiro número: "))
    operação = input("qual operação deseja realizar? ")
    if operação != sinal_soma \
        and operação != sinal_subtração \
        and operação != sinal_multiplicação \
        and operação != sinal_divisão :
        print("Operação matemática não permitida ")
    numero2 = float(input("Digite o segundo número: "))
    print("\n")

     
# condições de cálculo
    if operação == "+":
        soma =  numero1 + numero2
        print(f"O total desta soma é {soma}")
        
    elif operação == "-":
        subtração =  numero1 - numero2
        print(f"A diferença desta subtração é {subtração} \n")
        
    elif operação == "*":
        multiplicação =  numero1 * numero2
        print(f"O produto desta multiplicação é {multiplicação} \n")

    elif operação == "/":
        divisão =  numero1 / numero2
        print(f"O quociente desta divisão é {divisão} \n")

##    print("Operação matemática não permitida")

    print("===============================")
    print("\n")

# condição de repetição
    repetição = input("Deseja fazer um novo cálculo? [s]Sim / [n]Não \n")
    print("\n")
    if repetição != sim:
        break # sai do while
