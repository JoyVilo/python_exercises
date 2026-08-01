from datetime import datetime
import random

nombres = ["Isabella", "Carlos", "Marga", "Mari", "Nani"]
ahora = datetime.now()
ganador = random.choice(nombres)

print(f"el sorteo realizado el {ahora.strftime('%d/%m/%y')} a las {ahora.strftime('%H:%M')}")
print(f"el ganador es: {ganador}")
