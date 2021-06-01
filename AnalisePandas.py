#importação das bibliotecas necessárias para o funcionamento do programa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#leitura do banco de dados
dados = pd.read_csv('MOCK_DATA MODIFICADO.csv', delimiter=',', encoding= 'utf-8')  

#Listas responsáveis pela execução do programa
cores = ['r','b','m','c','k','g','y','w']
nomes = []
coordenadas = []
media = []
histo = []

#Função menu, responsável pela seleção dos gráficos
def menu():
    print('''[1] - grafico\n[2] - histograma\n[3] - sair do programa''')
    opção = int(input('qual a sua opção? '))
    return opção

#função responsável pelo localização dos itens do banco de dados
def geraCoordenadas():
    for i in range(0,len(nomes)):
        a = dados.loc[dados['marca'] == nomes[i]]
        b = a[['ano','valor']].copy()
        b = b.sort_values(by=['valor'])
        coordenadas.append(b)

#função responsável pelo cálculo da média 
def calculo():
    for i in nomes:      
        a = dados.loc[dados['marca'] == i]
        b = a[['modelo','valor']].copy()
        c = b.groupby('modelo').mean()
        media.append(c)

#função responsável pela plotagem dos gráficos de linhas(curvas)
def graficos(nlinhas):
    calculo()
    geraCoordenadas()
    if nlinhas == 1:
        plt.figure(figsize=(30,10))   
        plt.xlabel('Modelos')
        plt.ylabel('Médias dos preços')
        plt.plot(media[0]['valor'], marker = '*')
        plt.show()    

    elif nlinhas == 2:
        plt.figure(figsize=(40,20))
        plt.xlabel('preço')
        plt.ylabel('ano')
        plt.plot(coordenadas[0]['valor'],coordenadas[0]['ano'],coordenadas[1]['valor'],coordenadas[1]['ano'], marker = '*')
        plt.show()   

    elif nlinhas == 3:
        plt.figure(figsize=(40,20))
        plt.xlabel('preço')
        plt.ylabel('ano')
        plt.plot(coordenadas[0]['valor'],coordenadas[0]['ano'],coordenadas[1]['valor'],coordenadas[1]['ano'],coordenadas[2]['valor'],coordenadas[2]['ano'], marker = '*')
        plt.show()

#função responsável pela localização dos dados para a plotagem dos histograma
def geraHist():
    for i in range(0,len(nomes)):
        a = dados.loc[dados['marca'] == nomes[i]]
        b = a[['modelo']].copy()
        histo.append(b)

#função responsável pela plotagem dos histogramas
def histograma(cor):
    geraHist()
    plt.figure(figsize = (100,10))
    x = np.linspace(0, 35, num=50) 
    plt.hist(histo[0]['modelo'], bins = x,rwidth=0.2,color = cor)
    plt.xlabel('Modelos')
    plt.ylabel('Quantidade')


op = menu()

#função if responsável pela seleção do número de linhas e das cores dos histogramas
if op == 1:
    n = int(input('numero de linhas: '))
    for i in range(0,n):
        nomes.append(str(input('nome da marca: ')))

    graficos(n)
  
elif op == 2:
    n = int(input('[0] - Vermelho\n[1] - Azul\n[2] - Rosa\n[3] - Ciano\n[4] - Preto\n[5] - Verde\n[6] - Amarelo\n[7] - Branco\nOpção: '))
    for i in range(1):
        nomes.append(str(input('nome da marca: ')))
    
    histograma(cores[n])

elif op == 3:
    print('voce saiu do programa!!')
    
else:
    print('valor invalido!')