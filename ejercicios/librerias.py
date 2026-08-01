import random

numero_secreto = random.randint(1, 10) #random integer o sea numero entero aleatorio

intentos = 0

while True:
    intento = int(input("Adivina el número de 1 al 10:  "))
    intentos += 1

    if intento == numero_secreto: 
        print(f"adivinaste en {intentos} intentos")
        break
    elif intentos == 3:
        print(f"perdiste, el numero era {numero_secreto}")
    elif intento < numero_secreto:
        print("Muy bajo")
    else:
        print("muy alto")