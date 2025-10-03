entrada = input()
competidor = input().split()

saida = 0

for i in competidor:
    if i == entrada:
        saida +=1

print(saida)