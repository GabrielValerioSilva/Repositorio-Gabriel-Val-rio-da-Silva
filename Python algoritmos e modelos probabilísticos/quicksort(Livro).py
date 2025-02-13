def quicksort(array): 
    if len(array) < 2: 
        return array #1
    else:
        pivo = array[0] #2
        menores = [i for i in array[1:] if i <= pivo]#3
        maiores = [i for i in array[1:] if i > pivo]#4
        return quicksort(menores) + [pivo] + quicksort(maiores)
print(quicksort([10, 5, 2, 3]))

#Base:
#1. Se o array tiver menos de 2 elementos, retorna o array--
#2. Define o pivo como o primeiro elemento do array---Caso recursivo
#3. Cria um array com todos os elementos menores que o pivo---Subarray
#4. Cria um array com todos os elementos maiores que o pivo---- Subarray 2