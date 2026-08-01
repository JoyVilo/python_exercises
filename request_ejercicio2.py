import requests
#libreria

#se pregunta la ciudad 
ciudad = input("¿De qué ciudad quieres saber el clima?")

#se agregan las apis de la ciudad
url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1"
respuesta_geo = requests.get(url_geo) #se extrae la respuesta de la api
datos_geo = respuesta_geo.json() #se muestra la respuesta de la api en un json

#se extrae la info de la api y se muestran estos dos valores
latitud = datos_geo["results"][0]["latitude"] #[0] significa el primer resultado de cada busqueda
longitud = datos_geo["results"][0]["longitude"]

#se agrega api del clima
url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
respuesta_clima = requests.get(url_clima) #se pide a la api el clima
datos_clima = respuesta_clima.json() #respuesta en json

#se muestra en lista la informacion de ciudad, temperatura y viento
clima = datos_clima["current_weather"]
print(f"ciudad: {ciudad}")
print(f"temperatura: {clima['temperature']} °C")
print(f"viento: {clima['windspeed']} km/H")

