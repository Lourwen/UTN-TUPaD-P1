#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
num = 0
for cant in range(1,11): #Para que incluya el 100 le agrego uno al valor final
    num += 1
    print(cant)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
num = int(input("Ingrese un numero entero: ")) #El ingreso por defecto son caracteres, por eso lo convertimos en numero con int
if num <0:
    digitos = len(str(num)) - 1  # Restamos 1 por el signo negativo
else:    
    digitos = len(str(num)) #len cuenta la cantidad de caracteres 

print(f"La cantidad de digitos que contiene {num} es de : {digitos}")   
 
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1= int(input("Ingrese un numero entero: "))
num2= int(input("Ingrese un otro numero entero: "))
#validamos para que num1 sea el menor
if num1 < num2:
    inic = num1 + 1 #para excluye el valor inicial
    fin = num2 #por defecto  se ecpluye el valor final
else:
    inic = num2 + 1 #si num2 es el menor lo declaro como inic
    fin = num1

suma = 0
for i in range(inic, fin):
    suma += i

print(f"La suma de los números entre {num1} y {num2}, excluyendolos, es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un cero.
CORTE = 0
num = None #Inicializamos num como None para que entre en el while la primera vez.
suma = 0

while num != CORTE:
    num = int(input("Ingrese un número entero (0 para cortar): "))
    if num != CORTE:      #Si el número es distinto a 0, lo sumamos a la variable suma.
        suma += num

print(f"La suma total es: {suma}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random #importamos la funcion random de las herramientas que no estan por defento 

numero_a_adivinar = random.randint(0, 9) # random.randint genera un numeros aleatoreo entre 0 y 9
intentos = 0
adivinado = False   # la variable "adivinado" la usaremos para corte el ciclo cuando su valor sea verdadero. 

print("Adivina el número entre 0 y 9")

while adivinado == False: # Mientras adivinado no sea True, que sea falso, sigue ejecutando el bloque de código dentro del bucle
    intento = int(input("Ingresá números para divinar: ")) # Se solicita al usuario que ingrese los intentos
    intentos += 1

    if intento == numero_a_adivinar: # Sí el numero ingresado como intento es igual al numero generado aleatoreamente...
        print("Diste con el número en", intentos, "intento/s")
        adivinado = True  #...valor de adivinado será verdadero y el ciclo se corta.
    else:
        print("Intenta de nuevo.") #Si el intento no es igual al número a adivinar , el ciclo continua.


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for num in range(100, -1, -2): #-1 es porque el valor final no incliye a este valor y quiero que imprima 0.  
    print(num)                 # El-2 es para la cuenta regresiva en numero par


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero positivo: "))

if num >0: #validacion para que la entrada permita solo numeros positivos mayores a cero
    suma = 0
    for i in range(1,num + 1): # para que el numero ingresado por el usuario se incluya en la suma, le sumamos 1 (num+1)
        suma = suma + i # En la variable suma vamos guardando cada valor por cada iteracion sumandolo.
    print (f"La suma de de todos los numeros comprendidos entre 0 y {num} es igual a {suma}")
else:
    print("ingrese un numero entero positivo mayor a cero")        

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. 


cantidad_de_numeros = 100
positivos=0
negativos=0
pares = 0
impares= 0
for i in range(1,cantidad_de_numeros + 1):
    num= int(input("Ingrese un un numero entero: "))
    if num <=0:
        negativos = negativos + 1
    else:
        positivos = positivos + 1    
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(f"cantidad de positivos es: {positivos} ; negativos: {negativos}; pares :{pares}; impares:{impares}")      


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.  
cantidad_de_numeros = 5
suma = 0
media = 0
for i in range(1,cantidad_de_numeros + 1):  # Para el ciclo sean 100 veces le sumo 1
    num = int(input("Ingrese un numero entero : "))
    while num < 0: #validacion de numeros positivos: en caso de un num negativo, el programa pedira nuevamente un entero al usuario
        print("Numero no válido. Ingrese un numero entero positivo.")
        num = int(input("Ingrese nuevamente un numero: "))
    
    suma += num

media = suma / cantidad_de_numeros
print(f"La media de los números ingresados es: {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero entero positivo: "))
numero_invertido = 0
if num <=0:
    print("Intentelo de nuevo usando numeros enteros positivos")
else:
    while num > 0:    #Mientras que le valor ingresado sea mayor a 0, lo usamos para cortar el bucle cuando termine de invertir los digitos.
        digito = num % 10                # Se divide el num en 10 y tomamos el sobrante de la division,"el resto", para tomar el ultimo digito
        numero_invertido = numero_invertido * 10 + digito  # "0*10 + digito" va colocando los numeros de manera inversa, del primer resto obtenido al ultimo. 
        num = num // 10               # Utilizamos la division entera para eliminar el último digito y terminar el bucle cuando de cero

    print(f"El numero invertido es: {numero_invertido}")


           
