import matplotlib.pyplot as plt

def plotar_grafico(hospitais):
    nomes = [h["hospital"] for h in hospitais]
    tempos = [h["tempo_espera"] for h in hospitais]

    plt.figure(figsize=(10, 6))
    plt.barh(nomes, tempos, color='skyblue')
    plt.xlabel("Tempo de Espera (minutos)")
    plt.ylabel("Hospitais")
    plt.title("Tempo de Espera nos Hospitais")
    plt.gca().invert_yaxis()  # Inverte o eixo Y para mostrar o menor tempo no topo
    plt.show()

def laco(lista):
    for i, hospital in enumerate(lista):
        print(f"{i}. {hospital['hospital']} - {hospital['tempo_espera']}")
    plotar_grafico(lista)
    
def ordena(dados,ordem):
    return sorted(dados, key=lambda x: x["tempo_espera"], reverse=ordem)

def ordenaAlpha(dados,ordem):
    return sorted(dados, key=lambda x: x["hospital"], reverse=ordem)

def mostra(lista):
    print("Original")
    laco(lista)
    
    print("Crescente")
    lista = ordena(lista,False)
    laco(lista)
    
    print("Decrescente")
    lista = ordena(lista,True)    
    laco(lista)
            
hospital_data = [
    {"hospital": "Hospital A", "tempo_espera": 45},
    {"hospital": "Hospital B", "tempo_espera": 30},
    {"hospital": "Hospital C", "tempo_espera": 60},
    {"hospital": "Hospital L", "tempo_espera": 60},
    {"hospital": "Hospital D", "tempo_espera": 20},
    {"hospital": "Hospital E", "tempo_espera": 50},
    {"hospital": "Hospital X", "tempo_espera": 10},
    {"hospital": "Hospital F", "tempo_espera": 25},
]

mostra(hospital_data)

print("Alfabeto")
d = ordenaAlpha(hospital_data,False)
laco(d)