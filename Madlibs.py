'''
Construir um projeto de jogo de madlibs com uma interface gráfica simples

Organização:
- Importar biblioteca GUI
- Atribuir variáveis
- Definir layout, janela e extração dos resultados
- Loop infinito 
- Imprimir reultados
'''
import PySimpleGUI as sg
sg.theme('DarkAmber')
#Layout
layout = [
    [sg.Text('Primeiro adjetivo',size=(15,0)),sg.Input(size=(15,0),key='adj1')],
    [sg.Text('Segundo adjetivo',size=(15,0)),sg.Input(size=(15,0),key='adj2')],
    [sg.Text('Substantivo',size=(15,0)),sg.Input(size=(15,0),key='subs')],
    [sg.Text('Frase',size=(15,0)),sg.Input(size=(15,0),key='frase')],
    [sg.Text('Pessoa famosa',size=(15,0)),sg.Input(size=(15,0),key='famoso')],
    [sg.Button('Mostrar resultado')],
    [sg.Output(size=(50,20))]
]
#Janela
janela = sg.Window('Madlibs', layout)
#Extrair os dados na tela
while True:
    button,values = janela.read()
    adj1 = values['adj1']
    adj2 = values['adj2']
    subs = values['subs']
    frase = values['frase']
    famoso = values['famoso']
    print(f'''Programar é muito {adj1} e também me faz me sentir muito {adj2} por isso eu tava outro dia andando e pensando nesse código que tava escrevendo e dando alguns problemas e de repente um {subs} apareceu na minha frente e gritou {frase}! isso me inspirou imediatamente e consegui resolver o problema do código, foi incrível! Me senti igual a {famoso}''')
