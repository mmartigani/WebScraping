import bs4
import requests



resultado=requests.get('https://www.escueladirecta.com/courses')
sopa=bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes=sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_1=requests.get(imagenes)
#wb significa escribir binario
#se crea una imagen y la guardo como un archivo en mi carpeta 
f=open('mi_imagen.jpg', 'wb')
f.write(imagen_1.content)
f.close()