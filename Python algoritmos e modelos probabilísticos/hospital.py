import csv
import heapq

# Dicionário para definir as prioridades das doenças
prioridades = {
    "Sinusite": 1,
    "Alergia": 2,
    "Febre": 3,
    "Gripe": 4
}

# Função para carregar os pacientes e criar uma fila de prioridade
def criar_fila_prioridade(arquivo_csv):
    heap = []  # Fila de prioridade implementada com heap
    
    # Ler o arquivo CSV
    with open(arquivo_csv, 'r') as file:
        leitor_csv = csv.DictReader(file)
        
        for linha in leitor_csv:
            nome = linha['nome']
            doenca = linha['doenca']
            
            # A prioridade é inversa, pois heapq é min-heap por padrão
            prioridade = -prioridades[doenca]
            
            # Adicionar na fila (prioridade, nome, doença)
            heapq.heappush(heap, (prioridade, nome, doenca))
    
    return heap

# Função para exibir apenas os nomes em ordem de prioridade
def exibir_fila(fila):
    print("Fila de atendimento:")
    while fila:
        _, nome, _ = heapq.heappop(fila)
        print(nome)

# Caminho para o arquivo CSV
arquivo_csv = 'pacientes.csv'

# Criar e exibir a fila de prioridade
fila_prioridade = criar_fila_prioridade(arquivo_csv)
exibir_fila(fila_prioridade)
