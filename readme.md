# Python urllib.request ejemplo

## Descripción
Con el objetivo de demostrar el uso de python urllib.request, hemos desarrollado una herramienta que nos permite conocer si una página web puede llegar a tener alguna vulnerabilidad o no.

El modo de hacer esto es comprobando si la página cuenta con algún objeto de tipo oculto (hidden) y/o con código PHP integrado en el front-end.

Ojo, en caso de que cualquier de los casos sea verdadero, no garantiza que sea un punto de penetración, pero nos muestra una posible vulnerabilidad.

## Uso

`py request_vscan.py [-u "http://www.ejemplo1.com,http://www.ejemplo1.com,"] [-f "links.txt"] -o "salida.txt"`

`--urls, -u` nos permite introducir links manualmente separados por una coma (,)

`--file, -f` nos permite introducir links a través de un archivo de texto. (En caso de error, introducir la ruta absoluta.)

`--output, -o` debemos especificar el archivo de salida del programa.