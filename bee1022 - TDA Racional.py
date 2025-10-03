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
        
        print(f'{result_soma} = {int(parte_soma_1/gcd(parte_soma_1,parte_soma_2))}/{int(parte_soma_2/gcd(parte_soma_1,parte_soma_2))}')
    
    # Subtração
    elif ent[3] == '-':
        parte_subtracao_1 = (n1*d2-n2*d1)
        parte_subtracao_2 = (d1*d2)
        result_subtracao = str(parte_subtracao_1) + '/' + str(parte_subtracao_2)
    
        print(f'{result_subtracao} = {int(parte_subtracao_1/gcd(parte_subtracao_1,parte_subtracao_2))}/{int(parte_subtracao_2/gcd(parte_subtracao_1,parte_subtracao_2))}')
    
    # Multiplicação
    elif ent[3] == '*':
        parte_multiplicacao_1 = (n1*n2)
        parte_multiplicacao_2 = (d1*d2)
        result_multiplicacao = str(parte_multiplicacao_1) + '/' + str(parte_multiplicacao_2)
    
        print(f'{result_multiplicacao} = {int(parte_multiplicacao_1/gcd(parte_multiplicacao_1,parte_multiplicacao_2))}/{int(parte_multiplicacao_2/gcd(parte_multiplicacao_1,parte_multiplicacao_2))}')
    # Divisão
    else:
        parte_divisao_1 = (n1*d2)
        parte_divisao_2 = (n2*d1)
        result_divisao = str(parte_divisao_1) + '/' + str(parte_divisao_2)
    
        print(f'{result_divisao} = {int(parte_divisao_1/gcd(parte_divisao_1,parte_divisao_2))}/{int(parte_divisao_2/gcd(parte_divisao_1,parte_divisao_2))}')

