
lista=[]

def main():
    menu()

def menu():
    while True:
        print("\nLista:",lista)
        print("Escoge una de las siguientes opciones: "
          "\n1. Insert "  # Insertar un elemento en una lista en una posición específica
          "\n2. Append "  # Agregar un elemento al final de la lista
          "\n3. Remove "  # Eliminar la primera aparición de un elemento en la lista
          "\n4. Pop "  # Eliminar y devolver el último elemento de la lista
          "\n5. Clear "  # Eliminar todos los elementos de la lista
          "\n6. Extend "  # Agregar los elementos de otra lista al final de la lista actual
          "\n7. Reverse "  # Invertir el orden de los elementos en la lista
          "\n8. Sort "  # Ordenar los elementos de la lista en orden ascendente
          "\n9. Index "  # Devolver el índice de la primera aparición de un elemento en la lista
          "\n10. Salir\n")

        # Obtenemos el valor y le quitamos el espacio al inicio y al final
        valor = input("Ingresa una de las opciones (1-10): ").strip()

        if not valor.isdigit():
            print("\nDebe ingresar un número válido")

            '''Hace que el bucle while regrese al inicio, sin ejecutar 
            las siguientes líneas de código en esa iteración
            
            Esto evita que el programa intente convertir una entrada inválida en un numero
            '''
            continue

        opcion = int(valor)

        if opcion == 1:
            print("\nSe escogió la opción insert\n")
            insert()
        elif opcion == 2:
            print("\nSe escogió la opción append\n")
            append()
        elif opcion == 3:
            print("\nSe escogió la opción remove\n")
            remove()
        elif opcion == 4:
            print("\nSe escogió la opción pop\n")
            pop()
        elif opcion == 5:
            print("\nSe escogió la opción clear\n")
            lista.clear()
        elif opcion == 6:
            print("\nSe escogió la opción extend\n")
            extend()
        elif opcion == 7:
            print("\nSe escogió la opción reverse\n")
            lista.reverse()
        elif opcion == 8:
            print("\nSe escogió la opción sort\n")
            lista.sort()
        elif opcion == 9:
            print("\nSe escogió la opción index\n")
            index()
        elif opcion == 10:
            print("\nFinalizando programa\n")
            break
        else:
            print("\nOpción no válida. Ingresa un número entre 1 y 10.")


def insert():
    """
    Función para insertar un elemento en una lista en una posición específica.
    Valida que la posición ingresada sea un número entero y maneja posibles errores.
    """
    posicion = input('Ingresa la posicion en donde deseas insertar: ').strip()
    if not posicion.isdigit():
        print("\nIngresa un numero valido. Intentalo de nuevo")
        return

    posicion = int(posicion)
    elemento = input('Ingresa el elemento a insertar: ').strip()

    # Insert nos sirve para insertar un elemento en la posición especificada
    lista.insert(posicion, elemento)

def append():
    elemento = input('Ingresa el elemento a insertar al final: ').strip()
    lista.append(elemento)

def remove():

    if len(lista) == 0:
        print("La lista esta vacia")
        return

    elemento = input('Ingresa el elemento que desea eliminar: ').strip()
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("El elemento no esta en la lista")

def pop():
    if len(lista) == 0:
        print("La lista esta vacia")
        return
    lista.pop()

def extend():
    auxiliar=[]
    cantidad= input("Ingresa la cantidad de elementos que quieras agregar: ")
    if not cantidad.isdigit():
        print("La cantidad debe de ser un numero")
        return
    cantidad=int(cantidad)
    for i in range(cantidad):
        auxiliar.append(input(f"Ingresa el elemento de la posicion {i}: "))
    lista.extend(auxiliar)

def index():

    if len(lista) == 0:
        print("La lista esta vacia")
        return

    elemento = input('Ingresa el elemento que quieres buscar en la lista: ').strip()
    if elemento in lista:
        indice=lista.index(elemento)
        print(f"\nEl elemento '{elemento}' aparece por primera vez en el índice {indice}")
    else:
        print("El elemento no esta en la lista")

main()