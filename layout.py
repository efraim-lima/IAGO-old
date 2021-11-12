import PySimpleGUI as sg

def sgLayout():
        #python -m venv __YT__
    #### para acionar o virtual env
    #__YT__\Scripts\activate.bat
    #### para ativar o virtual env
    #sg.change_look_and_feel('DarkEmber')
    #### deixei pra ter referência de temas, já que ao usar este o Terminal me retorna todos nomes existentes
    sg.change_look_and_feel('SystemDefaultForReal')
    #### tema que estou usando
    sg.popup_ok("Hello!! \nI'm IAGO  \nAn Artificial Inteligence that helps You \nto find your content for videos!!!") 
    ####janela de popup

    #desenhando o layout simples

    layout= [[sg.Text(
                    "\nFirst I need your help... \nWhats your main theme or niche?"
                    ),
            sg.Input()
            ],#[sg.Button('Iniciar Análise')],
            [sg.Submit(),
            sg.Cancel()
            ]
        ]

    janela = sg.Window('IA5').layout(layout) #### abre a janela de acordo com o Layout acima especificado
    event, values = janela.read()

    YT_Category = values[0].lower() #### captura o texto dentro da caixa de Texto
    #print = sg.Print
    #print(YT_Category)
    janela.close()


    #YT_Category = input(f'tema: ')
    #Confirmation = input(
    #    '\n\n Obrigado, primeiro vamos analisar a quantidade de concorrentes que você possui. \nA analise a seguir vai abrir um navegador do Chrome, depois disso pode voltar para essa tela que o robô faz tudo isso.\nQuer fazer essa analise agora? [S/N] \nR: ')

    #if YT_Category and Confirmation == 's' or 'S' or 'Sim' or 'sim':
    #    print('\n\n\n Aguarde...\n\n\n')
    #elif YT_Category and Confirmation == 'n' or 'N' or 'No' or 'Not' or 'não' or 'Não':
    #    print('Poutz, que pena, mas o programa vai rodar por default...depois arrumo isso, ta bem?')
    #    quit()
    #else:
    #    print('Não entendi, sou meio limitado, poderia me dizer se quer Sim ou não?  ')

    #for i in range(1,100):
    #    sg.one_line_progress_meter(
    #        'Theme Analysis',
    #        i+1,
    #        100,
    #        'Better Channels',
    #        'Decrypting Channels\n and Data'
    #    )

    return YT_Category