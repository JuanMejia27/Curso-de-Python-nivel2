from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import keys

'''service = Service("C:/SeleniumDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
#print(driver.title)
elemento = driver.finf_element_by_id("elemento_id")
print(elemento.text)
driver.quit()'''

'''service = Service("C:/SeleniumDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfTg3h5AHG99hVPIMCwerg2SA8Qb33ZMijyUVBfRHFtBqo22Q/viewform")

elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "elemento.id"))
)

botono_seleccion = driver.find_element(By.XPATH, '//*[@id="i9]/div[3]/div')
botono_seleccion.click()

driver.implicitly_wait(10)

boton=driver.find_element(By.XPATH,'//*[@id="mG61Hd]/div[2]/div/div[3]/div/div[1]/div/span/span')
boton.click()
driver.quit()'''

service = Service("C:/sleniumDrivers/chromedriver.exe")
driver = webdriver.chrome(service=service)

try:
    driver.get('https://www.google.com')
    barra_busqueda = driver.find_element(By.CLASS_NAME, 'q')
    barra_busqueda.send_keys('Selenium python')
    barra_busqueda.send_keys(keys.RETURN)
    resultados = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'h3'))
    )
    for resultados in resultados[:5]:
        print(resultados.text)
finally:
    driver.quit()