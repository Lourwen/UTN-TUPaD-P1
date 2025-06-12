# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función
#  para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 
# y el número que indique el usuario

# Solicitar número al usuario
num = int(input("Ingrese un numero para calcular sus factoriales desde 1 hasta ese numero: "))

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Programa principal
if num < 1:
    print("Ingrese un numero mayor o igual a 1")
else:
    for i in range(1, num + 1):
        print(f"Factorial de {i} es {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
#  Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# deficio de la funcion

def fibonacci_recursivo(posicion):
    if posicion==0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion -1) + fibonacci_recursivo(posicion-2)
# Solicitar número al usuario
posicion = int(input("Ingrese un numero para calcular el valor de la s.fibbonacci: "))  
print("Serie de Fibonacci hasta la posición", posicion, ":")
for i in range(posicion + 1):
    print(f" En la posicion {i} obtenemos el valor de fibonacchi :{fibonacci_recursivo(i)}") 

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
#  utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general

# Función recursiva para la potencia
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1  # todo valor elevado a 0 es 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Algoritmo general que solicita datos al usuario
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia_recursiva(base, exponente)
print(f"{base} elevado a {exponente} es igual a {resultado}")
     
#4)Crear una función recursiva en Python que reciba un número entero positivo en base decimal
#  y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

# Solicitar al usuario
numero = int(input("Ingrese un numero entero positivo: "))

if numero < 0:
    print("Ingrese un numero positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El numero {numero} en binario es: {binario}")     

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
#  y devuelva True si es un palíndromo o False si no lo es. La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primera y última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva extrayendo los extremos de la palabra(se saca [0] y [:-1] la ultima posicion de la palabra)
    return es_palindromo(palabra[1:-1])

# Solicitar palabra la usuario
palabra = input("Ingrese una palabra sin espacios ni tildes: ")
resultado = es_palindromo(palabra)
print(f"La palabra ingresada es palíndromo: {resultado}")    

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo
#  y devuelva la suma de todos sus dígitos. No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.


def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)
n= int(input("Ingrese un numero entero y positivo: "))

print(suma_digitos(n))

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.


def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

n_bloques= int(input("Ingrese el n de bloques en el viel más bajo: "))
bloques_totales=contar_bloques(n_bloques)
print(f"Se necesitan un total de {bloques_totales} bloques")



#8) Escribí una función recursiva llamada contar_digito(numero, digito)
#  que reciba un número entero positivo (numero) y un dígito (entre 0 y 9),
# y devuelva cuántas veces aparece ese dígito dentro del número.

numero= int(input("Ingrese un numero: "))
digito=int(input("ingrese un digito: "))
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ult = numero % 10
        resto = numero // 10
        if ult == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return contar_digito(resto, digito)
        
print(f" en {numero} el digito {digito } se repite {contar_digito(numero, digito)} veces")