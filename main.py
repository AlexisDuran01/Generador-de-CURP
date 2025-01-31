# Función para validar que se ingrese un número
def validar_numero(mensaje):
    # Usamos un bucle infinito para asegurarnos de que el valor ingresado sea válido.
    while True:
        # Mostramos el mensaje y tomamos la entrada del usuario con input().
        valor = input(mensaje)

        # Comprobamos si la entrada es un número usando el método isdigit() que retorna True si es un número.
        if valor.isdigit():  # Verifica si es un número
            # Si es un número, lo convertimos a entero y lo retornamos.
            return int(valor)
        else:
            # Si no es un número, mostramos un mensaje de error y seguimos pidiendo el valor.
            print("Por favor, ingresa un número válido.")

# Función para validar que se ingrese un texto con solo letras y más de dos caracteres
def validarCadena(mensaje):
    # Usamos un bucle infinito para asegurarnos de que el valor ingresado sea válido.
    while True:
        # Mostramos el mensaje y tomamos la entrada del usuario con input().
        valor = input(mensaje)

        # Comprobamos si la entrada contiene solo letras y tiene más de dos caracteres.
        if valor.isalpha() and len(valor) > 2:  # Verifica que solo contenga letras y tenga más de 2 caracteres
            # Si es válido, lo retornamos.
            return valor
        else:
            # Si no es válido, mostramos un mensaje de error y seguimos pidiendo el valor.
            print("Por favor, ingresa un texto válido (más de dos letras y solo letras).")

# Función para pedir un estado y validarlo
def elegir_estado():
    print("\nSelecciona tu estado de nacimiento:")
    # Mostramos todos los estados disponibles numerados
    for i, estado in enumerate(estados, 1):
        print(f"{i}. {estado}")

    # Usamos la función validar_numero para pedir que el usuario seleccione el estado
    estado_elegido = validar_numero("Selecciona el número de tu estado: ")

    # Validamos que el número ingresado sea un valor correcto dentro del rango de la lista
    if 1 <= estado_elegido <= len(estados):
        # Si es válido, obtenemos el estado de la lista según el número seleccionado.
        estado = estados[estado_elegido - 1]
        return estado
    else:
        # Si no está en el rango, mostramos un error.
        print("Estado no válido.")
        return elegir_estado()

# Función para pedir la fecha de nacimiento separada por día, mes y año
# Función para pedir la fecha de nacimiento separada por día, mes y año
def pedir_fecha_nacimiento():
    while True:
        dia = validar_numero("Ingresa el día de tu nacimiento (dd): ")
        if 1 <= dia <= 31:
            # Si el día es válido, continuamos
            break
        else:
            print("El día debe estar entre 1 y 31.")

    while True:
        mes = validar_numero("Ingresa el mes de tu nacimiento (mm): ")
        if 1 <= mes <= 12:
            # Si el mes es válido, continuamos
            break
        else:
            print("El mes debe estar entre 1 y 12.")

    while True:
        año = validar_numero("Ingresa el año de tu nacimiento (aaaa): ")
        if año >= 1900:
            # Si el año es mayor o igual a 1900, continuamos
            break
        else:
            print("El año debe ser 1900 o posterior.")

    # Si los valores son válidos, devolvemos la fecha en formato "dd/mm/aaaa"
    return f"{dia:02d}/{mes:02d}/{año}"

# Lista de estados en México (abreviaturas)
estados = [
    "AGU", "BCN", "BCS", "CAM", "CHP", "CHH", "COA", "COL", "DIF", "DUR",
    "GTO", "GRO", "HID", "JAL", "MIC", "MOR", "NAY", "NLE", "OAX", "PUE",
    "QUE", "ROO", "SLP", "SIN", "SON", "TAB", "TAM", "TLA", "VER", "YUC", "ZAC"
]

  # Función para encontrar la primera consonante interna
def primera_consonante_interna(palabra):
        consonantes = "BCDFGHJKLMNPQRSTVWXYZ"  # Consonantes en español
        for letra in palabra[1:]:  # Comenzamos desde la segunda letra
            if letra.upper() in consonantes:
                return letra.upper()
        return 'X'  # Retornar 'X' si no hay consonante interna

# Función para generar la CURP
def generar_curp(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, estado):
    # Primero, tomamos las primeras dos letras del apellido paterno y materno, y el primer nombre
    curp = apellidoPaterno[:2].upper() + apellidoMaterno[0].upper() + nombre[0].upper()
    # Añadimos la fecha de nacimiento (día, mes y año)
    # La fecha de nacimiento se recibe en formato "dd/mm/yyyy"
    # Usamos el método split('/') para separar el día, mes y año
    dia, mes, año = fechaNacimiento.split('/')  # Esto divide la cadena en partes

    # Ahora formamos la parte de la CURP que corresponde a la fecha de nacimiento
    # Al usar [2:], estamos diciendo "toma todos los caracteres desde el índice 2 hasta el final de la cadena".
    curp += año[2:]  # Añadimos los últimos dos dígitos del año a la CURP

    # Añadimos el mes y el día a la CURP
    curp += mes  # Añadimos el mes (por ejemplo "04" para abril)
    curp += dia  # Añadimos el día (por ejemplo "15")

    # Añadimos el sexo (H o M)
    curp += sexo

    # Añadimos las primeras dos letras del estado de nacimiento
    curp += estado[:2].upper()  # Solo las dos primeras letras del estado

    # Obtener la primera consonante interna de cada parte
    consonantePaterno = primera_consonante_interna(apellidoPaterno)
    consonanteMaterno = primera_consonante_interna(apellidoMaterno)
    consonanteNombre = primera_consonante_interna(nombre)

    # Añadir las consonantes internas al final de la CURP
    curp += consonantePaterno + consonanteMaterno + consonanteNombre

    # Retornamos la CURP generada
    return curp

# Función principal para pedir los datos y generar la CURP
def pedir_datos():
    print("Generando CURP...")

    # Solicitar datos al usuario utilizando las funciones correspondientes
    nombre = validarCadena("Ingresa tu primer nombre: ")
    apellidoPaterno = validarCadena("Ingresa tu apellido paterno: ")
    apellidoMaterno = validarCadena("Ingresa tu apellido materno: ")
    fechaNacimiento = pedir_fecha_nacimiento()  # Llamamos a la función para pedir la fecha de nacimiento
    sexo = input("Ingresa tu sexo (H/M): ").upper()  # Usamos upper() para asegurar que la letra sea mayúscula

    # Llamamos a la función para elegir el estado
    estado = elegir_estado()

    # Generar y mostrar la CURP utilizando los datos
    curp = generar_curp(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, estado)
    print(f"\nTu CURP es: {curp}")

# Ejecutar la función para obtener los datos
pedir_datos()





