import hashlib


# Función para validar que se ingrese un número
def validar_numero(mensaje):

    # Usamos un bucle infinito para asegurarnos de que el valor ingresado sea válido.
    while True:

        valor = input(mensaje)  # Elimina espacios al inicio y final
        if not valor:
         print("No puede estar vacio el campo")
         #Continue se conoce como declaración de control de flujo
         '''Su función es saltar el resto del código dentro del bucle y pasar 
            directamente a la siguiente iteración '''
         continue

        # Comprobamos si la entrada es un número usando el método isdigit() que retorna True si es un número.
        if valor.isdigit():  # Verifica si es un número
            # Si es un número, lo convertimos a entero y lo retornamos.
            return int(valor)
        else:
            # Si no es un número, mostramos un mensaje de error y seguimos pidiendo el valor.
            print("Por favor, ingresa un número válido")

def validarCadena(mensaje):
    '''La variable mensaje es la que contiene el texto para pedir el dato en especifico
    y se usa en la funcion input'''
    while True:
        valor = input(mensaje).strip()  # Elimina espacios al inicio y final
        # Verifica si la cadena está vacía
        if not valor:
         print("No puede estar vacio el campo")
         #Continue se conoce como declaración de control de flujo
         '''Su función es saltar el resto del código dentro del bucle y pasar 
            directamente a la siguiente iteración '''
         continue

        # Verifica si la cadena tiene más de dos caracteres y solo contiene letras
        if valor.isalpha() and len(valor) > 2:
            return valor  # Retorna el valor válido

        # Mensaje de error si no cumple las condiciones
        print("Por favor, ingresa un texto válido (más de dos letras y solo letras)")


# Función para pedir un estado y validarlo
def elegir_estado():
    print("\nSelecciona tu estado de nacimiento:")
    # Mostramos todos los estados disponibles numerados
    for i, estado in enumerate(estados, 1):
        '''Se pone el cero ya que es la posicion dentro de la tupla a la cual queremos
        acceder siempre, osea el primer elemento en cada tupla'''
        print(f"{i}. {estado[0]}")

    # Usamos la función validar_numero para pedir que el usuario seleccione el estado
    estado_elegido = validar_numero("Selecciona el número de tu estado: ")

    # Validamos que el número ingresado sea un valor correcto dentro del rango de la lista
    if 1 <= estado_elegido <= len(estados):
        # Si es válido, obtenemos el la tupla con el estado y la abreviacion de la lista
        estado = estados[estado_elegido - 1]
        '''
        por ejemplo 
        si obtenemos esta tupla("Aguascalientes", "AGU")
        podemos acceder a la abreviatura con el índice 1 '''
        abreviatura = estado[1]
        return abreviatura
    else:
        # Si no está en el rango, mostramos un error.
        print("Estado no válido")
        return elegir_estado() #En lugar de usar un while retornamos la funcion

# Función para pedir la fecha de nacimiento separada por día, mes y año
def pedir_fecha_nacimiento():

    while True:
        dia = validar_numero("Ingresa el día de tu nacimiento: ")
        if dia >= 1 or dia <= 31:
            break ## Se rompe el bucle si el numero esta dentro del rango
        else:
            print("El día debe estar entre 1 y 31")


    while True:
        mes = validar_numero("Ingresa el mes de tu nacimiento: ")

        if mes >= 1 and mes <= 12:
            break  # Se usa la sentencia break para salir del ciclo
        else:
            print("El mes debe estar entre 1 y 12")

    while True:
        año = validar_numero("Ingresa el año de tu nacimiento (aaaa): ")
        if año >= 1900:
            # Si el año es mayor o igual a 1900, continuamos
            break
        else:
            print("El año debe ser 1900 o posterior")

    # Si los valores son válidos, devolvemos la fecha en formato "dd/mm/aaaa"
    # Explicación del formato :02d:
    # :   Indica que lo que sigue es una especificación de formato.
    # 02  Asegura que el valor de dia tendrá al menos dos dígitos, añadiendo un cero si es necesario.
    # d   Representa un número entero (sin decimales).
    return f"{dia:02d}/{mes:02d}/{año}"

# Lista de estados en México (abreviaturas)
# Es una lista de tuplas, donde cada tupla contiene dos elementos
# Las tuplas son estructuras de datos que permiten almacenar varios valores en una sola variable
# Se definen usando paréntesis ()
# Esta es una lista de tuplas por lo tanto se pueden agregar o eliminar elementos completos
# Pero no modificar sus elementos individualmente

