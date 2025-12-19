# Criando um função que recebe uma lista de números inteiros e retorna a soma desses números.
def sum_list(list):
    s = 0
    for i in list:
        s += i
    return s

lista = []
for i in range(5):
    n = int(input("Digite um número inteiro: "))
    lista.append(n)

print("A lista digitada é:", lista)
print("A soma dos números da lista é:", sum_list(lista))
