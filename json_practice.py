import json
#libreria de json (javascript object notation)

#creacion del perfil, diccionario con información
perfil = {
    "nombre": "Joy",
    "habilidades": ["Python", "Cloud", "Git"],
    "experiencia": "Junior", 
}
#guardar el diccionario anterior como archivo
with open("perfil.json", "w") as archivo: #w es guardar
    json.dump(perfil, archivo) #dump es guardar en archivo json

with open("perfil.json", "r") as archivo: #r es leer 
    datos = json.load(archivo) #load es leer el archivo
    print(datos["nombre"]) # se imprime el nombre y las habilidades
    print(datos["habilidades"])