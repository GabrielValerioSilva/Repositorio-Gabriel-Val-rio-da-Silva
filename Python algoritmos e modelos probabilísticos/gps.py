import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from math import radians, sin, cos, sqrt, atan2

# Carregar os dados do CSV
dados = pd.read_csv("cidades.csv")
# Função para calcular a distância geográfica (fórmula de Haversine)
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Converter coordenadas para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Fórmula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    raio_terra = 6371  # Raio médio da Terra em km
    return raio_terra * c

# Adicionar uma coluna com a distância calculada
dados['distancia'] = dados.apply(lambda row: calcular_distancia(
    row['latitude_origem'], row['longitude_origem'],
    row['latitude_destino'], row['longitude_destino']), axis=1)
# Selecionar as features (entrada) e o target (tempo)
X = dados[['distancia']]
y = dados['tempo']
# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Criar e treinar o modelo de regressão
modelo = LinearRegression()
modelo.fit(X_train, y_train)
# Função para prever o tempo de viagem baseado no nome das cidades
def prever_tempo_por_cidades(origem, destino):
    # Buscar coordenadas das cidades no CSV
    try:
        cidade_origem = dados[dados['origem'] == origem].iloc[0]
        cidade_destino = dados[dados['destino'] == destino].iloc[0]
    except IndexError:
        raise ValueError(f"Cidades {origem} ou {destino} não encontradas no CSV.")
    
    # Extrair coordenadas
    lat1, lon1 = cidade_origem['latitude_origem'], cidade_origem['longitude_origem']
    lat2, lon2 = cidade_destino['latitude_destino'], cidade_destino['longitude_destino']
    
    # Calcular distância
    distancia = calcular_distancia(lat1, lon1, lat2, lon2)
    
    # Prever tempo
    entrada = [[distancia]]
    tempo_previsto = modelo.predict(entrada)
    return tempo_previsto[0]

# Exemplo de uso: prever o tempo de Curitiba para Campinas
origem = "Curitiba"
destino = "Belo Horizonte"

try:
    tempo = prever_tempo_por_cidades(origem, destino)
    horas = int(tempo // 60)  # Parte inteira das horas
    minutos = int(tempo % 60)  # Parte restante em minutos
    print(f"Tempo em média previsto para o trajeto de {origem} até {destino}: {horas} horas e {minutos} minutos")
except ValueError as e:
    print(e)
