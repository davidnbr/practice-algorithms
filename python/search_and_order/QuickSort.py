# Uso de algoritmo Quick Sort para ordernar lista de números
# Tiene varias versiones dependiendo como se escoja el pivote
# En este caso se escoge el último elemento de la lista como pivote
from random import randint

def quick_sort(lista):
    # Caso base
    if len(lista) <= 1:
        # Lista ya ordenada
        return lista
    
    # Caso recursivo
    pivote = lista.pop() # Ultimo elemento de lista como pivote
    #pivote = lista.pop(randint(0, len(lista) - 1)) # Elemento aleatorio de lista como pivote
    lista_izq = []
    lista_der = []

    for elem in lista:
        if elem <= pivote:
            lista_izq.append(elem)
        else:
            lista_der.append(elem)
    
    lista_izq = quick_sort(lista_izq)
    lista_der = quick_sort(lista_der)

    return lista_izq + [pivote] + lista_der

lista = [64, 34, 25, 12, 22, 11, 90, 1, 20, -4, 7, 3]
print(lista)
print(quick_sort(lista))
