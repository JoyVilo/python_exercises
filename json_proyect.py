import requests
import json
#se agregan librerias

#se agrega la api para la consulta de vacantes
url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=100"
respuesta = requests.get(url)
datos = respuesta.json() #se pide la respuesta obtenida por la url en formato json

#se crea una lista con el nombre de vacantes python que es lo que nos interesa
vacantes_engineer = []

#se hace que recorra los datos, que filtre por el nombre de python
#que nos muestre el titulo del trabajo, la empresa y el link del lugar
for trabajo in datos["jobs"]:
    if "Engineer" in trabajo["title"] or "engineer" in trabajo["title"].lower(): #aqui se añade dos probabilidades de vacantes al ser escritas en m o M
        vacantes_engineer.append( {
            "titulo": trabajo["title"],
            "empresa": trabajo["company_name"],
            "url": trabajo["url"]
        })

#se guarda en un archivo json
with open("vacantes.json", "w") as archivo:
    json.dump(vacantes_engineer, archivo, indent=4)

# se pide que se muestren los resultados
print(f"vacantes encontradas: {len(vacantes_engineer)}") #len cuenta cuantas vacantes se encontraron
for vacante in vacantes_engineer: #recorre las vacantes en los filtros
    print(f" {vacante['titulo']} - {vacante['empresa']}") #nos muestra el titulo de la vacante y la empresa