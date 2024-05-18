# Algoritmo Heap Sort para ordenar lista de números

def heap_sort(lista):
    lista_final = []

    for i in range(len(lista)//2-1,-1,-1): # Rango descendente hasta 0
        lista = heapify(lista, i)
    
    for i in range(0, len(lista)):
        lista[0], lista[-1] = lista[-1], lista[0] # Intercambio primer elemento por ultimo elemento de lista
        lista_final.append(lista.pop()) # Agrego ultimo elemento a lista_final y elimino de lista
        lista = heapify(lista, 0)

    return lista_final

def heapify(lista, i):
    # i nodo desde el que aplica heapify
    # Si nodo tiene dos hijos
    pos_derecho = 2*i+2 # hijo derecho
    pos_izquierdo = 2*i+1 # hijo izquierdo
    if pos_derecho <= len(lista)-1: # Si tiene hijo derecho (dos hijos)
        if lista[pos_izquierdo] <= lista[pos_derecho]: # Si hijo derecho es menor que hijo izquierdo
            min = pos_izquierdo # hijo izquierdo
        else:
            min = pos_derecho
        
        if lista[i] > lista[min]:
            lista[i], lista[min] = lista[min], lista[i]

            heapify(lista, min)

    # Si nodo tiene un hijo    
    elif pos_izquierdo <= len(lista)-1:
        if lista[i] > lista[pos_izquierdo]:
            lista[i], lista[pos_izquierdo] = lista[pos_izquierdo], lista[i] # Nodo padre donde esta hijo e hijo donde estaba padre
    
    return lista

if __name__ == '__main__':
    lista = [10, 90, 1, 20, -4, 7,3, 35, 42, 18, 72, -6, 11]
    print(lista)
    print(heap_sort(lista))
