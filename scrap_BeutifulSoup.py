from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'

# envio de solicitud a la web
respuesta = requests.get(website)

# obtencion del texto
contenido = respuesta.text

# localizar elementos en una web,
sopa = BeautifulSoup(contenido, 'lxml')

# ver resultados con formato html
# print(sopa.prettify())

# orden de búsqueda:
# 1.id
# 2.Class name 3
# 3.Tag name, CSS selector
# 4. Xpath

# contenido seleccionado usando id, class
caja = sopa.find('article', class_ = 'plot')

# nombre de la película
titulo = sopa.find('h1').get_text()
# strip=True -> elimina los espacios al principio y al final del string al poner como separador ' '
transcripcion = sopa.find('div', class_ = "full-script").get_text(strip = True, separator = ' ')

# Crear archivo de texto y llenarlo con el contenido de transcripcion
with open(f'{titulo}.txt', 'w', encoding="utf-8") as file:
    file.write(transcripcion)
