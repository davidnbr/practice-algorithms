def merge_sort(lista):
    # Caso base
    if len(lista) == 1:
        return lista
    # Caso recursivo
    else:
        lista_izq = lista[:len(lista) // 2] # División entera, lista desde inicio a punto medio
        lista_der = lista[len(lista) // 2:] # Lista desde punto medio a final

        lista_izq = merge_sort(lista_izq) # Guardo lista izquierda ordenada
        lista_der = merge_sort(lista_der) # Guardo lista derecha ordenada

        return merge(lista_izq, lista_der) # Llamo a la función merge con las listas ordenadas

def merge(lista_izq, lista_der):
    lista_ord = []

    while len(lista_izq) > 0 and len(lista_der) > 0:
        if lista_izq[0] < lista_der[0]:
            lista_ord.append(lista_izq[0])
            lista_izq.pop(0) # Elimino primer elemento de lista_izq
        else:
            lista_ord.append(lista_der[0])
            lista_der.pop(0) # Elimino primer elemento de lista_der

    if len(lista_izq) > 0:
        lista_ord += lista_izq
    elif len(lista_der) > 0:
        lista_ord += lista_der

    return lista_ord

if __name__ == '__main__':
    lista = [64, 34, 25, 12, 22, 11, 90, 1, 20, -4, 7, 3]

    print(lista)
    print(merge_sort(lista))