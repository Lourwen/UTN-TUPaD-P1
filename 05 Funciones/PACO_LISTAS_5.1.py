#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_4 = list(range(4, 101, 4))#El rango comienza en 4 porque pide que sean multiplos de 4. 100 + 1 para que incluya al 100.
print(multiplos_4)                  # El último 4 es para que el salto sea de 4 hasta llegar a 100.

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

especies_en_japones= ['桜','大銀杏','桃の木','杉','さざんか']
penultimo = especies_en_japones[-2]
print(f" el penultimo elemento de {especies_en_japones} es: {penultimo}")

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#  Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(0)
lista_vacia.append(7)
print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
#  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar
#  cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]
animales = ['perro','gato','conejo','pez']
animales[1]="loro" #actualizo el segundo valor de la lista
print(animales)
animales[-1] = "oso" #actualizo el ultimo valor de la lista
print(animales)  # lista resultante de ambas actualizaciones

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8,15,3,22,7]
numeros.remove(max(numeros)) #"max", busca el maximo vamor de una lista de numeros y "remove" lo extrae de la lista.
print(numeros)               # Se imprimira la lista de numeros resultante, la lista sin el max valor extraido.

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

lista_con_saltos =list(range(10,35,5))
print(lista_con_saltos)

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
#autos = ["sedan", "polo", "suran", "gol"]

autos = ['sedan', 'polo', 'suran', 'gol']
autos[1:3] =["fitito", "chata"]  #actualizo el elemento 1 y el 2, por eso uso 3 ya que no incluye el valor final
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []                  #lista vacia
dobles.append(5 * 2)         #append agregara el valor resultante solicitado
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)               #[10,20,30]

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#                   compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#   a) Agregar "jugo" a la lista del tercer cliente usando append.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
print(compras)
#   b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
print(compras)
#   c) Eliminar "pan" de la lista del primer cliente.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
#   d) Imprimir la lista resultante por pantalla
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15,True,[25.5, 57.9 ,30.6],False]
print(lista_anidada)