maior_numero = -999999999
numero = int(input("Digite um número (-1 para sair): "))
if numero == -1:
    print(maior_numero)
    numero = int(input("Digite um número (-1 para sair): "))
if numero > maior_numero:
    maior_numero = numero
