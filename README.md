# Calculadora de integrales sencillas  

- [x] Esta calculadora es un mini proyecto que realiza aproximaciones de algunas integrales definidas,
      el programa aproximará las integrales de las funciones que se le den, siempre y cuando sean funciones continuas, estén definidas en todo su dominio.

- [x] Se probó con  las integrales de los ejercicios de la sección 5.6 del libro "Cálculo con      geometría analítica - Earl W. Swokowski". 

- [x] El programa no es a prueba de tontos xd, por ahorro de tiempo, sin embargo es una herramienta útil si se usa con total claridad por ejemplo sabiendo que n > 0. 


<p align="left">
  <!-- Fecha - Último commit -->
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/BETAPANDERETA/Calculadora-b-sica-integrales-sencillas?style=for-the-badge">
  <!-- Issues icono -->
  <a href="https://github.com/BETAPANDERETA/Calculadora-b-sica-integrales-sencillas/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/BETAPANDERETA/Calculadora-b-sica-integrales-sencillas?style=for-the-badge"></a>
  <!-- Stars icono -->
  <a href="https://github.com/BETAPANDERETA/Calculadora-b-sica-integrales-sencillas/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/BETAPANDERETA/Calculadora-b-sica-integrales-sencillas?color=yellow&style=for-the-badge"></a>
  <!-- Viendo icono -->
  <!-- Licencia-->
</p>

## Requisitos:

1. Módulo tabulate 0.8.7 [Descarga el módulo acá](https://pypi.org/project/tabulate/)

## ¿Cómo funciona? (Resumen)

:one: El programa realiza aproximaciones numéricas con tres algoritmos ya conocidos.

:two: La función que se le proporciona en el código es tomada como una "curva" y además se le dice el intervalo sobre el que se "integrará".

:three: Toma el intervalo que se le da por consola y lo divide n-veces (El usuario decide el intervalo y n), siendo n la cantidad de particiones que se realizará por debajo de la curva introducida.

:four: Al tratarse de aproximaciones entre mayor sea "n" mayor será la aproximación de la integral y menor el error de estimación.

:five: Los algoritmos con los que se realiza la aproximación son:

- [x] Rn: Aproximación tomando el extremo derecho de cada partición (rectángulo)

<p align="center">
  <img width="162" height="82" src=Images/Rn.png>
</p>

- [x] Regla del Trapecio: Aproximación tomando trapecios en vez de rectángulos.

<p align="center">
  <img width="427" height="92" src=Images/trapecio.png>
</p>

- [x] Regla de Simpson: Aproximación tomando Parábolas, n debe ser par en este caso:

<p align="center">
  <img width="562" height="65" src=Images/simpson.png>
</p>


## Demostración - ejemplo

- [x] La función probada es:  (se realizará simplemente la aproximación con 6 particiones(n = 6), sin embargo pueden ser introducidas la cantidad de particiones que se quieran)

<p align="center">
  <img width="218" height="79" src=Images/int_ej.png>
</p>

- [x] La función introducida en el código se ve:

<p align="center">
  <img width="600" height="200" src=Images/loc_func.PNG>
</p>

- [x] Las aproximaciones obtenidas por Rn, trapecio y Simpson son (Imágenes de visualización de datos en la terminal):

<p align="center">
  <img width="200" height="200" src=Images/Rn_demo.PNG>
  <img width="200" height="200" src=Images/Trapecios_demo.PNG>
  <img width="200" height="200" src=Images/Simpson_demo.PNG>
</p>

## Uso
1. Ubicar la función deseada en donde corresponde - Linea 47.
2. Dar cantidad de particiones, a y b (Esta parte es muy intuitiva, el programa le pedirá estos datos por consola).
3. Asegúrese que la función sea continua en el intervalo que dió, el programa no realiza integrales impropias, ni mucho menos pretende reemplzar a Symbolab, este solo hace aproximaciones númericas de integrales definidas.

## Integrales probadas

<p align="center">
    <img width="400" height="400" src=Images/list_int.jpeg>
</p>

## Licencia
Licencia MIT (Open source)