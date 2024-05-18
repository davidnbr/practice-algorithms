# Algoritmo de Radix Sort para ordenar lista de números

def radix_sort(lista):
    n = 0 # Número de dígitos del número más grande de la lista

    for elem in lista:
        if len(str(elem)) > n:
            n = len(str(elem))
    
    for i in range(len(lista)):
        lista[i] = str(lista[i]).zfill(n) # Relleno con ceros a la izquierda para que todos los números tengan la misma longitud

    for j in range(n-1, -1, -1):
        # Se repite desde el digito menos significativo al mas significativo
        grupos = [[] for i in range(10)]

        for i in range(len(lista)):
            grupos[int(lista[i][j])].append(lista[i]) # Guardo a numero en grupo de acuerdo al dígito en la posición j
        
        lista = []
        for grupo in grupos:
            lista += grupo # Concateno todos los grupos en lista
    
    return [int(elem) for elem in lista]

if __name__ == '__main__':
    from random import randint

    lista = [str(randint(0, 200)) for i in range(10)]
    print(lista)
    print(radix_sort(lista))
