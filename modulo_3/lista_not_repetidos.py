""" magine uma lista - não muito longa, não muito complicada, apenas uma lista simples que contém alguns números inteiros. Alguns desses números podem ser repetidos, e essa é a pista. Não queremos repetições. Queremos que eles sejam removidos.

Sua tarefa é escrever um programa que remova todas as repetições de números da lista. O objetivo é ter uma lista na qual todos os números não aparecem mais de uma vez.

Nota: suponha que a lista de origem seja codificada dentro do código - você não precisa inseri-la no teclado. Claro, você pode melhorar o código e adicionar uma parte que possa conversar com o usuário e obter todos os dados dele.

Dica: recomendamos que você crie uma nova lista como uma área de trabalho temporária. Você não precisa atualizar a lista in situ. """
my_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5, 9, 10, 8]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print("Lista original:", my_list)
print("Lista sem repetições:", new_list)

# Outra forma de fazer usando conjuntos (sets).
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# O set remove automaticamente as duplicatas
new_list = list(set(my_list))

print("Elementos exclusivos:")
print(new_list) # Note que a ordem dos elementos pode mudar ao usar sets.

# Outra forma de fazer usando dicionários.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]    
new_list = list(dict.fromkeys(my_list))
print("Elementos exclusivos:")
print(new_list)
# Outra forma de fazer usando list comprehension.
my_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5, 9, 10, 8]
new_list = []
[new_list.append(item) for item in my_list if item not in new_list]
print("Lista original:", my_list)
print("Lista sem repetições:", new_list)
