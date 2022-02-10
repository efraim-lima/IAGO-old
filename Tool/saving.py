import pandas as pd
import os.path
import urllib


def theme(name, df, *args, **kwargs):
    if not os.path.exists('./content'):
            os.mkdir('./content')
    elif not os.path.exists(f'./content/{name}'):
        os.mkdir(f'./content/{name}')
        #df.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'./content/{name}/{name}.csv',
            index=False
        )
        df.to_json(
            f'./content/{name}/{name}.json',
            index=True
        )
        print(f'\n\n{df}\n\n')
        
    elif os.path.exists(f'./content/{name}') and not os.path.exists(f'./content/{name}/{name}.csv'):
        #YT.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'./content/{name}/{name}.csv',
            index=False
        )
        df.to_json(
            f'./content/{name}/{name}.json',
            index=True
        )
        print('\n\nTema já existe\n Resumo não existe \n\n')

        print(f'\n\n{df}\n\n')
    
    elif os.path.exists(f'./content/{name}') & os.path.exists(f'./content/{name}/{name}.csv'):
        YT = pd.read_csv(f'./content/{name}/{name}.csv')
        # for row in YT:
        #     if row == row in df:
        #         pass
        #     else:
        #         YT.loc(row)
        df = df.reset_index(drop=True)
        df2 = YT.reset_index(drop=True)
        df = df.join(df2)
        df = df.loc[:,~df.columns.duplicated()]
        #YT.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'./content/{name}/{name}.csv',
            index=False
        )
        df.to_json(
            f'./content/{name}/{name}.json',
            index=True
        )
        print('\nTema já existe')
        print(f'\n{YT}\n\n')
        
