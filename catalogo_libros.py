import bs4
import requests


url_base='http://books.toscrape.com/catalogue/category/books_1/page-{}.html'
#nos muestra los enlaces alas 10 primeras paginas del catalogo
for n in range(1,11):
    print(url_base.format(n))
    
#nos devuelve las primeras 10 paginas del libro 
#http://books.toscrape.com/catalogue/category/books_1/page-1.html
#http://books.toscrape.com/catalogue/category/books_1/page-2.html
#http://books.toscrape.com/catalogue/category/books_1/page-3.html
#http://books.toscrape.com/catalogue/category/books_1/page-4.html
#http://books.toscrape.com/catalogue/category/books_1/page-5.html
#http://books.toscrape.com/catalogue/category/books_1/page-6.html
#http://books.toscrape.com/catalogue/category/books_1/page-7.html
#http://books.toscrape.com/catalogue/category/books_1/page-8.html
#http://books.toscrape.com/catalogue/category/books_1/page-9.html
#http://books.toscrape.com/catalogue/category/books_1/page-10.html

#ahora extraemos los titulos que contienen 
#5 estrellas 

