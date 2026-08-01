import requests
#lubreria externa que permite conectarse a internet

respuesta = requests.get("https://api.github.com/users/JoyVilo")
#hace una petición GET a una URL
#GET significa "dame información de esta url"
#la URL apunta a mi perfil de github
#la respuesta se guarda en la variable "respuesta"

print(respuesta.status_code) 
#status_code es el código de respuesta del servidor

#convierte la respuesta en un formato legible (json)
datos = respuesta.json()
print(datos["login"])
print(datos["name"])
print(datos["public_repos"])
print(datos["followers"])

