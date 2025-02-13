import  random 

coroas = []
media = 0

for i in range(1,11):
    experimento = [ random.randint(1,2) for i in  range (100) ]
    cara = experimento.count(1)
    coroa = experimento.count(2)
    
    coroas.append(coroa)
    
    media = sum(coroas)/len(coroas)
    
    print(f'Experimento {i}')
    print(f'Média: {media}')
    print()        