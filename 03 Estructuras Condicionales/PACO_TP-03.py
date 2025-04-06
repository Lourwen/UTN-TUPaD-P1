#1)	Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad=int(input("Ingrese su edad "))
print("su edad es:", edad)
if edad>18:
    print("Es mayor de edad")
else:
    print("Usted no es mayor de edad ")   
#2)	Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario 
#deberá mostrar el mensaje “Desaprobado”.     
nota=int(input("Ingrese su nota "))
if nota>=6:
    print("Aprobado")
else:
    print("desaprobado")
#3)	Escribir un programa que permita ingresar solo números pares.Si el usuario ingresa un
# número par, imprimir en pantalla el mensaje "Ha ingresado un número par";    
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".Usar módulo (%)     
numero=int(input("Ingrese un numero "))   
if numero==0:
    print("ingrese un numero mayor a cero")
elif numero%2==0:
    print("el numero ingresado,",numero, "es par")    
else:
    print("el numero ingresado,",numero,"es impar")   
#4)Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#●	Niño/a: menor de 12 años.
#●	Adolescente: mayor o igual que 12 años y menor que 18 años.
#●	Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#●	Adulto/a: mayor o igual que 30 años.
edad=int(input("Ingrese su edad "))
if edad<12:
    print("Niño/a")
elif edad>=12 and edad <18:
    print("Adolescente")
elif edad>=18 and edad<30:
    print("Adulto/a joven")
else:
    print("Adulto/a")   
#5)	Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
#Si el usuario ingresa una contraseña de longitud adecuada, imprimir en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
contraseña=input("Ingrese una contraseña entre 8 y 14 caracteres ")
if len(contraseña)>=8 and len(contraseña)<=14:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

#6)Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media, 
#compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista
# numeros_aleatorios de la siguiente forma:el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria

from statistics import mode, median, mean  # Importacion las funciones
import random  # Importarcion de módulo random para generar números aleatorios

# lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda:{moda}")         #el valor que más veces se repite
print(f"Mediana: {mediana}")  #el valor hubicado en el medio de la lista
print(f"Media:{media}")       #el promedio de la lista

# Determinacion del sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")    
#7)Escribir un programa que solicite una frase o palabra al usuario.
#  Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase=input("Ingrese una frase o palabra: ")

if frase[-1] in 'aeiou':  
    print(f"{frase} !")  
else:
    print(frase)

#8)	Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1.	Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2.	Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3.	Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla 
#Usar: upper(), lower() y title()    
nombre=input("Ingrese su nombre: ")
num=int(input("seleccione una opción del 1 al 3 para el tipo de impresión: "))
if num== 1:
    salida=nombre.upper()
    print(salida)
elif num==2 :
    salida=nombre.lower()
    print(salida)
else:
    salida=nombre.title()
    print(salida)   
     
#9)	Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#●	Menor que 3: "Muy leve" (imperceptible).
#●	Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#●	Mayor o igual que 4	y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#●	Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#●	Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#●	Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
escala=int(input("Ingrese un numero de escala de Richter: "))
if escala<3:
    print("Muy leve (imperceptible)")
elif escala>=3 and escala<4 :
    print("Leve (ligeramente perceptible)")    
elif escala>=4 and escala <5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif escala >=5 and escala <6:
    print("Fuerte (puede causar daños en estructuras débiles)")    
elif escala >=6 and escala <7:
    print("Muy Fuerte(puede causar daños significativos)")    
else:
    print("Extremo(puede causar graves daños a gran escala)")  

#10)
#Periodo del año	                                                  HN              HS
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)  	    Invierno	    Verano
#Desde el 21 de marzo hasta el 20 de junio (incluidos)	            Primavera	    Otoño
#Desde el 21 de junio hasta el 20 de septiembre (incluidos)	        Verano	        Invierno
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)	    Otoño	        Primavera

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
#qué mes del año es y qué día es. Imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio =input("Ingrese en que hemisferio se encuentra, sur o norte: ")
mes=int(input("Ingrese el numero (1 al 12) mes de la fecha: "))
dia=int(input("Ingrese el dia de la fecha: "))
if (dia>=21 and mes == 12) or (1<=mes<=2) or (dia <21 and mes==3):
    if hemisferio=="sur":
        print("verano")
    else:
        print("Invierno")
elif (dia >=21 and mes ==3) or((4<=mes<=5)) or (dia <21 and mes==6):
    if hemisferio=="sur":
        print("otoño")
    else:
        print("primavera")
elif (dia >=21 and mes==6) or (5<=mes<=8)or (dia<21 and mes ==9):
    if hemisferio=="sur":
        print("invierno")
    else:
        print("verano")         
else:
    if hemisferio=="sur":
        print("primavera")
    else:
        print("otoño")  