import os #os significa sistema operativo
#le aviso a python que voy a usar mis herramientas

print(os.getcwd()) #get current working directory, acá pregunto en qué carpeta estoy

if not os.path.exists("ejercicios"): #pregunta si existe la carpeta en la computadora
    os.mkdir("ejercicios") # make directory es crear carpeta, crea la carpeta automatica
    print("Carpeta creada")
else:
    print("Ya existe")

archivos = os.listdir(".") #list directory(listar carpeta) el . significa la carpeta en la que estoy trabajando
for archivo in archivos: #recorre la lista de archivos
    print(archivo)