def channel(YT_Theme, df, CH, *args, **kwargs):
    """[Estamos recebendo os dados do yt_channel e processando para salvar
    no banco de dados]

    Args:
        YT_Theme ([string]): [tema selecionado pelo user]
        df ([object]): [um dataframe contendo informações]
        CH ([string]): [contém o nome do canal, que será usado aqui]
    """
    if not os.path.exists(f'./content/{YT_Theme}/canais_{YT_Theme}'):
        os.mkdir(f'./content/{YT_Theme}/canais_{YT_Theme}')
        os.mkdir(f'./content/{YT_Theme}/canais_{YT_Theme}/client')
    elif os.path.exists(f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.csv'):
        try:
            YT = pd.read_csv(f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.csv')
            #df2 = df2.astype(str)
            #YT = YT.astype(str)
            #df2 = YT.merge(df2, how = 'outer')
            #YT = pd.concat([YT, df2]).drop_duplicates().reset_index(drop=True)
            # YT = YT.astype(str) #tentando contornar erro que não permite o merge entre dataframes
            # df = df.astype(str) #tentando contornar erro que não permite o merge entre dataframes
            # YT = pd.merge(
            #     YT,
            #     df,
            #     how='outer',

            #     on=[
            #         'Category',
            #         'Channel',
            #         'Ch_URL',
            #         'Video_URL',
            #         'Videos',
            #         'Date'
            #     ],
            #     # right_on=[
            #     #     'Category',
            #     #     'Channel',
            #     #     'Ch_URL',
            #     #     'Video_URL',
            #     #     'Videos',
            #     #     'Date'
            #     # ],
            #     suffixes=(
            #         '',
            #         '_drop'
            #     )
            # )
            # YT.drop([col for col in YT if 'drop' in col], axis=1, inplace=True)
            # YT = YT.drop_duplicates()
            # #YT.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
            
            df = df.reset_index(drop=True)
            df2 = YT.reset_index(drop=True)
            df = df.join(df2)
            df = df.loc[:,~df.columns.duplicated()]
            
            df.to_csv(
                f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.csv', 
                index=False
                )
            df.to_json(
                f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.json', 
                index=True
                )
            print('\n\nCanal já existe')
            print(f'\n{YT}\n\n')
        except:
            os.path.exists(f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.csv')
            next
    else:
        #df.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
        df.to_csv(
            f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.csv', 
            index=False
        )
        coisa = ['Channel','Titles']
        df.to_csv(
            f'./content/{YT_Theme}/canais_{YT_Theme}/client/client_{CH}.csv', 
            index=False, columns = coisa
            )
        df.to_json(
            f'./content/{YT_Theme}/canais_{YT_Theme}/{CH}.json', 
            index=True
            )
        df[['Channel','Titles']].to_json(
            f'./content/{YT_Theme}/canais_{YT_Theme}/client/client_{CH}.json', 
            index=True
            )
        #df[f'Subs{today}'] = subscribers
        #df[f'View{today}'] = views
        print('\n\nTema já existe\n Canal não existe \n')
        print(f'{df}\n\n')

    #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}_df_l.csv')
    #print(f'\n\n {df2} \n\n')
    
def video(YT_Theme, df, channel, *args, **kwargs):
    """[aqui estamos salvando os vídeos, por hora acredito que tenha bastante coisa
    errada, as estou tentando alinhar todos os processos para que fique melhor salvo
    no banco de dados..]

    Args:
        YT_Theme ([string]): [é o tema gerado no yt_theme]
        df ([object]): [conjunto de dados, um dataframe]
        channel ([string]): [nome do canal, que vamos usar aqui]
        title([string]): [título do vídeo, para a thubnail]
        thumb([object]): [é um array, se não me engano...gera a imagem da thumnail]
    """
    
    if not os.path.exists(f'./content/{YT_Theme}/descricoes_{YT_Theme}'):
        os.mkdir(f'./content/{YT_Theme}/descricoes_{YT_Theme}')
        df.to_csv(f'./content/{YT_Theme}/descricoes_{YT_Theme}/{channel}.csv', index=False)
        df.to_json(f'./content/{YT_Theme}/descricoes_{YT_Theme}/{channel}.json', index=True)
    else:
        YT = pd.read_csv(f'./content/{YT_Theme}/descricoes_{YT_Theme}/{channel}.csv')
        df = df.reset_index(drop=True)
        df2 = YT.reset_index(drop=True)
        df = df.join(df2)
        df = df.loc[:,~df.columns.duplicated()]
        print(f'\n\n {df} \n\n')
        df.to_csv(f'./content/{YT_Theme}/descricoes_{YT_Theme}/{channel}.csv', index=False)
        df.to_json(f'./content/{YT_Theme}/descricoes_{YT_Theme}/{channel}.json', index=True)
        #df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{Canal}_df_l.csv')
    
def thumbnail(YT_Theme, channel, title, thumb, *args, **khwargs):
    """[aqui estamos salvando as thumbnails no lugar correto]

    Args:
        title([string]): [título do vídeo, para a thubnail]
        thumb([object]): [é um array, se não me engano...gera a imagem da thumnail]
    """

    if not os.path.exists(f'./content/{YT_Theme}/canais_{YT_Theme}/img'):
        os.mkdir(f'./content/{YT_Theme}/canais_{YT_Theme}/img')
        os.mkdir(f'./content/{YT_Theme}/canais_{YT_Theme}/img/{channel}')
        path2 = f'./content/{YT_Theme}/canais_{YT_Theme}/img/{channel}/{title}.jpg'
    elif not os.path.exists(f'./content/{YT_Theme}/canais_{YT_Theme}/img/{channel}'):
        os.mkdir(f'./content/{YT_Theme}/canais_{YT_Theme}/img/{channel}')
        path2 = f'./content/{YT_Theme}/canais_{YT_Theme}/img/{channel}/{title}.jpg'
        urllib.request.urlretrieve(thumb, path2)
    else: 
        path3 = f'./content/{YT_Theme}/canais_{YT_Theme}/img/{channel}/{title}.jpg'
        urllib.request.urlretrieve(thumb, path3)
        print('\n Canal já existe \n')
    #df2.to_csv(f'{YT_Theme}/descricoes_{YT_Theme}/{Canal}_df_l.csv')
    
def tweet(name, df, *args, **kwargs):
    if not os.path.exists(f'./content/{name}/tweets'):
        try:
            os.mkdir(f'./content/{name}/tweets/')
        except:
            os.makedirs(f'./content/{name}/tweets')
        #df.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'./content/{name}/tweets/{name}.csv',
            index=False
        )
        df.to_json(
            f'./content/{name}/tweets/{name}.json',
            index=True
        )

        print(f'\n\n{df}\n\n')
    
    elif os.path.exists(f'./content/{name}/tweets') and not os.path.exists(f'./content/{name}/tweets/{name}.csv'):
        #YT.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'./content/{name}/tweets/{name}.csv',
            index=False
        )
        df.to_json(
            f'./content/{name}/tweets/{name}.json',
            index=True
        )
        print('\n\nTema já existe\n Resumo não existe \n\n')

        print(f'\n\n{df}\n\n')
    
    elif os.path.exists(f'./content/{name}/tweets') & os.path.exists(f'./content/{name}/tweets/{name}.csv'):
        YT = pd.read_csv(f'./content/{name}/tweets/{name}.csv')
        # for row in YT:
        #     if row == row in df:
        #         pass
        #     else:
        #         YT.loc(row)
        # df = pd.merge(YT, df,how = "left", on = ["Tweet"])
        #YT.to_csv(f'{name}/{name}_data_leitura.csv')
        YT.to_csv(
            f'./content/{name}/tweets/{name}.csv',
            index=False
        )
        YT.to_json(
            f'./content/{name}/tweets/{name}.json',
            index=True
        )
        print('\nTema já existe')
        print(f'''
              
              {YT}
              
              ''')