# Comparar listas para saber quais números foram sorteados em uma loteria.
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1
        print("Número acertado:", number)

print("Quantidade de acertos:", hits) # Saída: 4