estados = [
    ("Aguascalientes", "AG"), ("Baja California", "BC"), ("Baja California Sur", "BC"),
    ("Campeche", "CA"), ("Chiapas", "CH"), ("Chihuahua", "CH"), ("Coahuila", "CO"),
    ("Colima", "CO"), ("Distrito Federal", "DI"), ("Durango", "DU"),
    ("Guanajuato", "GT"), ("Guerrero", "GR"), ("Hidalgo", "HI"), ("Jalisco", "JA"),
    ("Michoacán", "MI"), ("Morelos", "MO"), ("Nayarit", "NA"), ("Nuevo León", "NL"),
    ("Oaxaca", "OA"), ("Puebla", "PU"), ("Querétaro", "QU"), ("Quintana Roo", "RO"),
    ("San Luis Potosí", "SL"), ("Sinaloa", "SI"), ("Sonora", "SO"), ("Tabasco", "TA"),
    ("Tamaulipas", "TA"), ("Tlaxcala", "TL"), ("Veracruz", "VE"), ("Yucatán", "YU"),
    ("Zacatecas", "ZA")
]

def primera_consonante_interna(palabra):
    # Definimos una lista con todas las consonantes en español
    consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
                   "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

    # Recorremos la palabra desde la segunda letra hasta el final.
    for letra in palabra[1:]:
        # Recorremos la lista de consonantes y comparamos con la letra actual.
        for consonante in consonantes:
            if letra.upper() == consonante:  # Si la letra es una consonante
                return consonante  # Retorna la primera consonante encontrada

    # Si no se encuentra ninguna consonante interna, retornamos 'X'.
    return 'X'

def validar_sexo(mensaje):
    while True:
        valor = input(mensaje).strip().upper()

        if len(valor) == 0:
            print("No puede estar vacio el campo")
        elif len(valor) > 1:
            print("Se ingresaron mas de un caracter")
        elif valor  == "H" or valor == "M":
            return valor
        else:
            print("Sexo no válido")

# Función para generar la CURP
def generar_curp(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, estado):
    # Primero, tomamos las primeras dos letras del apellido paterno, la primer del materno, y la primera letra del nombre
    curp = apellidoPaterno[:2].upper() + apellidoMaterno[0].upper() + nombre[0].upper()

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
    curp += estado.upper()  # Solo las dos primeras letras del estado

    # Obtener la primera consonante interna de cada parte
    consonantePaterno = primera_consonante_interna(apellidoPaterno)
    consonanteMaterno = primera_consonante_interna(apellidoMaterno)
    consonanteNombre = primera_consonante_interna(nombre)

    # Añadir las consonantes internas al final de la CURP
    curp += consonantePaterno + consonanteMaterno + consonanteNombre

    # Retornamos la CURP generada
    return curp

# Función principal para pedir los datos y generar la CURP
def pedir_datos_curp():

    # Solicitar datos al usuario utilizando las funciones correspondientes
    nombre = validarCadena("Ingresa tu primer nombre: ")
    apellidoPaterno = validarCadena("Ingresa tu apellido paterno: ")
    apellidoMaterno = validarCadena("Ingresa tu apellido materno: ")
    fechaNacimiento = pedir_fecha_nacimiento()  # Llamamos a la función para pedir la fecha de nacimiento
    sexo = validar_sexo("Ingresa tu sexo (H/M): ")

    # Llamamos a la función para elegir el estado
    estado = elegir_estado()

    # Generar y mostrar la CURP utilizando los datos
    curp = generar_curp(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, estado)
    print(f"\nTu CURP es: {curp}")
    print(f"\nTu CURP encriptada con SHA-256 es: \n{encriptar_sha256(curp)}")

'''
Aqui se usa tupla es una colección ordenada e inmutable de elementos. Una vez creada, no se 
puede modificar. En este caso como los meses nuncan cambian es lo mas conviente usar una 
tupla
'''
meses = ( (1, "Enero"),   (2, "Febrero"),  (3, "Marzo"),  (4, "Abril"),  (5, "Mayo"),
    (6, "Junio"), (7, "Julio"), (8, "Agosto"), (9, "Septiembre"), (10, "Octubre"),
    (11, "Noviembre"), (12, "Diciembre")
)

