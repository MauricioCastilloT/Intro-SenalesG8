# Electrocardiografía 

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Electrocardiograma](#electrocardiograma)
  * [Conexión usada](#conexión-usada)
  * [Metodología](#metodología)
  * [Video de señal](#video-de-señal)
  * [Gráficos OpenSignals](#gráficos-opensignals)
  * [Resumen y explicación final](#resumen-y-explicación-final)
  * [Archivos](#archivos)
  * [Gráficos en Python](#gráficos-en-python)
* [Bibliografía](#bibliografía)

## Objetivos:
En el laboratorio de esta semana buscamos adquirir señales de ECG y observar también la velocidad de conducción de nervios perifericos, todo esto usando la placa BiTalino para su adquisición. Posteriormente se buscará extraer la información de las señales adquiridas por medio del software OpenSignals (r)evolution.
* Adquirir señales biomédicas ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution.

## Materiales y equipos:

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>
* El Kit de BiTalino incluye la placa BiTalino, una bateria y electrodos junto con dos cables de 3 y 2 hilos.

## Entregable: 
### Electrocardiograma 
<p align="justify">Se define como un registro que refleja la actividad eléctrica del corazón, que usualmente se realiza con un aparato llamado electrocardiógrafo, este muestra la direccion y magnitud de las corriente electricas del corazón. 
En los músculos del corazón, la corriente fluye en diferenes direcciones, a partir de esto se obtienen las resultantes de todos los vectores que se generan en un momento dado haciendo uso de electrodos que son debidamente colocados. [1] </p>

<p align="justify">Los latidos cardíacos quedan representados en el ECG normal por las diferentes oscilaciones de la línea basal (línea horizontal existente entre cada latido) en forma de ángulos, segmentos, ondas e intervalos, constituyendo una imagen característica que se repite con una frecuencia regular a lo largo de todo el electrocardiograma. Un ECG normal consta de una serie de deflexiones (ondas del ECG) que alternan con la línea basal. Realizando la lectura de izquierda a derecha, se distinguen la onda P, el segmento P-R, el complejo QRS, el intervalo QT, el segmento ST y finalmente la onda T. Como se observa en la siguiente imagen. [2] </p>

<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231630397-ac9948a1-fdf9-4177-8575-012e9321d685.png" align="center" width="400" height="300"/>
</p>

- La onda P representa la despolarización auricular, es el momento en que las aurículas se están contrayendo y enviando sangre hacia los ventrículos.
- El intervalo PR es el período entre el comienzo de la despolarización auricular y la despolarización ventricular. En este punto aurículas terminan de vaciarse y se produce una desaceleración en la transmisión de la corriente eléctrica a través del corazón, justo antes del inicio de la contracción de los ventrículos.
- El complejo QRS representa la despolarización ventricular. los ventrículos se contraen y expulsan su contenido sanguíneo.
- El intervalo QT es el período entre el comienzo de la despolarización ventricular y el final de la repolarización ventricular.
- El segmento ST representa la despolarización completa del miocardio ventricular. Su elevación o descenso respecto a la línea basal puede indicar ciertas patologías.
- La onda T refleja la repolarización ventricular.


<p align="justify">La placa BiTalino (r)evolution , cuenta con todos los bloques electrónicos necesarios para adquirir bioseñales ya que cuenta con diferentes sensores como de:</p>

- Electromiografía
- Electrocardiografía
- Actividad electrodérmica
- Electroencefalografía
- Acelerómetro 
- Luz 

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230244892-44d09e82-7ea1-4056-95a1-efdb625c0109.jpg" align="center" width="400" height="300"/>
</p>

### Conexión usada
<p align="justify">Este  kit viene con: un cable de dos hilos y un cable de tres hilos, a estos se les puede conectar 5 electrodos. 
Para cumplir con el fin de la práctica , el equipo decidió hacer uso del cable de tres hilos con tres de los electrodos no invasivos:</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230241500-95754d9d-4f83-4f87-8f6d-39dd80ec6c81.png" align="center" width="150" height="150"/></p>


<p align="justify">Este cable contaba con tres tipos de conexiones: positivo, negativo y tierra. La notación por color viene a estar detallada por la siguiente imagen proveniente de <b>BITalino (r)evolution User Manual</b> [3].
Acerca de la señal, se optó por realizar electrocardiografía (ECG).</p>

<p align="center"><img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/6b0bf88c4170eed2da41aea33c30c4093b5a2a31/Images/bitalinomanual.JPG" width="600" height="300"></p>

<p align="justify">Para la realización de la conexión usamos las posiciones indicadas en <b>BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for ECG</b>[4]. Dentro de la cual se nos mencionan 2 formas de trabajo:</p> 

<p align="justify">La primera ilustra una posible configuración del sensor de ECG BITalino para Einthoven Lead I en la clavícula y la cresta ilíaca. El electrodo positivo (rojo) está ubicado en la clavícula izquierda y el electrodo negativo (negro) en la clavícula derecha. La referencia (REF) en blanco se sitúa en la cresta ilíaca.</p>

| Referencia pose | Pose laboratorio |
| :---:         |       :---: |
| ![r1](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/85925c04ed07c7661797cc706e65e8a37b702930/Images/Lab4/ref1.JPG) | ![ana](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/85925c04ed07c7661797cc706e65e8a37b702930/Images/Lab4/anapaint.jpg) 

<p align="justify">La segunda consta de colocar los electrodos en las muñecas. El electrodo positivo en la muñeca izquierda, el negativo en la muñeca derecha y la referencia en la cresta ilíaca.</p>

| Referencia pose | Pose laboratorio |
| :---:         |       :---: |
| ![r2](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/85925c04ed07c7661797cc706e65e8a37b702930/Images/Lab4/ref2.JPG) | ![manuel](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/85925c04ed07c7661797cc706e65e8a37b702930/Images/Lab4/manuelpaint.jpg) 

Para recibir la señal de ECG más cualitativa y distinguir todos los complejos PQRS entre sí, los electrodos deben colocarse cerca del corazón en el tórax.

### Metodología
<p align="justify">Se procederá a detallar los pasos realizados durante el desarrollo del laboratorio:</p>

   1. Se establece la conexión de los electrodos superficiales al cuerpo del voluntario de acuerdo a como ha sido detallado anteriormente, con el fin de obtener la señal ECG.
   2. Se procede a la conexión vía Bluetooth del BiTalino con la computadora, eligiéndose el canal (en el caso de ECG es canal 2).
   3. Se realiza la medición de las señales ECG en el software OpenSignals. 
   4. Se establecen las variaciones en la toma de muestras:

             a. Estado de reposo.
    
             b. Conteniendo la respiración durante la grabación por 30 segundos.
    
             c. Conteniendo la respiración durante 1 minuto antes de iniciar la grabación.
    
             d. Después de haber realizado ejercicio dinámico durante 5 minutos.
      
   5. Se exporta la data de la señal para poder trabajarla con lenguaje Python.
### Video de señal 

En este apartado se muestran los videos tomados de la experiencia.

<p align="justify">* En el siguiente video se puede apreciar la conexión realizada a nuestra primera voluntaria y la señal en OpenSignals:</p>

<div align="center">
 
https://user-images.githubusercontent.com/112776840/231618914-66f3d1f1-3933-498b-9900-fd5bc1ee13d4.mp4</div>
 
<p align="justify">* En el siguiente video se puede apreciar la conexión realizada a nuestro segundo voluntario y la señal en OpenSignals:</p>


<div align="center">
 
https://user-images.githubusercontent.com/112776840/231617441-02dbf5d8-f1d0-44a4-80b0-941cba20b578.mp4</div>

<p align="justify">* En el siguiente video se puede apreciar la señal en OpenSignalsFluke resultante del dispositivo ProSim 4 Vital Signs Patient Simulator l:</p>

<div align="center">
 
https://user-images.githubusercontent.com/112776840/231617142-4a1971af-5ae0-406b-9d3f-806a9d6b91b8.mp4</div>
  
  
<p align="justify">* En el siguiente video se puede apreciar un ejemplo de ejercicio dinámico realizado para la toma de muestra.</p>z

<div align="center">
 
https://user-images.githubusercontent.com/112776840/231619183-9ec122a2-e994-4164-91b1-67aa8ff66fae.mp4</div>


### Gráficos OpenSignals
#### Plots con ondas PQRST indicadas
<p align="justify">En la siguiente gráfica podemos ver la ubicación de las ondas PQRST, los intervalos PT y QT, el segmento ST y el complejo QRS.</p>

#### ECG - Manuel (Sin respirar en intervalos 5-10 segundos)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231635174-ee69d09d-6c9b-4af7-a5ab-3f52c36c0e6e.png" align="center" width="400" height="300"/>
</p>

<p align="justify">Para las demás gráficas solo se indicará las ondas PQRST, y los intervalos, segmentos y complejos podrán señalarse en base a lo anterior.</p>

#### ECG - Manuel (Reposo)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231637999-bd3877e1-d19c-426d-a5c9-2ba52c1f8dd9.png" align="center" width="400" height="300"/>
</p>

#### ECG - Manuel (Luego de no respirar por 1 minuto)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231637682-2be86cf2-6622-49e6-80c8-2d6df674cd89.png" align="center" width="400" height="300"/>
</p>

#### ECG - Manuel (Luego de un ejercicio intenso)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231637918-d87e7e81-b2be-4918-8cb1-dab2cea620f3.png" align="center" width="400" height="300"/>
</p>

#### ECG - Ana Paula (reposo)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231638305-638e0661-87b2-43bf-9921-d48512b105ea.png" align="center" width="400" height="300"/>
</p>

#### ECG - Ana Paula (Sin respirar en intervalos 5-10 segundos)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231638854-96b3881d-ca3e-4bd8-a3e9-c6af244f5f7f.png" align="center" width="400" height="300"/>
</p>

#### ECG - Manuel (Luego de no respirar por 1 minuto)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231639548-7f64bd0a-aa7e-43d2-815f-227d6d263b7a.png" align="center" width="400" height="300"/>
</p>

#### ECG - Ana Paula (Luego de un ejercicio intenso)
<p align="center">
<img src="https://user-images.githubusercontent.com/70824325/231639255-636a9696-e5bf-40c8-900a-74efa36d8c0f.png" align="center" width="400" height="300"/>
</p>
 
Es importante resaltar que significan cada una de estos segmentos de onda [9]:
- Onda P: Despolarizacion de las auriculas; primera onda del ciclo cardiaco, la primera parte corresponde a la despolarizacion de la auricula derecha y la final a la despolarizacion de la auricula izquierda, generalmnete tiene una duración menor a 0.1s y una amplitud maxima de 0.25mV.

- Complejo QRS: Despolarización de los ventrículos; compuesto por un subconjunto de ondas, su duración oscila entre 0.06 y 0.1s 
   * Onda Q: Primera onda del complejo, negativa.
   * Onda R: Primera onda positiva del complejo.
   * Onda S: Tercera onda, onda negrativa.
   
- Onda T: Repolarización de los ventrículos; lo normal es que sea positiva; sin embargo, en obesos, niños y mujeres puede ser negativa.

### Resumen y explicación final
Se realizó la medición de la señal electrocardiográfica en 3 situaciones distintas, en estado de reposo, de aguante de
respiración y despues de actividad física. Se obtuvieron dichas gráficas para dos voluntarios de prueba y del generador de
señales fisiológicas proporcionado.
Uno de los aspectos más importantes es la colocación de los electrodos sobre el cuerpo, se decició adoptar ambas
posiciones sugeridas en el manual de uso de “Bitalino” en uno de los voluntarios [5]

 * Reposo: Durante esta etapa se pudieron observar los picos QRS correspondientes a la despolarización ventricular, la
señal fue estable en esta segunda derivada con los normales (70 a 80 latidos por minuto) [6], sin embargo, si se puede
destacar algo es que en intensidad no fueron tan fuertes como la señal leída con el generador de señales fisiológicas. Se
intuye que esto puede ser debido al no uso de gel conductor que tiene la función de reducir la resistencia entre la piel y el electrodo o una colocación poco precisa de estos sobre el cuerpo.

* Aguante de la respiración: Se procuró iniciar la medición desde un punto neutro y que comience la inhalación justo al
inicio, luego de 20 segundos aproximadamente se dio la exhalación para observar como reaccionaba la señal. Durante la
etapa de inhalación y alrededores se pudo observar un aumento ligero de la frecuencia cardiaca, lo cual es coincidente
con lo que se estipula en [6], en la etapa de aguante de la respiración se empezó a ver un comportamiento ligeramente
sinusodal entre las zonas T y P de la señal (correspondiente a la repolarización ventricular), esto también se expandió
hacia algunas ondas QRS provocando una deformación. Este comportamiento snusoidal podría deberse a que la
compañera a veces tenía que hacer un sobre esfuerzo al aguantar la respiración lo que daría un resultado similar a como
si tuviera disnea con esfuerzo, esta característica puede producir sinusoidalidad en la señal [7]

* Efecto del movimiento: La principal caracerística fue la aceleración el ritmo cardiaco, aproximadamente un número
mayor a las 120 por minuto (60 por medio minuto que duró la adquisición). Fue disminuyendo un poco ya que luego del
ejercicio vigoroso se tomó un tiempo para volver a conectar los electrodos del “Bitalino”. Nuevamente las señal fue similar
en frecuencia a la observada con el generador de señales, pero en menor intensidad, atribuido a las mismas causas que
en el caso de reposo [8] 

Como observación adicional se menciona que se vieron ondas similares en ambos posicionamientos de electrodos (tanto
en muñecas como en las clavículas), aunque en el primero de los casos está el inconveniente de tener que mantener los
electrodos a la altura del corazón, lo que se intuye que podría haber dado lugar a alguna clase de ruido indeseado.

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

### Gráficos en Python
A partir del procesamiento realizado en python pudimos obtener los siguinetes graficos, tanto para los dos alumnos y para el simulador:

* Alumna 1 (Ana Paula):

| Lectura en reposo | Lectura durante aguante de respiración | Lectura tras aguante de respiración | Lectura despues de realizar movimientos |
| :---      |   :---:  |   :---:  |       ---: |
| ![ana1](https://user-images.githubusercontent.com/70769712/231648164-620226eb-f2aa-4940-9f3c-a18be4696473.jpeg) | ![ana2](https://user-images.githubusercontent.com/70769712/231648211-1a37d70e-250c-4f31-bd77-8cdfd733d53d.jpeg) | ![ana3](https://user-images.githubusercontent.com/70769712/231648216-9c02a70e-0eb5-4da7-9d89-cbb42013f0c4.jpeg) | ![ana4](https://user-images.githubusercontent.com/70769712/231648219-01e06174-d14e-4283-a417-b7365044677e.jpeg) |

* Alumno 2 (Manuel):

| Lectura en reposo | Lectura durante aguante de respiración | Lectura tras aguante de respiración | Lectura despues de realizar movimientos |
| :---      |   :---:  |   :---:  |       ---: |
| ![manuel1](https://user-images.githubusercontent.com/70769712/231648719-b135046d-ca96-43ab-8df5-4355ad88388a.jpeg)| ![manuel2](https://user-images.githubusercontent.com/70769712/231648754-1956c736-b27c-419e-8f70-b27e2e9786b9.jpeg)| ![manuel3](https://user-images.githubusercontent.com/70769712/231648748-f1eb83d0-e9ec-4ef7-8775-eb02515ebe56.jpeg)| ![manuel4](https://user-images.githubusercontent.com/70769712/231648751-fa93ba2f-3f85-4f5e-bab3-77481e0f698b.jpeg) |
 
* Simulador

| Lectura | 
|   :---:  | 
| ![simulador](https://user-images.githubusercontent.com/70769712/231648993-93665359-6cbd-4b23-b9c8-d2c53180c01e.jpeg) |
## Bibliografía

[1]W. Uribe, M. Duque, L. Medina, J. Marín, J. Enrique Velásquez, and J. Aristizábal, “ELECTROCARDIOGRAFÍA BÁSICA.” Available: https://www.siacardio.com/wp-content/uploads/2015/01/ECG-Capitulo-1-Conceptos-b-%C3%ADsicos.pdf

[2]Farré Antonio López and C. M. Miguel, Libro de la Salud cardiovascular del hospital clínico san carlos Y la fundación BBVA. Barcelona: Fundación BBVA, 2009. 

[3]“BITalino (r)evolution User Manual.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2021/11/bitalino-revolution-user-manual.pdf

[4]“BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” support.pluxbiosignals.com. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/ (accessed Apr. 13, 2023).

[5] “BITalino (r)evolution Lab Guide.” Available: https://support.pluxbiosignals.com/wpcontent/uploads/2022/04/HomeGuide2_ECG.pdf

[6] “Relación del electrocardiograma con la respiración y el pulso | Manual de laboratorio de fisiología, 6e | AccessMedicina
| McGraw Hill Medical,” Mhmedical.com, 2015. https://accessmedicina.mhmedical.com/content.aspx?
bookid=1722&sectionid=116885435 (accessed Apr. 12, 2023).

[7] Enero-Febrero, ActA MédicA coloMbiAnA, vol. 41, 2016, Accessed: Apr. 12, 2023. [Online]. Available:
http://www.scielo.org.co/pdf/amc/v41n1/0120-2448-amc-41-01-00074.pdf

[8] “Para qué se utiliza el gel conductor | Sisneo Bioscience,” Sisneo Bioscience, Jan. 25, 2023. https://sisneo.com/paraque-se-utiliza-el-gelconductor/#:~:text=Y%20el%20gel%20conductor%20permite,precisi%C3%B3n%20de%20los%20resultados%20obtenidos.
 (accessed Apr. 12, 2023).

[9]Ondas del Electrocardiograma By  Container: My-ekg.com Year: 2018 URL: https://www.my-ekg.com/generalidades-ekg/ondas-electrocardiograma.html
