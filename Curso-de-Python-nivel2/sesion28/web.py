import requests
from bs4 import BeautifulSoup

#url = "https://soundcloud.com/"
#url = "https://en.wikipedia.org/wiki/Geralt_of_Rivia"
url = "https://quotes.toscrape.com/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True)
        autor = quote.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip = True) for tag in quote.find_all("a", class_="tag")]

        print(f"Cita: {text}")
        print(f"Autor: {autor}")
        print(f"Etiquetas: {','.join(tags)}")
        print("-"*50)
else:
    print(f"Error: {response.status_code}")

'''page = 1
while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    
    if 'No quotes found !' in response.text:
        break  # Sale del while cuando no encuentra citas

    soup = BeautifulSoup(response.text, "html.parser")
    citas = soup.find_all('div', class_='quote')

    for cita in citas:
        texto = cita.find("span", class_="text").text
        autor = cita.find("small", class_="author").text
        print(f"Cita: {texto}\nAutor: {autor}\n")

    page += 1

#print(response.status_code)'''


#Obtiene el codifo html de la pagina limitado en est caso alos 500 caracteres
'''print(response.text[:500])
if response.status_code == 200:
    print("Solicitud exitosa")
    print(response.text[:500])
else:
    print("Error: ", response.status_code)'''

#Este trae todo el codigo de html 
#html = response.text

#Obtener una clase en especifico
#elementos = soup.find_all("div", class_="errorPage__inner sc-hidden")
#for e in elementos:
#    print(e)
#Obtener todos los titulos
#titulo = soup.find("p")
#parrafos = soup.find_all("p")
#for p in parrafos:
#    print(p)
#print(titulo)
#print(soup.prettify())
