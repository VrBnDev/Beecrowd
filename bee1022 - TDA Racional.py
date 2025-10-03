from math import gcd 
entrada = int(input())

for i in range(entrada):
    ent = input().split()
    n1, d1, n2, d2 = int(ent[0]), int(ent[2]), int(ent[4]), int(ent[6])

    # Adição
    if ent[3] == '+':
        parte_soma_1 = (n1*d2+n2*d1) 
        parte_soma_2 = (d1*d2)
        result_soma = str(parte_soma_1) + '/' + str(parte_soma_2)
        
        print(f'{result_soma}')
    # Subtração
    elif ent[3] == '-':
        result_subtracao = (n1*d2-n2*d1)/(d1*d2)
    # Multiplicação
    elif ent[3] == '*':
        result_multiplicacao = (n1*n2)/(d1*d2)
    # Divisão
    else:
        result_divisao = (n1*d2)/(n2*d1)


