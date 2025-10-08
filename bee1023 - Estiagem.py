while True:
    entrada_imoveis = int(input())
    
    contador_cidade = 0
    contador_moradores = 0
    soma_consumo = 0
    soma_media = 0
    
    dados_residenciais = []

    contador_cidade+=1
    print(f"Cidade #  {contador_cidade}:")
    for i in range(0,entrada_imoveis):
        entrada_moradores_consumo = input().split()
        
        contador_moradores += int(entrada_moradores_consumo[0])
        soma_consumo += int(entrada_moradores_consumo[1])
        media = soma_consumo//contador_moradores
        soma_media += media
        dados_residenciais.append(f'{entrada_moradores_consumo[0]}-{media}')

    print(dados_residenciais)
    #print(f'Moradores: {contador_moradores}')    
    #print(dados_residencias)
    
