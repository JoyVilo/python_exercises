import os #libreria agregada

carpetas = ["documents", "images","cloud"] #creación de lista con las 3 carpetas

#cracion de carpetas

#para saber si las carpetas ya existen antes de crearla
for carpeta in carpetas:
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
        print("Carpetas creadas exitosamente")
    else:
        print("Ya existen")

#mostrar todas las carpetas del directorio actual
contenido = os.listdir(".")
for elemento in contenido: 
    print(elemento)
