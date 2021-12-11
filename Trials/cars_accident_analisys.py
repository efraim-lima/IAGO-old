# início da programação de catalogação e analise dos acidentes de trânsito do Paraná
# 
# #Ferramenta adotada para solução: Python
import pandas as pd #biblioteca que será importante para a análise dos dados

#criação de listas vazias, simplesmente conteiners para receber dados futuramente preenchidos
city_code = [] #aqui receberemos o código da cidade
city_touring_cars = [] #aqui receberemos a quantidade de veículos de passeio daquela cidade
traffic_accident = [] #aqui receberemos a quantidade de acidentes ocorridos naquela cidade

#início do laço while, que terminará apenas quando contemplarmos todas as cidades
while True:
    #processo de coleta de dados
    print('Olá, poderia nos informar o código da sua cidade, por favor?') 
    code = int(input('Código da Cidade [apenas números]: '))
    print('Muito obrigado, agora poderia me informar a quantidade de veículos de passeio na cidade?')
    cars = int(input('Quantidade de Carros de Passeio [apenas números]:'))
    print('para concluir precisamos apenas da quantidade de acidentes de trânsito em sua cidade.')
    accident = int(input('Quantidade de acidentes de trânsito [apenas números]:'))
    
    #aqui catalogaremos os dados nas listas vazias, para um processo futuro
    city_code.append(code)
    city_touring_cars.append(cars)
    traffic_accident.append(accident)
    
    biggest_traffic_accident = [] #aqui o programa preencherá com a quantidade de acidentes acima da média
    less_traffic_accident = [] #aqui o programa preencherá com a quantidade de acidentes abaixo da média
    traffic_accident_sum = [] #aqui o programa preencherá a soma de acidentes contando com todas cidades

    print('Acabcaram-se as cidades?') #neste momento decidiremos se devemos repetiremos ou concluiremos o laço
    answer = str(input('[S/N]')) #input com resposta do usuário
    if answer == 'S': #condição de término do código
        dataframe = [] #dataframe vazio, na verdade é uma lista que será transformada em dataframe
        for code, cars, accident in zip (city_code, city_touring_cars, traffic_accident): #manipulação dos dados coletados
            dataframe.append({
                'City':code,
                'Cars':cars,
                'Accidents': accident
            })
        df = pd.DataFrame(dataframe) #transformando as listas em um dataframe
                
        #calculando as cidades com maior e menor íncices de acidentes
        accidents_mean = df['Accidents'].mean() #calculo da média de acidentes
        accident_big = df.query(f'Accidents > {accidents_mean}') #definindo as cidades com maior índice de acidentes
        accident_less = df.query(f'Accidents < {accidents_mean}') #definindo as cidades com menor índice de acidentes
        biggest_traffic_accident.append(accident_big) #inserindo as cidades de maior índice em uma lista a parte
        less_traffic_accident.append(accident_less)  #inserindo as cidades de menor índice em uma lista a parte
        
        #calculando a média de veículos das cidades
        mean_df = df['Cars'].mean()
        
        #definindo a média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio
        cars_below_2000 = df.query('Cars < 2000') #definindo quais as cidade com menos de 2000 veículos
        mean_accidents = cars_below_2000['Accidents'].mean() #calculando a média de acidentes das cidades encontradas acima
            
        
        #processso de printar as mensagens na tela para que o usuário tenha ciência dos resultados
        print(f'Quantidade de cidades: {len(city_code)}')
        print(f'Quantidade de veículos de passeio: {sum(city_touring_cars)}')
        print(f'Quantidade de acidentes (soma): {sum(traffic_accident)}')
        print(f'Tabela com cidade de maior índice de acidentes de trânsito: \n{biggest_traffic_accident}')
        print(f'Tabela com cidade de menor índice de acidentes de trânsito: \n{less_traffic_accident}')
        print(f'A média de veículos (considerando todas as cidades) é: {mean_df}')
        print(f'A média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio é {mean_accidents}')
        print(f'\nAbaixo você pode ver uma tabela com os dados:\n\n{df}') # BÔNUS: Uma tabela para exemplificar de forma mais clara
        print('\n\n Obrigado por sua participação')
        break #fim do programa/término do laço
    elif answer == 'N': #condição que define a repetição do laço
        continue
    else: #condição neutra, caso o usuário insira uma mensagem desconhecida pelo programa.
        print('Não entendi, encerrando o programa')
#fim da programação