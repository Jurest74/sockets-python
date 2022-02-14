# yacurl

Este programa realizado en Python se concecta por medio de sockets a un servidor y descarga el archivo html y los recursos a la carpeta donde se ejecute.

<h3>Para tener en cuenta: </h3>

* Para correr este programa deberá contar con un ambiente en que pueda correr Python, recomentamos el editor VS CODE
* nuestro programa contiene 2 archivos, uno llamado "data.txt" que contiene la siguiente estructura: url completa - host - puerto

![image](https://user-images.githubusercontent.com/43093044/153802038-f479eb6c-81f3-4c8d-8d6a-57cce48dfaf6.png)

Si desea modificar alguno de los parametros no modificar la estructura de este.

Adicionalmente un archivo llamado "Cliente.py" donde esta el programa

* Para una correcta ejecucion debe instalar los paquetes.

![image](https://user-images.githubusercontent.com/43093044/153802885-5c15cf24-3e2c-4cda-a220-68b1c1e98f20.png)


<h3>Ejecución</h3>

- En VS CODE al tener el programa podemos ejeutar con f5

En la consola verá el resultado de la siguiente manera:


* La primera parte nos indica la descarga de imagenes o recursos 

![image](https://user-images.githubusercontent.com/43093044/153802982-5a7c783a-76df-48ad-835d-ffc33bcbed66.png)

* Luego veremos la confirmación de la conexión con el servidor

![image](https://user-images.githubusercontent.com/43093044/153803063-bf4e2fcb-463e-4da0-bd63-27f5ff5bcb96.png)

* Posteriormente nos enseñará la cabecera http

![image](https://user-images.githubusercontent.com/43093044/153803123-99eb62b1-c58b-4e6f-8303-a5e03a3b20d6.png)

* Finalmente podemos visualizar un string con el html 

![image](https://user-images.githubusercontent.com/43093044/153803175-f021256e-10b5-452e-be70-19e1039efddf.png)

<h3>Output</h3>

Si regresamos a el directorio donde se encuentra nuestro programa veremos que se ha genera un archivo html y un directorio icons con los recursos

![image](https://user-images.githubusercontent.com/43093044/153803342-3a5af152-249e-4477-b714-b959060a05e8.png)

![image](https://user-images.githubusercontent.com/43093044/153803358-bdf29fd3-f835-48a3-92d1-837865d9ec5e.png)

<h4>Referencias</h4>

- https://www.thepythoncode.com/article/download-web-page-images-python
- https://www.scrapingbee.com/blog/web-scraping-101-with-python/
- https://github.com/st0263eafit/st0263-2261/tree/main/sockets/python





