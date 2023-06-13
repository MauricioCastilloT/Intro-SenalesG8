# Filtros Digitales

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Introducción y conceptos previos](#introducción-y-conceptos-previos)
  * [Metodología](#metodología)
  * [Gráficos de resultados](#gráficos-de-resultados)
  * [Resumen y explicación final](#resumen-y-explicación-final)
  * [Archivos](#archivos)
* [Conclusiones](#conclusiones)
* [Bibliografía](#bibliografía)

## Objetivos:

*  Diseño de un filtro tipo FIR usando Dataset obtenido.
*  Diseño de un filtro tipo IIR usando Dataset obtenido.
*  Ploteo de información usando la herramienta Jupyter Notebook.
*  Observar las diferencias entre señal cruda y señal filtrada.

## Materiales y equipos:

<div align="center">
 
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |


</div>
* El Kit de BiTalino incluye la placa BiTalino, una bateria y electrodos junto con dos cables de 3 y 2 hilos.

## Entregable:

<p align="justify">En el laboratorio pasado se realizó una tabulación de data, con el fin de analizar y visualizar de forma más precisa y ordenada las señales adquiridas anteriormente; en nuestro caso en particular, hemos decidido realizar este proceso en las señales adquiridas de ECG con ayuda de un BiTalino; el proceso llevado a cabo para la adquisicon de ECG se puede ver en el siguiente enlace:</p> 

 - [ECG lectura](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electrocardiograf%C3%ADa/Electrocardiograf%C3%ADa.md)

<p align="justify">Por otro lado, tambien buscamos tabular y etiquetar la data con el fin con el fin de aplicar técnicas de machine learning de una forma mas eficiente en un futuro; ya que es eficiente para el reconocimietno de patrones en distintas señales [5].</p>

<p align="justify">En el presente laboratorio se realizará el filtrado de la señal antes mencionada, para lo cual se trabajará con técnicas de filtros FIR e IRR. Para realizar este proceso usaremos un notebook de jupyter.</p>


### Introducción y conceptos previos
### Filtros 

<p align="justify">En los sistemas eléctricos y electrónicos, en ciertas ocasiones, se necesita manejar información a ciertas frecuencias; es por esto que solo se deja pasar a ciertos grupos de frecuencias y las demás se eliminan. Esta función la realizan los filtros que son sistemas electrónicos que presentan características selectivas de frecuencias. </p>

<p align="justify">Segun el tipo de señal, estos se dividen en filtros analógicos y digitales [1].</p>

#### Filtros analógicos:
<p align="justify">Sirven para procesar señales analógicas o señales de tiempo continuo y se dividen en filtros activos, pasivos y de capacidad conmutada [2].</p>

#### Filtros digitales:
<p align="justify">Estos filtros, dependiendo de las variaciones de señal de entrada en tiempo y amplitud, se realiza un procesamiento matematico en la señal mediante FFT (Transformada Rapida de Fourier) obteniendo una señal de salida.</p>
Hay diferentes tipos de filtro, como [3]:

* De acuerdo con la parte del espectro que dejan pasar y que atenúan hay:

	- Filtros pasa alto.
	
	- Filtros pasa bajo.
	
	- Filtros pasa banda.
	
	- Banda eliminada.
	
	- Multibanda.
	
	- Pasa todo.
	
	- Resonador.
	
	- Oscilador.
	
	- Filtro peine (Comb filter).
	
* De acuerdo con su orden:

	- Primer orden
	
	- Segundo orden

* De acuerdo con el tipo de respuesta ante entrada unitaria:

	- FIR
	
	- IRR

#### Filtros FIR: 
Finite Impulse Response.
<p align="justify">Su base consiste en conectar la entrada del filtro a una serie de retardos, con diferentes cantidades de muestras, posteriormente se atenua con un factrode ganancia específico y filamnete se suman las salidas [4].</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236109318-4a0977d0-774e-4082-ad1a-efde152e04c2.png" align="center"/>
</p>

<p align="justify">Los filtros FIR, suelen usar el método de ventaneo, esto con el propósito de diseñar un filtro ideal. El proceso de windowing de una señal consiste en multiplicar el registro temporal por una ventana de suavizado de longitud finita cuya amplitud varía suave y gradualmente hacia cero en los bordes. La longitud, o intervalo de tiempo, de una ventana de suavizado se define en términos de número de muestras.</p>
Se tienen algunas de las siguientes:

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236267784-50c7bcca-ed05-46d5-a1c4-34cca28f81ef.png" align="center"/>
</p>

Las ventanas más usadas en este método son: 
* Bartlett: se puede observar que tiene una forma triangular, se suele usar para suavizar señales.

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236265074-65658d3b-f62c-40b0-b2d0-65f5a613ae78.png"/>
</p>
<p align="center">
	Recuperado de Matlab 
</p>
* Rectangular: Los valores de estas ventanas sólo varían entre 1 y 0, este filtro logra que la señal no cambie en 1 y se elimine en 0.

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236265524-6ed6b73b-c190-475e-bee5-c18b9973d2ac.png"/>
</p>
<p align="center">
	Recuperado de Matlab 
</p>
* Blackman: tiene forma cónica gracias a que esta estructuradas  por cósenos, sirve para atenuar los lóbulos laterales de la señal.

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236265863-946ec0c9-748e-4773-94e8-a5293e8e8be7.png"/>
</p>
<p align="center">
	Recuperado de Matlab 
</p>
* Hanning: Usa transformada de Fourier para su filtrado y busca casi eliminar los lados laterales de la señal.

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236265968-77d84902-4d4c-4007-a68d-df833a3319c7.png"/>
</p>
<p align="center">
	Recuperado de Matlab 
</p>
* Hamming:  Busca reducir las discontinuidades de los laterales.

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236266045-4fd1a534-8963-4098-bf2f-a764c08825ba.png"/>
</p>
<p align="center">
	Recuperado de Matlab 
</p>


#### Filtros IIR:
Infinite Impulse Response.
Utiliza retrasos para los valores a la entrada del filtro, toma también los valores de la salida, les aplica una nueva cadena de retrasos y retroalimenta esta señal a la entrada del filtro [4].

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236109230-4f47e80a-49b7-4bba-b0aa-583bd07f0283.png" align="center"/>
</p>

- **Butterworth:** <p align="justify">Son filtros IIR que proporcionan una respuesta suave y uniforme en la banda se paso, sin picos  ni caídas pronunciadas. Este tipo de filtro se utiliza comúnmente cuando se requiere una respuesta en frecuencia plana en la banda de paso, sin importar la atenuación en la banda de rechazo.</p>

- **Bessel:** <p align="justify">Tipo de filtro electrónico, que únicamente tiene polos. Están diseñados para tener una fase lineal en las bandas pasantes, por lo que no distorsionan las señales; por el contrario tienen una mayor zona de transición entre las bandas pasantes y no pasantes.</p>
- **Elíptico:** <p align="justify">Filtro diseñado de manera que consiguen estrechar la zona de transición entre bandas y también acota el rizado en estas bandas.</p>
- **Chebyshev:** <p align="justify">Son un tipo de filtro electrónico, puede ser tanto analógico como digital. Con estos se consigue una caída de la respuesta en frecuencia más pronunciada en frecuencias bajas debido a que permiten rizado en alguna de sus bandas (paso o rechazo). Existen 2 tipos de filtro de chebyshev: los de tipo I, que solo tienen polos; y los de tipo II, que tienen ceros y polos.</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/236267674-685281e4-a02d-4dc3-a8ee-ba8d21c52051.png" align="center"/>
</p>


### Metodología

1. Se trabajó con el Dataset de la señal ya obtenido.
2. Se utilizó Jupyter Notebook para poder desarrollar los filtros respectivos.
En este apartado se encuentran los códigos en los que se desarrollaron los filtros y su explicación respectiva paso a paso.
- [Filtros FIR](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Filtros_Digitales/FiltroFIR_laboratorio_7.ipynb)
- [Filtros IRR](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Filtros_Digitales/FiltroIIR_laboratorio_7.ipynb)

#### Filtro FIR
- Primero se plotean las señales sin filtrar.
- Se calcula la transformada rápida de Fourier mediante el comando fft y se grafica.
- Se procede a diseñar el filtro FIR pasa bajos con una frecuencia de corte en 50Hz y una ventana de tipo Hamming de longitud 37.
- Se grafica la señal en el dominio de a frecuencia, junto a su frecuencia de corte.
- Se aplica el filtro a las señales ECG.
- Finalmente se grafican las señales filtradas en el dominio del tiempo.

#### Filtro IIR
- Primero se plotean las señales sin filtrar.
- Se calcula la transformada rápida de Fourier mediante el comando fft y se grafica.
- Se realiza el análisis espectral de las señales y se identifican los picos de frecuencia.
- Se procede a diseñar el filtro IIR pasa bajos de orden 9 con una frecuencia de corte calculada en 14.96Hz.
- Se realiza la transformada bilineal y posteriormente se aplica el filtro a las señales ECG.
- Finalmente se grafica las señales filtradas en conjunto con las señales no filtradas con el fin de compararlas y analizar el efecto del filtro a la señal ECG.

### Gráficos de resultados

| Señal |Señal cruda| Filtro IIR| Filtro FIR | 
| :---:  |  :----: | :----: | :----: |
| **Basal**|<p><img src="https://user-images.githubusercontent.com/70769712/236269571-c611cc34-ec91-4768-9060-2f9704a548f5.png"/></p>|<p><img src="https://user-images.githubusercontent.com/70769712/236269141-6ab3e6f1-7d49-42cf-8c09-7a58770eef49.png"/></p>|<p><img src="https://user-images.githubusercontent.com/70769712/236271049-40733403-cbf5-4541-a110-1acd70cf6958.png"/></p>|
| **Respiración**|<p><img src="https://user-images.githubusercontent.com/70769712/236269667-d85a0165-104a-49a3-a4a8-aa5f5ceb75a8.png"/></p>|<p><img src="https://user-images.githubusercontent.com/70769712/236268904-098bf201-ea33-49c0-abce-c3212663f702.png"/></p>|<p><img src="https://user-images.githubusercontent.com/70769712/236271109-b04b16c7-4d53-42a2-b849-948536de7601.png"/></p>|
| **Post-ejercicio**|<p><img src="https://user-images.githubusercontent.com/70769712/236269745-d078d980-8abc-44d3-b74c-a4e2da6eaa3f.png"/></p>|<p><img src="https://user-images.githubusercontent.com/70769712/236269462-7c2214e3-3738-48d4-8616-c940d270ed32.png"/></p>|<p><img src="https://user-images.githubusercontent.com/70769712/236271157-c4f89d45-92ff-41bc-866e-5778f47747a1.png" /></p>| 

#### Las imágenes se pueden observar de manera más clara en los códigos proporcionados en Metodología.

### Resumen y explicación final 
 
<p align="justify">En el caso del filtros FIR e IIR, se optó por el uso del filtro monotónico butterworth para ambos casos, aunque los filtros IIR son más comunes debido a su mayor eficiencia computacional [5], En clase se mencionó que el Butterworth es quizá el filtro más usado ya que la amplitud de la señal de salida se atenúa a un ritmo constante en la banda de atenuación, lo que significa que la transición de la banda de paso a la banda de atenuación es muy suave y gradual. En consecuencia, el filtro Butterworth se considera un filtro "máximamente plano" porque evita resonancias en la banda de atenuación y no introduce mucho rizado en la banda de paso, esto último es importante porque todas las frecuencias dentro de la banda de paso se atenúan por igual [6]. Esto ayuda a mantener la forma de la onda original de la señal ECG y se reduce el riesgo de un mal diagnóstico por errores introducidos durante el filtrado. </p>

<p align="justify">En cuanto al código en el caso FIR se convierte la señal al dominio de la frecuencia para poder ser filtrada con “firwin” de la libreria “spicy.signal”, se definen la longitud de ventana y frecuencia de corte para filtrar la señal original y realizar la transformada de fourier de esta, se calcula la magnitud y las frecuencias de la señal transformada, y se grafica la magnitud frente a la frecuencia en una figura para luego graficar la señal filtrada en el dominio del tiempo.</p>

<p align="justify">Entre los parámetros más importantes se encuentran la frecuencia de corte y la ventana, la cual en esta ocasión fue Hamming el cual por su forma cónica provee atenuación de frecuencias no deseadas, lo que sucede es que la amplitud de la señal del electrocardiograma es muy pequeña en relación con las frecuencias no deseadas y se debe utilizar una ventana que atenúe estas frecuencias y permita la visualización de la señal de interés.</p>

<p align="justify">Otra cosa curiosa sobre la ventana Hamming en FIR y que también es útil es la reducción del error de gibbs que es un fenómeno que puede ocurrir en la transformada de Fourier de una señal, esta técnica es usada en el código de creación del filtro FIR.</p>

<p align="justify">En el caso del filtro IIR este no usa ventanas si lo comparamos con el filtro FIR podría destacarse que los IIR requieren menos coeficientes que los FIR para lograr la misma respuesta en frecuencia, lo que significa que pueden ser más eficientes computacionalmente [7]. Tambien los cambios en la señal de entrada se reflejan en la señal de salida de manera más rápida y sin distorsión. Esto sería útil en electrocardiógrafos con filtrado en tiempo real sumado a la mayor flexibilidad de diseño que ofrecen los IIR al no emplear ventanas y poder enfatizar la frecuencia deseada. La generación del código involucra un ajuste en la respuesta en frecuencia del filtro mediante la transformación de esta, lo que implica el mapeo de las frecuencias del filtro especificado a una banda de frecuencia estándar. En el caso del filtro Butterworth usado, se utiliza una transformación bilineal, que mapea las frecuencias del filtro especificado a la banda de frecuencia de Nyquist y en realidad hace la trasnformación al dominio z de una función (misma labor de un ADC en una señal). Esta función de transferencia ya puede ser analizada y obtener sus coeficientes de filtro para su imlementeación en la parte final.</p>

<p align="justify">El filtrado colabora visualmente a una reducción en el rizado correspondiente a las frecuencias sinusoidales inútiles semejatntes a ruidos, esto se observa más que todo en las zonas de las ondas P y T las cuales ahora si pueden distinguirse con más claridad. En realidad tambien podían distinguirse con esfuerzo en las gráficas sin filtrar sin embargo para un programa de Machine Learning no sería tan sencillo detectar anomalías sin un correcto filtrado y “alisado de la señal”. En el caso de la onda QRS (despolarización ventricular) no se nota mucho cambio ya que es una señal más prominente. </p>

<p align="justify">Otro dato interesante es que el caso en el que menos se lograron filtrar los rizos es en el de aguante de la respiración, en el laboratorio de ECG comentamos que específicamente esta señal presentaba un extraño compontamiento sinusoidal general que hacia oscilar a toda la onda, esto similar a un cuadro de disnea provocado por aguante prolongado de la respiración, esto es coincidente con el menor filtrado de esos agentes sinusoidales muchos delos cuales pudieron pasar dentro de la banda de paso.</p>

<p align="justify">Como observación adicional se destaca la presencia de una señal en corriente directa con frecuencia cercana o igual a cero en el gráfico de frecuencias, esto se cree que puede deberse a algún componente estático (ruido o artefacto) causado por el bitalino.</p>

### Archivos
Se procesaron distintos archivos en Python y se obtuvo el siguiente código:
- [Filtros FIR](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Filtros_Digitales/FiltroFIR_laboratorio_7.ipynb)
- [Filtros IRR](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Filtros_Digitales/FiltroIIR_laboratorio_7.ipynb)


## Conclusiones
Respecto a laboratorio realizado, se concluye lo siguiente:

-Tras el filtrado de las señales se pudo observar mejoras en las mismas, tales como la disminución del ruido que presentaban y de la amplitud, dejandonos una señal mas limpia y con los componentes que son netamente de nuestro interes.

-Por otro lado, se comprobó que el filtrado con el filtro IIR son menos eficientes que con el filtro FIR, ya que estos ultimos son más estables, lo que los hace más adecuados para esta aplicación.

## Bibliografía 

[1]“FILTROS TEMA 4.” Available: https://catedras.facet.unt.edu.ar/e1/wp-content/uploads/sites/124/2018/04/Tema-4-1.pdf

[2] “INTRODUCCIÓN A FILTROS ANALÓGICOS CAPÍTULO 1.” Available: http://catarina.udlap.mx/u_dl_a/tales/documentos/lem/torres_d_ld/capitulo1.pdf

[3]“Filtro digital,” Los diccionarios y las enciclopedias sobre el Académico, 2023. https://es-academic.com/dic.nsf/eswiki/487449 (accessed May 04, 2023).

‌[4]JuanS, “IIR vs FIR: Entendiendo realmente sus diferencias,” JuanSaudio, Apr. 23, 2020. https://www.juansaudio.com/post/iir-vs-fir-entendiendo-realmente-sus-diferencias (accessed May 04, 2023).

[5] F. butterworth, “FIR butterworth also possible or just IIR?,” Signal Processing Stack Exchange, Dec. 19, 2018. https://dsp.stackexchange.com/questions/54258/fir-butterworth-also-possible-or-just-iir (accessed May 04, 2023).

[6] D. Filtros, L. Martínez, A. Gómez, J. Serrano, J. Vila, and Gómez, “2.1,” 2009. Available: [http://ocw.uv.es/ingenieria-y-arquitectura/filtros-digitales/tema_2._revision_de_los_tipos_de_filtros_analogicos_mas_comunes.pdf](http://ocw.uv.es/ingenieria-y-arquitectura/filtros-digitales/tema_2._revision_de_los_tipos_de_filtros_analogicos_mas_comunes.pdf).

[7] “Khan Academy,” Khanacademy.org, 2023. https://es.khanacademy.org/science/ap-chemistry/thermodynamics-ap/gibbs-free-energy-tutorial-ap/a/gibbs-free-energy-and-spontaneity (accessed May 04, 2023).
‌
[8] “BITalino (r)evolution Lab Guide.” Available: [https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf)
