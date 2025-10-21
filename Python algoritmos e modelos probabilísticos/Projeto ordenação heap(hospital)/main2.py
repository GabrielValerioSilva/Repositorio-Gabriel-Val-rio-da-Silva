import pandas as pd
from tarefas import Tarefas as tf

file_path = 'dados.csv'

df = pd.read_csv(file_path,sep=";")

print(df)

print(df.iloc[0])

# Obter o maior valor na coluna "tempo"
maior_tempo = df["tempo"].max()
print(maior_tempo)

print("----")
m=0
for i, linha in df.iterrows():
     tempo = linha["tempo"]
     print(tempo)
     if(tempo>m):
        m=tempo
print("MAIOR ")
print(m)