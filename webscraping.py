import bs4
import requests

#lo que hacemos es poner en un variable 
#con el metodo reuqest.get
#el enlace a la pagina web de busqueda 

resultado=requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
#.text nos muestra todo el texto fuente de la web 
#print(resultado.text) 

#transforma el string en elemnto legible
#realizamos el parsing
#usamos el motot lxlm
sopa=bs4.BeautifulSoup(resultado.text, 'lxml')
#select nos permite seleccionar la etiqueta
print(sopa.select('title'))
#me imprime el titulo
#[<title>Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python</title>]
#----------------------------------------------------
print(sopa.select('h1'))
#me imprime esto 
#[<h1>
#<a href="https://escueladirecta-blog.blogspot.com/">
##</a>
#</h1>]
#-----------------------------------------------
#si quiero ver le contenido sin etiquetas
print(sopa.select('title')[0].getText())
#nos imprime 
#Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python
#--------------------------------------------
parrafo=sopa.select('p')[3].getText()
print(parrafo)
#nos imprime solo el parrafo que esta en el indice 3 sin etiquetas
#instancia + _ + NombreClase + método/atributo oculto
#---------------------------------------------------------
#oebtenemos toda una clase con el .y la clase
columna_lateral=sopa.select('.content p')
for p in columna_lateral:
    print(p.getText())

