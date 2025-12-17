# Fatias e cópias de listas em Python
# Copiar a lista inteira. A omissão dos índices cria uma cópia completa.
list_1 = [1]
list_2 = list_1 [:]
list_1 [0] = 2
print (list_2)

# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)

# Fatia com negativos.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# Fatia fora dos limites.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

# Fatia com inicio omitido.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# Fatia com fim omitido.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[2:]
print(new_list)

# Excluindo fatias.
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
 
# Excluindo fatia com inicio omitido.
my_list = [10, 8, 6, 4, 2]
del my_list[:3]
print(my_list)  

# Excluindo todos os elementos. 
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# Verifica se elemento está na lista ou não.
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
print(12 not in my_list)
