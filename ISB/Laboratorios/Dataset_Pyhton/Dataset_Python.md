# Dataset en Python

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Video de señal](#video-de-señal)
  * [Metodología](#metodología)
  * [Archivos](#archivos)
  * [Resumen y explicación final](#resumen-y-explicación-final)
* [Bibliografía](#bibliografía)

## Objetivos:

*  Uso de Machine Learning para tabulamiento de data.
*  Etiquetado de señales fisiológicas a elección.
*  Ploteo de información usando la herramienta Jupyter Notebook.

## Materiales y equipos:

<div align="center">
 
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |


</div>
* El Kit de BiTalino incluye la placa BiTalino, una bateria y electrodos junto con dos cables de 3 y 2 hilos.

## Entregable:

<p align="justify">En el presenta laboratorio se realizara una tabulacion de data, con el fin de analizar y visualizar de forma más precisa y ordenada las señales adquiridad anteriormente; en nuestro caso en particular, hemos decidido realizar este proceso en las señales adquiridas de ECG con ayuda de un BiTalino; el proceso llevado a cabo para la adquisicon de ECG se puede ver en el siguiente enlace:</p> 

 - [ECG lectura](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/Electrocardiograf%C3%ADa.md)

<p align="justify">Por otro lado, tambien buscamos tabular y etiquetar la data con el fin con el fin de aplicar técnicas de machine learning de una forma mas eficiente en un futuro; ya que es eficiente para el reconocimietno de patrones en distintas señales [5].</p>

Para realizar este proceso usaremos un notebook de jupyter.

### Video de señal 

En este apartado se muestran los videos tomados de la experiencia de recolección de señal ECG.

<p align="justify">* En el siguiente video se puede apreciar la conexión realizada a nuestra primera voluntaria y la señal en OpenSignals:</p>

<div align="center">
 
https://user-images.githubusercontent.com/112776840/231618914-66f3d1f1-3933-498b-9900-fd5bc1ee13d4.mp4</div>
 
<p align="justify">* En el siguiente video se puede apreciar la conexión realizada a nuestro segundo voluntario y la señal en OpenSignals:</p>


<div align="center">
 
https://user-images.githubusercontent.com/112776840/231617441-02dbf5d8-f1d0-44a4-80b0-941cba20b578.mp4</div>

<p align="justify">* En el siguiente video se puede apreciar la señal en OpenSignalsFluke resultante del dispositivo ProSim 4 Vital Signs Patient Simulator l:</p>

<div align="center">
 
https://user-images.githubusercontent.com/112776840/231617142-4a1971af-5ae0-406b-9d3f-806a9d6b91b8.mp4</div>
  
  
<p align="justify">* En el siguiente video se puede apreciar un ejemplo de ejercicio dinámico realizado para la toma de muestra.</p>

<div align="center">
 
https://user-images.githubusercontent.com/112776840/231619183-9ec122a2-e994-4164-91b1-67aa8ff66fae.mp4</div>

### Metodología
<p align="justify">En este apartado explicaremos la metodología que utilizamos para el desarrollo de este laboratorio.</p>

1. El primer paso fue seleccionar los archivos que utilizaremos provenientes del laboratorio 4, el cual corresponde a las señales ECG. En total, fueron 4 archivos los utilizados. Además importamos las librerías necesarias y seleccionar el estilo de ploteo. 
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234915980-21f84bbc-057e-4551-84dc-3c369d054a92.png" align="center" width="600" height="300"/></p>

2. Luego de seleccionar estos archivos lo que hicimos fue realizar la lectura de la data y luego agruparlas en arrays.
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234916187-900af7e8-653b-4792-bb34-ca5c39107d15.png" align="center" width="600" height="300"/></p>

3. Luego lo que hicimos será seleccionar solo la data del sensor que deseamos.
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234916472-e5c9bc60-1269-4fde-a1bf-f73e220be28d.png" align="center" width="600" height="300"/></p>

4. Posteriormente procesamos estos arrays y lo graficamos. Se obtuvieron todas las gráficas, la siguiente corresponde al estado basal:
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234916603-ebf3e7db-587b-4e82-a5ab-e32021177000.png" align="center" width="600" height="300"/></p>

5. Ahora pasaremos la señal a en función del tiempo para poder graficarla, teniendo en cuenta que la frecuencia de muestreo utilizada fue de 1000 Hz. 
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234916804-9e21ba07-1375-4a8b-81af-22f2cbbbf588.png" align="center" width="600" height="300"/></p>
El resultado fue el siguiente: 
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234916937-5722b973-8859-472b-b349-a010146b5424.png" align="center" width="600" height="300"/></p>

6. Para poder tabular, primero necesitamos definir unas etiquetas dependiendo de la fase del ejercicio realizado. Estas fueron: estado basal, luego de aguantar la         respiración y luego de hacer ejercicio. 
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234917055-561f9404-0a17-4d79-8952-4e1d5108a5b6.png" align="center" width="600" height="300"/></p>

7. Para finalizar, realizamos la tabulación de la data 
<p align="center">
<img src="https://user-images.githubusercontent.com/128628819/234917190-5af5ad69-d4a4-461e-917e-2f7119f5da9a.png" align="center" width="600" height="300"/></p>


Finalmente obtuvimos las siguientes señales posterior a la tabulación realizada en el codigo explicado:

* Voluntario 1:
 
| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Lectura en estado basal**   | ![Basal](https://user-images.githubusercontent.com/70769712/234919228-b8b87824-32b7-4b02-99f9-e595f4bcfc20.png)  | 
| **Lectura post ejercicio**  |  ![Despues de no respirar](https://user-images.githubusercontent.com/70769712/234919339-6e4015d4-d476-4758-ad65-044325e9abfd.png)  | 
| **Lectura sin respirar**   | ![Post Ejercicio](https://user-images.githubusercontent.com/70769712/234919490-82975526-6e42-4bc7-818d-016c6527359d.png) | 

 
* Voluntario 2:

| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Lectura en estado basal**   | ![Reposo manuel](https://user-images.githubusercontent.com/70769712/234919970-0eb9b39e-07fd-4608-bc58-c4f28acaa29e.png)  | 
| **Lectura sin respirar**   | ![Sin Respirar Manuel](https://user-images.githubusercontent.com/70769712/234920048-4d8b3700-c44b-4581-8123-f35663617890.png) | 


Posteriormente e realizo la identificación de los complejos PQRST de cada una de las señales mostradas:

* Voluntario 1:

| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Complejo PQRST en estado basal**   | ![Complejo PQRST Basal](https://user-images.githubusercontent.com/70769712/234920988-fd7335bd-c26f-4c35-9c7b-499d66a52fe3.png)  | 
| **Complejo PQRST post ejercicio**  |  ![Complejo PQRST Post Ejercicio](https://user-images.githubusercontent.com/70769712/234921057-e132fc85-607f-42bf-aec1-52e80bdf6527.png)  | 
| **Complejo PQRST sin respirar**   | ![Complejo PQRST Despues de no respirar](https://user-images.githubusercontent.com/70769712/234921101-78b27908-6c7d-4b17-b025-dee7bc05eb37.png)  | 

* Voluntario 2:

| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Complejo PQRST en estado basal**   | ![Complejo PQRST Reposo manuel](https://user-images.githubusercontent.com/70769712/234921165-ce7b4062-f372-4faa-9d5b-11464c18f252.png) | 
| **Complejo PQRST sin respirar**   | ![Complejo PQRST Sin Respirar manuel](https://user-images.githubusercontent.com/70769712/234921182-321af2df-6b5d-4df6-9b39-a3d809388a30.png) | 


### Resumen y explicación final 
 
<p align="justify">Para el respectivo análisis se extrajo un array de igual longitud para todos los casos descritos, es este array el que representa una unidad de despolarización y repolarización y en la que se pueden observar en mayor o menor medida las ondas PQRST analizables. Son estos arrays la data que también puede ser analizada por un sistema de machine learning.</p>

**Reposo:** <p align="justify">Durante el período de reposo, se observaron los picos QRS que indican la despolarización ventricular del corazón. La señal se mantuvo estable en esta segunda derivada, con una frecuencia cardíaca normal de 70 a 80 latidos por minuto [2]. Sin embargo, la intensidad de la señal no fue tan fuerte como la señal leída por el generador de señales fisiológicas. Esto puede deberse a la falta de uso de un gel conductor que reduce la resistencia entre la piel y el electrodo, o a una colocación poco precisa de los electrodos en el cuerpo. A nivel fisiológico cabe destacar la acción del neurotransmisor acetilcolina el cual es segregado en situaciones de reposo y actúa sobre principalmente en células receptoras del nodo sino auricular, el cual es el principal responsable de la generación de la onda P en el electrocardiograma haciendo más lenta la despolarización y repolarización, la onda más grande QRS se da casi en los 0.3 y luego se da una lenta repolarización. En el estado basal ocurre algo parecido pero esta vez el periodo largo de espera se da antes de QRS, se cree que a causa el array tomado.</p>

**Aguante de la respiración:** <p align="justify">Se comenzó la medición desde un punto neutral y se inició la inhalación justo después. Después de unos 20 segundos, se exhaló para observar cómo reaccionaba la señal. Durante la inhalación, se notó un ligero aumento en la frecuencia cardíaca, lo cual coincide con lo que se indica en [2]. Durante la etapa de aguante de la respiración, se observó un comportamiento sinusoidal entre las zonas T y P de la señal, correspondiente a la repolarización ventricular. Este comportamiento también se extendió a algunas ondas QRS, causando una deformación. Este patrón sinusoidal puede ser el resultado de un esfuerzo excesivo en la respiración, lo que puede producir una apariencia similar a la disnea con esfuerzo y afectar la señal [3]. Cuando aguantamos la respiración disminuye la cantidad de oxígeno que llega al cuerpo, lo que provoca un aumento en la frecuencia cardíaca y cambios en los patrones de las ondas en el ECG. Además, cuando se retiene la respiración, aumenta la presión dentro del tórax lo que a su vez puede comprimir vasos sanguíneos y reducir la llegada de oxígeno, incluso en casos más extremos podría modificar ligeramente la posición del corazón y alterar su relación con los electrodos.</p>

**Despues de ejercicio:** <p align="justify">Durante el experimento, la característica principal fue un aumento en la frecuencia cardíaca, llegando a superar los 120 latidos por minuto (durante los 30 segundos que duró la adquisición). La frecuencia cardíaca disminuyó un poco después del ejercicio intenso, ya que se necesitó tiempo para volver a colocar correctamente los electrodos del "Bitalino". La señal registrada fue similar en frecuencia a la del generador de señales, pero con una menor intensidad debido a las mismas causas que en reposo [4]. Además, se observaron ondas similares en ambos lugares de colocación de los electrodos (tanto en las muñecas como en las clavículas), aunque en el primer caso se experimentó la dificultad de tener que mantener los electrodos a la altura del corazón, lo que posiblemente produjo algún tipo de interferencia en la señal. En general el array mostró una ligera disminución en la amplitud de la onda P ya que el aumento de la frecuencia cardiaca puede reducir el tiempo disponible para que las aurículas se llenen de sangre antes de la contracción.</p>

### Archivos
Se procesó distintos archivos en Python de 2 alumnos como se mencionó anteriormente, cada uno realizó 4 lecturas:
* Lectura en reposo
* Lectura durante aguante de respiración (20 segundos de agunte)
* Lectura tras aguante de respiración ( <= 1 minuto de agunte)
* Lectura depsues de realizar movimientos

Alumna 1 (Ana Paula):

- [Lectura en reposo 1](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_pau1.ipynb)
- [Lectura durante aguante de respiración 1](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_pau2.ipynb)
- [Lectura tras aguante de respiración 1](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_pau3.ipynb)
- [Lectura despues de realizar movimientos 1](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_pau4.ipynb)

Alumno 2 (Manuel): 

- [Lectura en reposo 2](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_manuel1.ipynb)
- [Lectura durante aguante de respiración 2](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_manuel2.ipynb)
- [Lectura tras aguante de respiración 2](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_manuel3.ipynb)
- [Lectura despues de realizar movimientos 2](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_manuel4.ipynb)

Posteriormente se analizo la señal con el simulador de ECG, la cual nos brinda la simulacion de una persona caminando mientras aumenta su velocidad cada 30 segundos:

- [Lectura del simulador](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/grafica_simulador.ipynb)

Archivo de data tabulada:
- [Archivo ipynb](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Dataset_Pyhton/Gu%C3%ADa_laboratorio_6.ipynb)

## Bibliografia 

[1] “BITalino (r)evolution Lab Guide.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

[2] “Relación del electrocardiograma con la respiración y el pulso | Manual de laboratorio de fisiología, 6e | AccessMedicina | McGraw Hill Medical,” Mhmedical.com, 2015. https://accessmedicina.mhmedical.com/content.aspx?bookid=1722&sectionid=116885435 (accessed Apr. 12, 2023).

[3] Enero-Febrero, ActA MédicA coloMbiAnA, vol. 41, 2016, Accessed: Apr. 12, 2023. [Online]. Available: http://www.scielo.org.co/pdf/amc/v41n1/0120-2448-amc-41-01-00074.pdf

[4] “Para qué se utiliza el gel conductor | Sisneo Bioscience,” Sisneo Bioscience, Jan. 25, 2023. https://sisneo.com/para-que-se-utiliza-el-gel-conductor/#:~:text=Y%20el%20gel%20conductor%20permite,precisi%C3%B3n%20de%20los%20resultados%20obtenidos. (accessed Apr. 12, 2023).[1] “BITalino (r)evolution Lab Guide.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

[5] Ayuware, “Tabulación de la información: qué es y en qué consiste,” Blog de Ayuware, Aug. 09, 2021. https://www.ayuware.es/blog/tabulacion-de-la-informacion/#:~:text=Gracias%20a%20la%20tabulaci%C3%B3n%20de,esta%20manera%2C%20a%20conclusiones%20v%C3%A1lidas. (accessed Apr. 27, 2023).

