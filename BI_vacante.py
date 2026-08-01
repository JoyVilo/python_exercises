from time import strftime

import requests
import json
from datetime import datetime

url = "https://remotive.com/api/remote-jobs?search=business+intelligence&limit=200"
respuesta = requests.get(url)
datos = respuesta.json()

niveles_ok = ["junior", "mid", "analyst", "associate", "lead"]
niveles_no =["senior", "manager","director", "head"]

vacantes_bi = []

for trabajo in datos["jobs"]:
    titulo = trabajo["title"].lower()

    if any(nivel in titulo for nivel in niveles_no):
        continue #que se salte la vacante que no cumpla con lo que pido

    vacantes_bi.append( {
        "titulo": trabajo["title"],
        "empresa": trabajo["company_name"],
        "url": trabajo["url"],
        "fecha_busqueda": datetime.now().strftime("%d/%m/%y")
            })

with open("vacantes_bi.json", "w") as archivo: 
    json.dump(vacantes_bi, archivo, indent=4)

print(f"vacantes encontradas: {len(vacantes_bi)}")
for vacante in vacantes_bi:
    print(f"{vacante['titulo']} - {vacante['empresa']}")