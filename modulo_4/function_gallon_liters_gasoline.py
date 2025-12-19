""" Sua tarefa é escrever um par de funções convertendo l/100 km em mpg e vice-versa.

As funções:

são nomeados liters_100km_to_miles_gallon e miles_gallon_to_liters_100km respectivamente;
use um argumento (o valor correspondente aos nomes)
Preencha o código no editor e execute-o para verificar se a sua saída é igual à nossa.

Aqui estão algumas informações para ajudá-lo:

1 milha americana = 1609.344 metros;
1 galão americano = 3,785411784 litros. """
def liters_100km_to_miles_gallon(liters):
    miles_per_liter = 100000 / 1609.344
    gallons_per_liter = 1 / 3.785411784
    mpg = miles_per_liter * gallons_per_liter / liters
    return mpg

def miles_gallon_to_liters_100km(mpg):
    miles_per_liter = 100000 / 1609.344
    gallons_per_liter = 1 / 3.785411784
    liters = miles_per_liter * gallons_per_liter / mpg
    return liters

# Testes para a função liters_100km_to_miles_gallon
print(liters_100km_to_miles_gallon(3.9))   # Saída esperada: 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))   # Saída esperada: 31.361701244813278
print(liters_100km_to_miles_gallon(10.))   # Saída esperada: 23.521458333333332 

# Testes para a função miles_gallon_to_liters_100km
print(miles_gallon_to_liters_100km(60.3))  # Saída esperada: 3.9007357357357357
print(miles_gallon_to_liters_100km(31.4))  # Saída esperada: 7.514907407407408
print(miles_gallon_to_liters_100km(23.5))  # Saída esperada: 10.0002150537634412
