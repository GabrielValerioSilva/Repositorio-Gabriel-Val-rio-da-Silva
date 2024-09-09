import tkinter as tk
from tkinter import messagebox
import threading
import time
import os
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ContaDoBancoGv:
    def __init__(self, usuario, saldo_inicial):
        self.usuario = usuario
        self.saldoficticio = saldo_inicial
        self.tempos = []
        self.saldos = []

    def atualizar_saldoficticio(self, percentual):
        self.saldoficticio *= 1 + percentual  # Aumenta ou diminui o saldo em percentual
        self.tempos.append(time.time())
        self.saldos.append(self.saldoficticio)

    def atualizar_saldoficticio_periodicamente(self, label_contador):
        while True:
            for i in range(60, 0, -1):  # Mudado para 60 segundos
                label_contador.config(text=f"Atualizando em {i} segundos")
                time.sleep(1)
            self.atualizar_saldoficticio(-0.02)  # Diminui o saldo em 2%
            label_contador.config(text="Saldo fictício atualizado!")
            self.plotar_grafico()

    def plotar_grafico(self):
        plt.plot(self.tempos, self.saldos)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Saldo Fictício')
        plt.title('Variação do Saldo Fictício')
        plt.pause(0.01)

def iniciar_janela_grafico(conta):
    root = tk.Tk()
    root.title("Gráfico do Saldo")
    root.geometry("600x400")

    label_grafico = tk.Label(root, text="Gráfico do Saldo")
    label_grafico.pack()

    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=root)  # Ajuste para tornar o gráfico compatível com o tkinter
    canvas.get_tk_widget().pack()

    def atualizar_grafico():
        ax.clear()
        ax.plot(conta.tempos, conta.saldos)
        ax.set_xlabel('Tempo (s)')
        ax.set_ylabel('Saldo Fictício')
        ax.set_title('Variação do Saldo Fictício')
        canvas.draw()
        canvas.flush_events()
        root.after(100, atualizar_grafico)  # Reduzindo o intervalo de atualização

    atualizar_grafico()
    plt.ion()  # Ativando o modo de interatividade
    root.mainloop()

window = tk.Tk()

# Define o caminho absoluto para o arquivo GIF
caminho_absoluto_gif = os.path.abspath('dinheirotest.gif')

label_usuario = tk.Label(window, text="usuário:")
entrada_usuario = tk.Entry(window)
label_saldoficticio = tk.Label(window, text="saldo fictício:")
entrada_saldoficticio = tk.Entry(window)
botao_ok = tk.Button(window, text="OK")
label_saldoficticio_atual = tk.Label(window, text="")
botao_refresh = tk.Button(window, text="Refresh", state="disabled")
label_contador = tk.Label(window, text="")  # Adicionado label_contador

# Adicionado campo de entrada para a resposta do usuário e botão para submeter a resposta
label_integral = tk.Label(window, text="Integral:")
label_resposta = tk.Label(window, text="Resposta:")
entrada_resposta = tk.Entry(window)
botao_submeter = tk.Button(window, text="Submeter")

# Adicionando o Label para exibir o GIF
gif_label = tk.Label(window)
gif = tk.PhotoImage(file=caminho_absoluto_gif)  # Caminho absoluto para o arquivo GIF
gif_label.config(image=gif)
gif_label.image = gif  # Mantenha uma referência ao GIF para evitar que ele seja excluído da memória

# Lista de integrais pré-definidas e suas soluções
integrais = [
    ("∫x dx", "x^2/2"),
    ("∫x^2 dx", "x^3/3"),
    ("∫x dx", "x^2/2"),
    ("∫x^2 dx", "x^3/3"),
    ("∫x^3 dx", "x^4/4"),
    ("∫e^x dx", "e^x"),
    ("∫sin(x) dx", "-cos(x)"),
    ("∫cos(x) dx", "sin(x)"),
    ("∫∫3xy + 2y dydx", "(3/4)x^2y^2+xy^2"),
    ("∫2x^3 + 1/4x dx", "2x^4/4+ln|4x|"),
    ("∫∫2yx^3 + 5cos(y) dydx", "(1/4)x^4y+5xcos(y)"),
    ("∫∫∫2yx^3 + 7z^4 dzdxdy", "(1/4)y^2x^4z+(7/40)yxz^5"),
    ("∂f/∂x = 2x+3y","2"),
    ("∂f^2/∂x^2 = 2x^2+3y","4"),
    ("∫ln(x) + e^x dx","xln(x)-x+e^x"),
    ("dx/dy=2x", "y=x^2"),
    ("∫(e^(3x)) dx", "(1/3)e^(3x)"),

    # Adicione mais integrais aqui
]
integral_atual = None

def on_ok():
    global conta, integral_atual
    usuario = entrada_usuario.get()
    saldoficticio = float(entrada_saldoficticio.get())
    conta = ContaDoBancoGv(usuario, saldoficticio)
    threading.Thread(target=conta.atualizar_saldoficticio_periodicamente, args=(label_contador,), daemon=True).start()
    threading.Thread(target=iniciar_janela_grafico, args=(conta,), daemon=True).start()
    messagebox.showinfo("Bem-vindo", f"Olá, {conta.usuario}! Seu saldo fictício será atualizado a cada 60 segundos.")
    botao_refresh.config(state="normal")
    botao_ok.config(state="disabled")
    atualizar_label_saldoficticio()
    integral_atual = random.choice(integrais)
    label_integral.config(text=f"Integral: {integral_atual[0]}")

botao_ok.config(command=on_ok)  # Configurado o comando para o botão OK

def on_refresh():
    conta.atualizar_saldoficticio(0)
    label_saldoficticio_atual.config(text=f"Saldo: R${conta.saldoficticio:.2f}")

botao_refresh.config(command=on_refresh)

def on_submeter():
    global integral_atual
    resposta = entrada_resposta.get()
    # Verifica se a resposta está correta
    if resposta == integral_atual[1]:  # Substitua 'resposta correta' pela resposta correta
        conta.atualizar_saldoficticio(0.02)  # Aumenta o saldo em 2%
        messagebox.showinfo("Parabéns", "Você acertou! Seu saldo fictício foi aumentado em 2%.")
    else:
        conta.atualizar_saldoficticio(-0.02)  # Diminui o saldo em 2%
        messagebox.showinfo("Desculpe", "Sua resposta está incorreta. Tente novamente.")
    integral_atual = random.choice(integrais)
    label_integral.config(text=f"Integral: {integral_atual[0]}")

botao_submeter.config(command=on_submeter)  # Configurado o comando para o botão Submeter

def atualizar_label_saldoficticio():
    label_saldoficticio_atual.config(text=f"Saldo: R${conta.saldoficticio:.2f}")
    window.after(500, atualizar_label_saldoficticio)  # Reduzindo o intervalo de atualização

label_usuario.pack()
entrada_usuario.pack()
label_saldoficticio.pack()
entrada_saldoficticio.pack()
botao_ok.pack()
label_saldoficticio_atual.pack()
botao_refresh.pack()
label_contador.pack() # Adicionado label_contador ao layout
label_integral.pack()  # Adicionado label_integral ao layout
label_resposta.pack()  # Adicionado label_resposta ao layout
entrada_resposta.pack()  # Adicionado entrada_resposta ao layout
botao_submeter.pack()  # Adicionado botao_submeter ao layout
gif_label.pack()

# Define o título e o ícone da janela e a cor de fundo diretamente no código
window.title("BANCOGV")  # Muda o nome da janela
window.iconbitmap('iconbaco.ico')  # Muda o ícone da janela
window.geometry("800x600")
window.configure(bg='red')

window.mainloop()
