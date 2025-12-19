# Criando uma função que cria e retorna uma lista de números inteiros com tamanho definido pelo usuário.
def list(list_size):
    lista = []
    for i in range(list_size):
        n = int(input("Digite um número inteiro (ou -1 para encerrar): "))
        if n == -1:
            break
        lista.append(n)
    return print("Lista criada com sucesso:", lista)

list(5)
