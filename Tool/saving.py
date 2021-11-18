import pandas as pd
import os.path
import os.path

def save_theme(name, df, *args, **kwargs):
    if not os.path.exists(f'{name}'):
        os.mkdir(f'{name}')
        #df.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'{name}/{name}.csv',
            index=False
        )

        print(f'\n\n{df}\n\n')
    elif os.path.exists(f'{name}') and not os.path.exists(f'{name}/{name}.csv'):
        #YT.to_csv(f'{name}/{name}_data_leitura.csv')
        df.to_csv(
            f'{name}/{name}.csv',
            index=False
        )
        print('\n\nTema já existe\n Resumo não existe \n\n')

        print(f'\n\n{df}\n\n')
    if os.path.exists(f'{name}') & os.path.exists(f'{name}/{name}.csv'):
        YT = pd.read_csv(f'{name}/{name}.csv')
        # for row in YT:
        #     if row == row in df:
        #         pass
        #     else:
        #         YT.loc(row)
        df = pd.merge(YT, df,how = "left", on = ["Channel","Ch_URL"])
        #YT.to_csv(f'{name}/{name}_data_leitura.csv')
        YT.to_csv(
            f'{name}/{name}.csv',
            index=False
        )
        print('\nTema já existe')
        print(f'\n{YT}\n\n')
        
def channel(YT_Theme, df, CH, *args, **kwargs):
    if not os.path.exists(f'{YT_Theme}/canais_{YT_Theme}'):
        os.mkdir(f'{YT_Theme}/canais_{YT_Theme}')
    elif os.path.exists(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv'):
        try:
            YT = pd.read_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv')
            #df2 = df2.astype(str)
            #YT = YT.astype(str)
            #df2 = YT.merge(df2, how = 'outer')
            #YT = pd.concat([YT, df2]).drop_duplicates().reset_index(drop=True)
            YT = YT.astype(str) #tentando contornar erro que não permite o merge entre dataframes
            df = df.astype(str) #tentando contornar erro que não permite o merge entre dataframes
            YT = pd.merge(
                YT,
                df,
                how='outer',

                on=[
                    'Category',
                    'Channel',
                    'Ch_URL',
                    'Video_URL',
                    'Videos',
                    'Date'
                ],
                # right_on=[
                #     'Category',
                #     'Channel',
                #     'Ch_URL',
                #     'Video_URL',
                #     'Videos',
                #     'Date'
                # ],
                suffixes=(
                    '',
                    '_drop'
                )
            )
            YT.drop([col for col in YT if 'drop' in col], axis=1, inplace=True)
            YT = YT.drop_duplicates()
            #YT.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
            YT.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv', index=False)
            print('\n\nCanal já existe')
            print(f'\n{YT}\n\n')
        except:
            os.path.exists(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv')
            next
    else:
        #df.to_csv(f'{YT_Theme}/canais_{YT_Theme}'_data_leitura.csv')
        df.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}.csv', index=False)
        #df[f'Subs{today}'] = subscribers
        #df[f'View{today}'] = views
        print('\n\nTema já existe\n Canal não existe \n')
        print(f'{df}\n\n')

    #df2.to_csv(f'{YT_Theme}/canais_{YT_Theme}/{CH}_df_l.csv')
    #print(f'\n\n {df2} \n\n')
