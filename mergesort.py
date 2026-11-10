def ordenar_mergesort(lista):

    def ordenar(datos):
        if len(datos) <= 1:
            return datos, 0

        medio = len(datos) // 2
        izquierda, it_izq = ordenar(datos[:medio])
        derecha, it_der = ordenar(datos[medio:])
        mezclada, it_mez = mezclar(izquierda, derecha)
        return mezclada, it_izq + it_der + it_mez

    def mezclar(izquierda, derecha):
        resultado = []
        iteraciones = 0
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            iteraciones += 1
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado, iteraciones

    return ordenar(lista.copy())
