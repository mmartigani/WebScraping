import bs4
import requests

#crear una url sin nro de pagina 
url_base='http://books.toscrape.com/catalogue/category/books_1/page-{}.html'

#creamos una lista vacia para agragar
#los titulos a medida que los encontremos 

titulo_rating_alto=[]
#iterar las paginas 
for pagina in range(1,51):
     
     
     url_pagina=url_base.format(pagina)
     resultado=requests.get(url_pagina)
     sopa=bs4.BeautifulSoup(resultado.text, 'lxml')
     
     #seleccionar datos de los libros 
     libros=sopa.select('.product_pod')
     #chequea que los libros tengan 4 y 5 estrellas
     for libro in libros :
          if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')):
               #guardar titulo en un avar 
               titulo_libro=libro.select('a')[1]['title']
               #agregar el libro a lista 
               titulo_rating_alto.append(titulo_libro)

#ver los libros de 4 y 5 estrellas 
for t in titulo_rating_alto:
     print(t)
