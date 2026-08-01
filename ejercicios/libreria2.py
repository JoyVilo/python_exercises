from datetime import datetime

ahora = datetime.now()
print(f"Hoy es: {ahora.strftime('%d/%m/%y')}")
print(f"son las: {ahora.strftime('%H:%M')}")

nombre = input("¿Cómo te llamas?")

hora = ahora.hour

if hora < 12:
    print(f"Buenos días {nombre}")
elif hora < 18:
    print(f"Buenas tardes {nombre}")
else: 
    print(f"Buenas noches, {nombre}")
