# Função para verificar se o ano é bissexto e retornar o número de dias em um mês específico 
def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return month_days[month - 1]

""" Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.

Use as funções escritas e testadas anteriormente. Adicione seus próprios casos de teste ao código. """
def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    return total_days

# Testes para a função day_of_year
print(day_of_year(2025, 12, 19))  # Saída esperada: 61
print(day_of_year(1900, 2, 29))  # Saída esperada: None

# Exemplos de uso da função days_in_month
print(days_in_month(1900, 2))  # Saída esperada: 28
print(days_in_month(2000, 2))  # Saída esperada: 29
print(days_in_month(2016, 2))  # Saída esperada: 29
print(days_in_month(1987, 2))  # Saída esperada: 28

# Testes
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 2, 2]
test_results = [28, 29, 29, 28]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print(" OK")
    else:
        print("Fracassado")
