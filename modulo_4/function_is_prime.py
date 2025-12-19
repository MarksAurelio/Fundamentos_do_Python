""" ua tarefa é escrever uma função verificando se um número é primo ou não.

A função:

é chamado is_prime;
requer um argumento (o valor a ser verificado)
retorna True se o argumento for um número primo e False caso contrário.
Dica: tente dividir o argumento por todos os valores subsequentes (começando em 2) e verifique o restante - se for zero, seu número não pode ser um primo; pense bem quando deve interromper o processo.

Se você precisar conhecer a raiz quadrada de qualquer valor, poderá utilizar o operador **. Lembre-se: a raiz quadrada de x é o mesmo que x0.5 """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Imprime todos os números primos entre 1 e 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# Testes para a função is_prime
print(is_prime(1))   # Saída esperada: False
print(is_prime(2))   # Saída esperada: True
print(is_prime(3))   # Saída esperada: True
print(is_prime(4))   # Saída esperada: False
print(is_prime(16))  # Saída esperada: False
print(is_prime(17))  # Saída esperada: True
print(is_prime(18))  # Saída esperada: False
print(is_prime(19))  # Saída esperada: True
print(is_prime(20))  # Saída esperada: False
print(is_prime(1000001))  # Saída esperada: True