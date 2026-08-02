
#librerias principal de selenium para controlar el navegador
import undetected_chromedriver as uc #libreria 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # se usa para simular teclas del teclado ujum
import time #libreria para manejar tiempos y pausas
import random

#configuracion para el capcha
options = uc.ChromeOptions()
options.add_argument("--disable.blink-features=automationControlled")
options.add_experimental_option("ExcludeSwitches", ["Enable-automation"])
options.add_experimental_option("UserAutomationExtension", False)

#instalador google
driver = uc.Chrome()
driver.get("https://www.google.com") #petición GET
time.sleep(random.uniform(2, 4)) #tiempo de espera

buscador = driver.find_element(By.NAME, "q")
for letra in "vacantes Business Intelligence":
    buscador.send_keys(letra)
    time.sleep(random.uniform(1,3))

time.sleep(3)
print(f"titulo de la pagina: {driver.title}")
driver.quit()
