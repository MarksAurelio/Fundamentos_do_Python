# uma única declaração if, por exemplo:
x = 10
 
if x == 10: # condição
    print("x é igual a 10")  # Executado se a condição for True.
print()

# uma série de declarações if, por exemplo:
x = 10
 
if x > 5: # condição um
    print("x é maior que 5")  # Executado se a condição um for True.
 
if x < 10: # condição dois
    print("x é menor que 10")  # Executado se a condição dois for True.
 
if x == 10: # condição três
    print("x é igual a 10")  # Executado se a condição três for True.
print()

# Cada declaração if é testada separadamente.
x = 10
 
if x < 10: # condição
    print("x é menor que 10")  # Executado se a condição for True.
 
else:
    print("x é maior ou igual a 10")  # Executado se a condição for False.
print()

# uma série de instruções if seguidas de um else, por exemplo:
x = 10
 
if x > 5: # condição um
    print("x é maior que 5")  # Executado se a condição um for True.
 
if x < 10: # condição dois
    print("x é menor que 10")  # Executado se a condição dois for True.
 
if x == 10: # condição três
     print("x é igual a 10")  # Executado se a condição três for True.
print()

# Cada um if é testado separadamente. O corpo do else é executado se o último if for False.
# A declaração if-elif-else, por exemplo:
x = 10
 
if x == 10: # True
    print("x == 10")
 
if x > 15: # False
    print("x > 15")
 
elif x > 10: # False
    print("x > 10")
 
elif x > 5: # True
    print("x > 5")
 
else:
    print("senão não será executado")
print()

# Se a condição para if for False, o programa verifica as condições dos blocos elif subsequentes - o primeiro bloco elif que é True é executado. Se todas as condições forem False, o bloco else será executado.
# Instruções condicional aninhadas, por exemplo:
x = 10
 
if x > 5: # True
    if x == 6: # False
        print("aninhado: x == 6")
    elif x == 10: # True
        print("aninhado: x == 10")
    else:
        print("aninhado: else")
else:
    print("else")
 
