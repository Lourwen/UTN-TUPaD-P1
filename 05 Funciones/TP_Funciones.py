# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()  
# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:“Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#Definicion de funciones
def saludar_usuario(nombre):
    print(f" Hola {nombre}!")
#programa principal
nombre = input("ingrese su nombre para ser saludado: ")
saludar_usuario(nombre)  

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")
#programa principal
nom = input("ingrese su nombre: ")
apel = input("ingrese su apellido: ")
ed = input("ingrese su edad: ")
resi = input("ingrese su residencia: ")
informacion_personal(nom,apel,ed,resi)  
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
#  Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Definicion de funciones
def calcular_area_circulo(a):
    return 3.14 * (a**2)
    
def calcular_perimetro_circulo(a):
    return 2 * 3.14 * a
    
#programa principal
radio = float(input("ingrese un radio: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)  
print(f"El area de un circulo con radio {radio} es igual a {area}")
print(f"El perimetro de un circulo con radio {radio} es igual a {perimetro}")   

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos 
# como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definicion de funciones
def segundos_a_horas(a):    
    return a/3600     #en 1h hay 3600 s
    
#programa principal
segundos = float(input("ingrese los segundos que quiera convertir en horas : "))
horas = segundos_a_horas(segundos)
 
print(f"Los {segundos} segundos equivalen a {horas} hs")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro
#  y imprima la tabla de multiplicar de ese número del 1 al 10.
#  Pedir al usuario el número y llamar a la función.

# Definicion de funciones
def tabla_de_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
#programa principal
numero = int(input("ingrese un numero entero: "))

print (f"Tabla de multiplicar de { numero} :")
tabla_de_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Definicion de funciones
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division ="Indefinido, No se puede dividir por 0!, pruebe otro numero para un resultado"
    else:
        division = a/b
    return(suma, resta, multiplicacion, division)    #tupla donde los indices seran el resultado de cada operacion

# programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

resultado = operaciones_basicas(num1, num2)
print(f"El resultado de sumar {num1} y {num2} es {resultado [0] }")
print(f"El resultado de restar {num1} y {num2} es {resultado [1] }")
print(f"El resultado de multiplicar {num1} y {num2} es {resultado [2] }")
print(f"El resultado de la division {num1} y {num2} es {resultado [3] }")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

# Definicion de funciones
def calcular_imc(peso,altura):
    return peso/(altura**2)    

# programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

imc = calcular_imc(peso, altura)

print(f"Su IMC ,segun su peso y altura es de {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius
# y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definicion de funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32   

# programa principal
grados = float(input("Ingrese los grados celsius: "))

fahrenheit = celsius_a_fahrenheit(grados)

print(f"Los {grados} grados celsius en grados fahrenheit es de {fahrenheit}")  
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros
#  y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definicion de funciones
def calcular_promedio(a, b, c):
    return (a + b + c )/3

# programa principal
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))


promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los numeros {num1}, {num2} y {num3} es de {promedio}")

  