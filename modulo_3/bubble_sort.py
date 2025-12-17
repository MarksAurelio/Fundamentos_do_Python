# Ordenando lista usando o algoritmo Bubble Sort
my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
 
# Saída esperada: [2, 4, 6, 8, 10]

# Outra forma de implementar o Bubble Sort através de uma função
def bubble_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Bubble Sort.
    """
    n = len(lista)
    houve_troca = True
    
    while houve_troca:
        houve_troca = False
        # Percorremos a lista até o penúltimo elemento
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                # Se o atual for maior que o próximo, trocamos
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                houve_troca = True
    
    return lista

# --- Testando a função ---

# Lista desordenada
numeros_aleatorios = [8, 10, 6, 2, 4]
print("Antes da ordenação:", numeros_aleatorios)

# Chamando a função
bubble_sort(numeros_aleatorios)

print("Depois da ordenação:", numeros_aleatorios)

# Testando com outra lista qualquer
outra_lista = [99, 1, 55, 23, 0, -5]
print("\nNova lista ordenada:", bubble_sort(outra_lista))

# Saída esperada: [2, 4, 6, 8, 10]
