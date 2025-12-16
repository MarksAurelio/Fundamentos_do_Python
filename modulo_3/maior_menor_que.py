""" Usando um dos operadores de comparação em Python, escreva um programa simples de duas linhas que aceita o parâmetro n como entrada, que é um inteiro, e imprime False se n for menor 100, e True se n for maior ou igual a 100. """
n = int(input("Digite um número inteiro: "))
print(n < 100); print(n >= 100)
print()

# Outra forma de fazer isso em uma única linha:
n = int(input("Digite um número inteiro: "))
print(n < 100, n >= 100)
