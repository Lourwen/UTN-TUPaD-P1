# 1.Dado el diccionario precios_frutas:precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#  Añadir las siguientes frutas con sus respectivos precios: Naranja = 1200, Manzana = 1500, Pera = 2300
  
precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}

# Agregamos frutas
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"] =1500
precios_frutas["Pera"]= 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#  actualizar los precios de las siguientes frutas:Banana = 1330,Manzana = 1700, Melón = 2800

precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}

# Agregamos frutas
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"] =1500
precios_frutas["Pera"]= 2300

# Actualizacion de  precios
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"] =1700
precios_frutas["Melon"]= 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#  crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}

# Agregamos frutas
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"] =1500
precios_frutas["Pera"]= 2300

# Actualizacion de  precios
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"] =1700
precios_frutas["Melon"]= 2800

#listamos frutas a partir de claves del diccionario
frutas = [fruta for fruta in precios_frutas]
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

# Diccionario para guardar los contactos telefonicos
contactos = {}

# Cargar 5 contactos
print("Ingrese 5 contactos para guardarlos en una lista")
for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    numero = input(f"Ingrese el número de tel. de {nombre}: ")
    contactos[nombre] = numero

# solicitar el contacto que desea consultar
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

# validacion de coincidencia con la lista de contactos
if consulta in contactos:
    print(f"El numero de {consulta} es: {contactos[consulta]}")
else:
    print("Contacto inex")

#5) Solicita al usuario una frase e imprime: Las palabras únicas (usando un set).
#  Un diccionario con la cantidad de veces que aparece cada palabra.

# solicitamos una frase 
frase = input("Ingrese una frase: ")

# Separar en palabras
palabras = frase.split()

# para obtener palabras no repetidas usamos set
palabras_unicas = set(palabras)
print("Palabras unicas:")
print(palabras_unicas)

# Contar cantidad de veces que aparece en el diccionario
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("n° de repeticiones de cada palabra:")
print(recuento) 

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#  Luego, mostrá el promedio de cada alumno.

# Diccionario para guardar alumnos y notas
alumnos = {}

# Ingresamos informacion de 3 alumnos
for i in range(3):
    nombre = input("Nombre del alumno: ")
    
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))

    # Guardamos las notas en una tupla
    notas = (nota1, nota2, nota3)

    # Guardamos en el diccionario
    alumnos[nombre] = notas

# Promedio por alumno
print("Promedios por alumno:")
for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f" El alumon {nombre} tiene un promedio de {promedio} ")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Estudiantes que aprobaron los dos
parcial1 = {"33453101", "34897654", "37000922", "36001001"}
parcial2 = {"33453101", "36456981", "35927355", "37550244"}

# Estudiantes que aprobaron ambos parciales
ambos_parciales = parcial1 & parcial2
print("aprobaron ambos parciales:", ambos_parciales)

# Estudiantes que aprobaron solo uno 
solo_uno = parcial1 ^ parcial2
print("aprobaron solo uno de los dos parciales:", solo_uno)

# Estudiantes que aprobaron al menos uno
al_menos_uno = parcial1 | parcial2
print("aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

# Diccionario con productos y su stock (ejemplo stock de arboles)
stock_productos = {
    "prunus": 10,
    "bauhinias": 5,
    "jacarandas": 8
}

# Imprimir productos disponibles
print("Productos disponibles:")
for producto in stock_productos:
    print("*", producto)

# Consultar el stock de un producto ingresado
producto = input("Ingrese el nombre del producto para ver su stock: ")

# validacion de disponibilidad
if producto in stock_productos:
    print("Stock actual de", producto, "=", stock_productos[producto])
    
    # Preguntar si quiere agregar unidades
    agregar = input("¿Desea incorporar unidades al stock? elija si/no: ")
    if agregar == "si":
        cantidad = int(input("¿Cuanto desea agregar?: "))
        stock_productos[producto] += cantidad
        print("Actualizacion de stock de", producto, "=", stock_productos[producto])
else:
    # En caso que el producto no este, se agrega nuevo
    print("No se halla producto en la lista.")
    nuevo = input("¿Desea agregarlo? elija si/no: ")
    if nuevo == "si":
        cantidad = int(input("¿Cual es el stock del producto agregado?: "))
        stock_productos[producto] = cantidad
        print("El producto agregado", producto, " tiene ", cantidad, "unidades.")

# Imprimimos el estado final del diccionario
print("Actualizacion del stock:")
for producto, stock in stock_productos.items():
    print(producto + "=", stock)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 

# Creacion de agenda
agenda = {
    ("lunes", "08:30"): "plantaciones en plaza",
    ("martes", "10:30"): "fumigacion de jacarandas",
    ("miércoles", "12:30"): "reunion con equipo",
    ("jueves", "16:00"): "firma de documentos",
    ("viernes", "08:00"): "poda lineal"}


# Solicitar día y hora
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (ejemplo 09:00): ")

# Buscar la actividad
clave = (dia, hora)

if clave in agenda:
    print(f"Evento agendado: {agenda[clave]}")
else:
    print("Sin actividades")    


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.
paises_a_capitales = {
    "Corea": "Seul",
    "Brasil": "Brasilia",
    "Tailandia": "Bangkok",
    "India": "Nueva Dehli",
    "Japón": "Tokio"
}

capitales_a_paises = {}

for pais in paises_a_capitales:
    capital = paises_a_capitales[pais]
    capitales_a_paises[capital] = pais

# imprimir nuevo diccionario
print(capitales_a_paises)    