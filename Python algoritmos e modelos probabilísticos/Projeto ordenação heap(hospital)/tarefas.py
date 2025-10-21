
import matplotlib.pyplot as plt


class Tarefas:
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