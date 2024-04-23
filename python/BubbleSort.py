def bubble_sort(lista):
    n = len(lista)

    for i in range(1, n):
        for j in range(n-1):
            if lista[j]>lista[j+1]:
                # Intercambio de valores si j es mayor que j+1
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    
    return lista

lista = [64, 34, 25, 12, 22, 11, 90, 1, 20, -4, 7, 3]

print(lista)
print(bubble_sort(lista))
