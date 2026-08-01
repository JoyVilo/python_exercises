import requests

ciudad = input("¿De qué ciudad quieres saber el clima?")

url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1"
respuesta_geo = requests.get(url_geo)
datos_geo = respuesta_geo.json()

latitud = datos_geo["results"][0]["latitude"]
longitud = datos_geo["results"][0]["longitude"]

url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
respuesta_clima = requests.get(url_clima)
datos_clima = respuesta_clima.json()

clima = datos_clima["current_weather"]
print(f"ciudad: {ciudad}")
print(f"temperatura: {clima['temperature']} °C")
print(f"viento: {clima['windspeed']} km/H")

