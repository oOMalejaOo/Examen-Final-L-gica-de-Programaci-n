import random

from heapsort import ordenar_heapsort
from mergesort import ordenar_mergesort


def generar_lista(n=10, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]


def comparar(lista):

    ordenada_h, it_h = ordenar_heapsort(lista)
    ordenada_m, it_m = ordenar_mergesort(lista)

    print(f"\nLista original: {lista}")
    print(f"Heapsort  -> {ordenada_h} | iteraciones: {it_h}")
    print(f"Mergesort -> {ordenada_m} | iteraciones: {it_m}")

    if it_h < it_m:
        print(f"\nResultado: Heapsort usó menos iteraciones ({it_h} vs {it_m}).")
    elif it_m < it_h:
        print(f"\nResultado: Mergesort usó menos iteraciones ({it_m} vs {it_h}).")
    else:
        print(f"\nResultado: ambos usaron las mismas iteraciones ({it_h}).")


def mostrar_menu():
    print("\n===== MENÚ DE ORDENAMIENTO =====")
    print("1. Ordenar con Heapsort")
    print("2. Ordenar con Mergesort")
    print("3. Ordenar con ambos y comparar iteraciones")
    print("4. Generar una nueva lista aleatoria")
    print("5. Mostrar lista actual")
    print("0. Salir")


def main():
    lista = generar_lista()
    print(f"Lista aleatoria generada: {lista}")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ordenada, it = ordenar_heapsort(lista)
            print(f"\nOriginal: {lista}\nOrdenada (Heapsort): {ordenada}\nIteraciones: {it}")
        elif opcion == "2":
            ordenada, it = ordenar_mergesort(lista)
            print(f"\nOriginal: {lista}\nOrdenada (Mergesort): {ordenada}\nIteraciones: {it}")
        elif opcion == "3":
            comparar(lista)
        elif opcion == "4":
            lista = generar_lista()
            print(f"\nNueva lista: {lista}")
        elif opcion == "5":
            print(f"\nLista actual: {lista}")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
