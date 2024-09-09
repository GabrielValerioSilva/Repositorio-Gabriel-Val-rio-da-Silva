import requests
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def buscar_palavra_Goku_google(api_key1, search_engine_id1, termo_de_busca1, periodo1): #Função que recebe 4 parâmetros/argumentos 

    url_base = "*********"  # URL  da API do Google Custom Search 

    # Parâmetros 
    # 'key' especifica a chave de API do Google Custom Search
    #'cx' especifica o ID do mecanismo de pesquisa  do Google Custom Search
    #'q'  especifica o termo de busca,"Goku"seria  o termo como o valor deste parâmetro 
    parametros = {
        "key": api_key1,
        "cx": search_engine_id1,
        "q": termo_de_busca1,
        "dateRestrict": f"{periodo1}d"
    }

    # requisição à API
    requisição  = requests.get(url_base, params=parametros)

    # Verifica se a requisição foi bem-sucedida
    if requisição .status_code == 200:
        # Retorna o número de resultados
        dados = requisição .json()
        if 'searchInformation' in dados:
            return int(dados['searchInformation']['totalResults'])
        else:
            return "Erro: Não foi possível obter informações de pesquisa."
    else:
        return f"Erro {requisição .status_code}: Não foi possível realizar a busca."




def plotar_janela_com_numero(numero_de_resultados):
    plt.text(2024, numero_de_resultados, f'{numero_de_resultados} vezes', ha='right', va='bottom')




def grafico_Goku(numero_de_resultados, periodo1): 
    # função para gerar o gráfico com a quantidade de vezes que a palavra "Goku" apareceu durante o tempo
    anos = list(range(2020, 2025))
    resultados_por_ano = []

    for ano in anos:
        # Calcula o número de resultados para cada ano individualmente
        resultados_ano = buscar_palavra_Goku_google(API_KEY1, SEARCH_ENGINE_ID1, termo_de_busca1, f"y{ano}")
        resultados_por_ano.append(resultados_ano)

    plt.figure(figsize=(10, 6))
    plt.plot(anos, resultados_por_ano, marker='o')
    plt.title('Quantidade de vezes que a palavra "Goku" apareceu por ano')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de vezes')
    plt.grid(True)
    plt.xticks(anos)
    plt.show()










# Carregando API_KEY e SEARCH_ENGINE_ID a partir dos arquivos txt
API_KEY = open('API_KEY1.txt').read().strip()  #chave da api
SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID1.txt').read().strip()#ID

#buscar o termo Goku
termo_de_busca1 = "Goku"

periodo1 = 1542   # período de 1 de janeiro de 2020 até 31 de março de 2024

# Chama a função para buscar o número de resultados
numero_de_resultados = buscar_palavra_Goku_google(API_KEY1, SEARCH_ENGINE_ID1, termo_de_busca1, periodo1)

mensagem = f'O termo "{termo_de_busca1}" apareceu aproximadamente {numero_de_resultados} vezes nos resultados de pesquisa do Google de 2020 até março de 2024.'



# Mostrar mensagem com Tkinter
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

messagebox.showinfo("Número de Resultados", mensagem)




print(f'O termo "{termo_de_busca1}" apareceu aproximadamente {numero_de_resultados} vezes nos resultados de pesquisa do Google de 2020 até março de 2024.')



grafico_Goku(numero_de_resultados, periodo1)