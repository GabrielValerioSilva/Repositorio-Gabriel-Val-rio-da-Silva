import random

direita = 1 #Define constantes para representar as direções possíveis: direita: Representada pelo valor 1. esquerda: Representada pelo valor 2.
esquerda = 2

posicoes = []
movimentacoes = []
#posicoes: Lista para armazenar as posições ocupadas durante o passeio. movimentacoes: Lista para registrar as movimentações ("direita" ou "esquerda").

posicao = 0
#Inicializa a posição atual no valor 0 (posição de partida).
posicoes.append(posicao)
movimentacoes.append('inicio')
#Registra a posição inicial (0) e a movimentação inicial como 'inicio'.


for i in  range(1,4): #Laço para realizar três rodadas de movimento (1 a 3).
    dir_ou_esq = random.randint(1,2) #Gera aleatoriamente um número inteiro entre 1 (direita) e 2 (esquerda).
     
    if dir_ou_esq == direita:
     movimentacoes.append('direita')
     posicao += 1
     #Se o número gerado for 1 (direita):=Adiciona 'direita' à lista de movimentações.Incrementa a posição atual em 1.
     
    elif dir_ou_esq == esquerda:
        posicao -= 1
        movimentacoes.append('esquerda')
        #Se o número gerado for 2 (esquerda): Adiciona 'esquerda' à lista de movimentações. Decrementa a posição atual em 1.
        
        
    posicoes.append(posicao) #Registra a nova posição na lista posicoes.

for index, (p,m) in enumerate(zip(posicoes,movimentacoes)):#Itera sobre as listas posicoes e movimentacoes simultaneamente usando zip().O índice (index) indica a rodada atual.
    print(f'Rodada: {index}')
    print(f'Posicao: {p}')
    print(f'Movimentacao: {m}')
    print() #Exibe a rodada, a posição e a movimentação correspondentes de forma formatada.