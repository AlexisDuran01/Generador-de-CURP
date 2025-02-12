# Lista principal de categorías (vacía al inicio)
categorias = []


def mostrar_menu():
    print("\n1. Administrar categorias")
    print("2. Administrar pendientes de una categoria")
    print("3. Mostrar categorias y pendientes")
    print("4. Salir")
    return input("\nSelecciona una opcion: ")

def mostrar_categorias():
    if not categorias:
        print("\nNo hay categorias disponibles")
    else:
        print("\nCategorías disponibles:")
        for i, categoria in enumerate(categorias):
            print(f"{i}. {categoria[0].upper()}")

def agregar_categoria():
    nombre = input("\nIngresa el nombre de la nueva categoria: ").strip()
    if nombre:
        categorias.append([nombre, []])
        print(f"Categoría '{nombre.upper()}' agregada correctamente")
    else:
        print("El nombre no puede estar vacio")

def renombrar_categoria():
    if not categorias:
        print("\nNo hay categorías disponibles para renombrar")
        return
    mostrar_categorias()
    try:
        index = int(input("\nSelecciona el numero de la categoria a renombrar: "))
        nuevo_nombre = input("Ingresa el nuevo nombre: ").strip()
        if nuevo_nombre:
            categorias[index][0] = nuevo_nombre.upper()
            print("Categoria renombrada correctamente")
        else:
            print("El nombre no puede estar vacio")
    except (ValueError, IndexError):
        print("Seleccion invalida")

def eliminar_categoria():
    if not categorias:
        print("\nNo hay categorías disponibles para eliminar")
        return
    mostrar_categorias()
    try:
        index = int(input("\nSelecciona el numero de la categoria a eliminar: "))
        categorias.pop(index)
        print("Categoria eliminada correctamente")
    except (ValueError, IndexError):
        print("Seleccion invalida")


def administrar_pendientes():
    mostrar_categorias()
    if not categorias:
        return
    try:
        index = int(input("\nSelecciona el numero de la categoría: "))
        categoria = categorias[index]
        while True:
            print(f"\n Pendientes en {categoria[0]}")
            for i, pendiente in enumerate(categoria[1]):
                print(f" {i}. {pendiente.lower()}")
            print("")
            print("1. Agregar pendiente")
            print("2. Renombrar pendiente")
            print("3. Eliminar pendiente")
            print("4. Ordenar pendientes")
            print("5. Volver al menu principal")
            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                tarea = input("\nIngresa la nueva tarea: ").strip()
                if tarea:
                    categoria[1].append(tarea.lower())
                    print("Pendiente agregado correctamente")
            elif opcion == "2":
                try:
                    i = int(input("\nSelecciona el numero del pendiente a renombrar: "))
                    nuevo_nombre = input("Nuevo nombre: ").strip()
                    if nuevo_nombre:
                        categoria[1][i] = nuevo_nombre.lower()
                        print("Pendiente renombrado correctamente")
                except (ValueError, IndexError):
                    print("Seleccion inválida")
            elif opcion == "3":
                try:
                    i = int(input("\nSelecciona el numero del pendiente a eliminar: "))
                    categoria[1].pop(i)
                    print("Pendiente eliminado correctamente")
                except (ValueError, IndexError):
                    print("Selección inválida")
            elif opcion == "4":
                categoria[1].sort()
                print("Pendientes ordenados correctamente")
            elif opcion == "5":
                break
            else:
                print("Opcion invalida")
    except (ValueError, IndexError):
        print("Seleccion invalida")

def mostrar_todo():
    if not categorias:
        print("\nNo hay categorías disponibles")
    else:
        print("\nCategorias y Pendientes")
        for categoria in categorias:
            print(f"{categoria[0].upper()}")
            if not categoria[1]:
                print(" - (No hay pendientes)")
            else:
                for pendiente in categoria[1]:
                    print(f"   - {pendiente.lower()}")

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        print("\n1. Agregar categoria")
        print("2. Renombrar categoria")
        print("3. Eliminar categoria")
        sub_opcion = input("\nSelecciona una opcion: ")
        if sub_opcion == "1":
            agregar_categoria()
        elif sub_opcion == "2":
            renombrar_categoria()
        elif sub_opcion == "3":
            eliminar_categoria()
        else:
            print("Opcion invalida")
    elif opcion == "2":
        administrar_pendientes()
    elif opcion == "3":
        mostrar_todo()
    elif opcion == "4":
        print("\nSaliendo del programa........")
        break
    else:
        print("Opcion invalida")