def obtener_fecha_nacimiento(curp):

    ''' inicio: posición donde empieza la extracción (se incluye)
    fin: posición donde termina la extracción (NO se incluye)
    Empezando desde la posicion cero (0) '''

    # Los caracteres 6 a 8 representan el día
    dia = curp[8:10]
    # Los caracteres 8 a 10 representan el mes
    mes_numero = int(curp[6:8])  # Convertir a entero de una vez
    mes_original=curp[6:8]
    mes = "Mes no valido"

    if int(dia) <= 1 or int(dia) >= 31 :
        dia= "Día no válido"

    if mes_numero >= 1 and mes_numero <= 12:
        for numero,mes_nombre in meses:
            if mes_numero == numero:
                mes = f"{mes_nombre} - {mes_original}"

    # Los caracteres 4 a 6 representan el año
    if int(curp[4:6]) > 30:
         # Si el año es mayor que 30 lo ponemos como 19 (1900-1999)
        anio = "19" + curp[4:6]  # Año del siglo XX
    else:
        # Si el año es mayor que 20 lo ponemos como 19 (2000-2099)
        anio = "20" + curp[4:6]  # Año del siglo XXI

    # Regresamos el día, mes y año como resultado
    return dia, mes, anio

def obtener_sexo(curp):
    #El sexo esta en la posicion 11 del CURP pero como empieza desde 0 se toma la 10
    sexo = curp[10].upper()
    if sexo == 'H':
        return "Masculino"
    elif sexo == 'M':
        return "Femenino"
    else:
        return "Valor no reconocido"

def obtener_lugar_nacimiento(curp):
    estado_abrev = curp[11:13].upper()
    for estado in estados:
        if estado_abrev == estado[1]:
            return estado[0]
    return "Valor no reconocido"

def validar_curp(curp):
    curp = curp.strip()
    # Verificar que la CURP tenga 16 caracteres y cumpla con el formato adecuado
    if len(curp) != 16 or not (
        curp[0:4].isalpha() and  # Primeros 4 caracteres deben ser letras
        curp[4:6].isdigit() and  # Año (2 dígitos numéricos)
        curp[6:8].isdigit() and  # Día (2 dígitos numéricos)
        curp[8:10].isdigit() and  # Mes (2 dígitos numéricos)
        curp[10].isalpha() and  # Sexo (1 letra)
        curp[11:13].isalpha() and  # Estado (2 letras)
        curp[13:16].isalpha()  # Últimos 3 caracteres deben ser letras
    ):
        return False
    return True

def pedir_curp():
        curp = input("Ingresa el CURP: ").strip()
        # La funcion validar_curp regresa un true si tiene el formato indicado y un false si no
        if not validar_curp(curp):
            print("\nLa CURP no cumple con el formato o tiene una longitud incorrecta")
        else:
            # Si el CURP tiene el formato adecuado se extrae la informacion
            # En cada funcion, se retorna valor no valido si la informacion esta mal
            dia, mes, anio = obtener_fecha_nacimiento(curp)
            sexo = obtener_sexo(curp)
            lugar_nacimiento = obtener_lugar_nacimiento(curp)

            # Mostrar resultados
            print(f"\nDía: {dia}")
            print(f"Mes: {mes}")
            print(f"Año: {anio}")
            print(f"Sexo: {sexo}")
            print(f"Lugar de nacimiento: {lugar_nacimiento}")

def encriptar_sha256(texto):
    # Crear un objeto hash con SHA-256
    sha256 = hashlib.sha256()

    # Actualizamos el objeto con el texto, primero necesitamos convertirlo a bytes
    sha256.update(texto.encode('utf-8'))

    # Obtener el valor hash en formato hexadecimal
    hash_encriptado = sha256.hexdigest()

    return hash_encriptado

def menu():
    while True:
        print("\nEscoge una del las siguientes opciones: "
          "\na. Generar CURP "
          "\nb. Ingresar CURP"
          "\nc. salir\n")

        valor = input("Ingresa una de las opciones: ").strip().lower()
        if len(valor) == 0:
            print("\nNo puede estar vacio el campo")
        elif len(valor) > 1:
            print("\nSe ingresaron mas de un caracter")
        elif valor == "a":
            print("\n Se escogio la opcion a\n")
            pedir_datos_curp()
        elif valor == "b":
            print("\n Se escogio la opcion b\n")
            pedir_curp()
        elif valor == "c":
            print("\nFinalizando programa\n")
            break
        else:
            print("\nOpcion no valida")

def main ():
    menu()

# Ejecutar la función main para correr el programa
main()






