def ordenar_heapsort(lista):

    datos = lista.copy()
    n = len(datos)
    iteraciones = 0

    def hundir(inicio, fin):
        """Hunde el elemento en 'inicio' dentro del montículo máximo [0, fin)."""
        nonlocal iteraciones
        raiz = inicio
        while True:
            hijo = 2 * raiz + 1
            if hijo >= fin:
                break
            # Elegir el hijo mayor
            if hijo + 1 < fin:
                iteraciones += 1
                if datos[hijo + 1] > datos[hijo]:
                    hijo += 1

            iteraciones += 1
            if datos[raiz] < datos[hijo]:
                datos[raiz], datos[hijo] = datos[hijo], datos[raiz]
                raiz = hijo
            else:
                break


    for i in range(n // 2 - 1, -1, -1):
        hundir(i, n)


    for fin in range(n - 1, 0, -1):
        datos[0], datos[fin] = datos[fin], datos[0]
        hundir(0, fin)

    return datos, iteraciones
