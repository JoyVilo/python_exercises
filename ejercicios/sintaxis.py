#Pedir nombre
#Nombre = input ("¿Cómo te llamas?")
#print("Holi,", Nombre, "<3")
"""
#mostrar numeros pares de 1 al 20 
for i in range(1,21) :
    if i % 2 == 0:
        print(i)

#pide un número y muestra su tabla de multiplicar del 1 al 10
numero = int(input("Dame un número"))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

#Pide un número y di si es positivo o negativo
numero = int(input("Escribe un número"))
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else: 
    print("Es cero")

#pide un número y di si es par o impar
numero = int(input("escribe un numero: "))
if numero % 2 == 0:
    print("es par")
else:
    print("es impar")

#cuenta cuantos números del 1 al 100 son divisibles por 3
contador = 0
for i in range(1,101):
    if i % 3 == 0: 
        contador = contador + 1

print("cantidad de numeros divisibles por 3:", contador) 


#Crea una lisra con 5 frutas

frutas = [ "Manzana" , "Pera" , "Uva" , "Guanabana"]
print(frutas)
print(frutas[0])
print(frutas[-1]) #da el ultimo sin importar el tamaño

frutas.append("Uchuba") #las variables van en minuscula
print (len(frutas)) #imprime los elementos que hay o sea los cuenta


notas = [85, 92, 78, 95, 60]

for nota in notas: #nota es cada elemento 
    print(nota)

print (len(notas))

notas.append(43)
print(notas[1])
print(notas[-1])


notas =[]
for i in range(5):
    nota = float(input("escribe una nota: "))
    notas.append(nota)

for nota in notas:
        print(nota)

print("total de notas: ", len(notas))

if notas[0] > notas[-1]:
    print("la primera nota es mayor")
elif notas[0] < notas[-1]:
    print("la ultima nota es mayor")
else:
    print("son iguales") 



#Haz lo mismo pero con 3 notas en vez de 5 y muestra solo las notas mayores a 70.

notas =[]
for i in range(3):
    nota = int(input("Agrega la nota: "))
    notas.append(nota)

for nota in notas: #entender bien esta parte. 
    print(nota)

print("total de notas: ", len(notas)) #cuenta cuántos elementos tiene la lista

for nota in notas: #Para cada variable dentro de la lista, haz x cosa
    if nota > 70:
        print(nota, "Pasaste el semestre")



#crear un diccionario

notas = {
    "Isabella": 96,
    "Carlos": 40,
    "Marga": 96
}
print(notas)

alumno = input("Añade otro alumno: ")  #en diccionarios no se agrega append porque necesita clave y valor
nota = int(input("añade la nota: "))
notas[alumno] = nota 

for alumno, nota in notas.items(): #items devuelve cada par clave y valor del diccionario
    print(alumno, ":", nota) #alumno recibe la clave y nota recibe el valor

print(notas["Marga"])


#funciones: son bloques de código que se puede reutilizar cuantas veces quieras sin repetirlo

def saludar(nombre): # def: definir(indicas que vas a crear una función) nombre: parámetro(valor que le pasas a la función)
    print("hola", nombre) #el cuerpo de la función

saludar("isabella") #llamar la función : usarla cuando se necesite

#crear una función llamada presentar que reciba nombre y edad

def presentar(nombre, edad): 
    print(f"hola, me llamo {nombre} y tengo {edad} años") #todo lo que va dentro de {} se convierte automaticamente a texto.

presentar("Isabella", 20)
presentar("Marga", 19)
presentar("Joy", 21)


def evaluar_nota(nombre, nota): 
    if nota > 70:
        print(f"El alumno {nombre} aprobó con {nota}")
    else: 
        print(f"el alumno {nombre} reprobó con {nota}")

evaluar_nota("Isabella", 90) #como en la función los dos valores son 1. nombre y 2. nota,
evaluar_nota("carlos", 54)  #al momento de llamarlos se detecta cuál es nombre y cúal tiene el valor de nota

#ciclos: while = Repite hasta que algo cambie
# for = Repite un número fijo de veces. 

#Una licuadora gira por 4 segundos exactos
for segundo in range(4):
    print("licuando...")

#gira hasta que todo esté triturado
triturado = False #el valor booleano siempre empieza en mayuscula (triturado vale falso)
while triturado == False: #== significa comparar si dos cosas son iguales (triturado es falso)
    print("licuando...")
    triturado = True #Cuando ya está listo, para.

#se puede simplificar asi:

while not triturado: 
    print("licuando...")
    triturado = True

#ejercicio

contador = 0 #empieza en 0 porque aún no he contado nada
numero = int(input("Escribe un número (0 oara salir): "))

while numero != 0: #todo lo que está dentro del while se repite
    print(numero)
    contador += 1
    numero = int(input("escribe un numero (0 para salir): "))


#print(f"ingresaste {contador} numeros")

#ejercicio 2

contraseña = input("Escribe la contraseña: ")

while contraseña != "python123":
    print("¡Acceso denegado!")
    contraseña = input("Escribe la contraseña: ")

print("¡Acceso concedido!")



#Manejo de errores. 

try: 
    number = int(input("Escribe un número: "))
except:
    print("No es un numero")

#ejercicio

#if/else son condiciones predecibles y controladas
#try/except son situaciones impredecibles y externas

while True: #Significa que no cambia entonces se repite para siempre
    try:
        numero = int(input("Escribe un número"))
        print(f"el doble es: {numero * 2}")
        break #
    except: 
        print("esto no es un número, intenta de nuevo")

#ejercicio  1 

while True:
    try: 
        numero = int(input("escribe un número"))
        print(f"la mitad de ese número es {numero / 2}")
        break
    except:  
        print("Eso no es un número")

#ejercicio 2

while True: 
    try:
        numero1 = int(input("Escribe un número: "))
        numero2 = int(input("Escribe otro número: "))
        print(f"{numero1} / {numero2} = {numero1 / numero2}") #es para mostrar el orgen de la operación
        break
    except ValueError: #errores predefinidos en python
        print("Eso no es un número")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

#ejercicio 3
while True: 
    try:
        numero1 = int(input("Añade un número:  "))
        numero2 = int(input("Añade otro número: "))
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
        break
    except ValueError:
        print("Eso no es un npumero")
    except ZeroDivisionError: 
        print("No se puede dividir entre 0")

#ejercicio 4

alumno = input("Añade un nombre:  ")
nota = (input("Agrega una nota: "))

archivo = open("alumnos.txt", "a")
archivo.write(f"{alumno}: {nota}\n")
archivo.close()

archivo = open("alumnos.txt", "r")
print(archivo.read())
archivo.close()
"""


#ejercicio 5

while True:
    opcion = input("¿Qué quieres hacer? (1/2/3)")
    if opcion == "1":
        entrada = input("¿Qué quieres escribir?  ")
        archivo = open("diary.txt", "a")
        archivo.write(f"{entrada}\n")
        archivo.close()

    elif opcion == "2":
        archivo = open("diary.txt", "r")
        print(archivo.read())
        archivo.close()

    elif opcion == "3":
        print("Chao")
        break