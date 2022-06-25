import bs4
import requests


url_base='http://books.toscrape.com/catalogue/category/books_1/page-{}.html'

resultado=requests.get(url_base.format('1'))#1 de la primera pagina
sopa=bs4.BeautifulSoup(resultado.text,'lxml')

libros=sopa.select('.product_pod')
#estamnos extrayendo los libros de 5 estrellas 
ejemplo=libros[0].select('.star-rating.Three')
#[<p class="star-rating Three">
#<i class="icon-star"></i>
#<i class="icon-star"></i>
#<i class="icon-star"></i>
#<i class="icon-star"></i>
#<i class="icon-star"></i>
#</p>]
print(ejemplo)
#extraemos el nombre dle libro 
ejemplo=libros[0].select('a')[1]['title']
print(ejemplo)
#A Light in the Attic