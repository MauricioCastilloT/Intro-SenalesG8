# Electroencefalograma

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Electroencefalograma](#electroencefalograma)
  * [Conexión usada](#conexión-usada)
  * [Metodología](#metodología)
  * [Video de señal](#video-de-señal)
  * [Gráficos de las tomas](#gráficos-de-las-tomas)
  * [Resumen y explicación final](#resumen-y-explicación-final)
  * [Archivos](#archivos)
  * [Gráficos en Python](#gráficos-en-python)
* [Bibliografía](#bibliografía)

## Objetivos:

Obtener señales EEG a través del BITalino y de un EEG Headset comparando señales al realizar diferentes actividades.

## Materiales y equipos:

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
| OpenBCI GUI  |   Ultracortex EEG Headset  |       1      |
|       -      |      Laptop     |       1      |

</div>
* El Kit de BiTalino incluye la placa BiTalino, una bateria y electrodos junto con dos cables de 3 y 2 hilos.

## Entregable: 
### Electroencefalograma
<p align="justify">Un electroencefalograma (EEG) es un estudio que mide la actividad eléctrica en el cerebro mediante electrodos colocados sobre el cuero cabelludo o cercano a la zona superior de la cabeza. Las neuronas cerebrales se comunican a través de impulsos eléctricos y están activas todo el tiempo, y esta actividad se manifiesta como líneas onduladas en un registro electroencefalográfico. [1]</p>

### Partes del cerebo y como afecta la conexión 
<p align="justify">El cerebro consiste de cuatro lóbulos principales, como se observa en la Figura 1, que son el lóbulo frontal (vista en naranja), el temporal (vista en verde), el parietal (vista en azul - celeste) y el occipital (vista en amarillo) [2]. En cada lóbulo ocurren diferentes procesos, con lo cual cada uno cumple una función diferente.</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/233761001-7780a247-1c86-453f-b889-e15214b57f9b.png" align="center"/></p>
<p align="center">Figura 1. El cerebro y sus lóbulos con sus respectivas funciones. Recuperado de [2]</p>

<p align="justify">El lóbulo frontal es el responsable de movimientos voluntarios, toma de decisiones, pensamientos, procesos cognitivos y es nuestro centro de personalidad. El lóbulo temporal es el responsable del procesamiento sensorial, memoria a largo plazo, memoria visual, la emoción y lenguaje. El lóbulo parietal es responsable de unir la información de fuentes del entorno como el ambiente y su relación con nuestro cuerpo, como la coordinación de las manos cuando se agarra un objeto. Finalmente, el lóbulo occipital es el responsable del procesamiento visual [3][4].</p>


### Tipos de onda en EEG 
<p align="justify">Las ondas cerebrales son de baja amplitud y el caso del cerebro humano estamos hablando de microvoltios y tambien diferentes tipos de frecuencias, siendo unas mas rápidas y otras mas lentas. Segun la frecuencia podemos clasificar a las ondas cerebrales [10]:</p> 

- Onda delta: Se encuentra en el tango de 0.5Hz a 4Hz y la amplitud varia. Esta onda esta asociada al estar en un sueño profundo o despertar, se suele confundir con artefactos del ceullo o mandibula.
- Onda Gamma: Este es un tipo de señal con mayor frecuencia, contando rangos de 35Hz a 200-400Hz; ene ste caso, este tipo de onda refleja como se maneja la conciencia.
- Onda Mu: Rangos de 8Hz a 12Hz, asociada con actividades motoras, disminuye con el movimeitno o intencion de movimietno.
- Onda Tetha: Localizada entre los 4Hz a 7Hz y suele aparecer al encontarse en situaciones de estres emocional, como frustracion y decepcion; sin emabrgo, tambien esta asociada a la inspiracion creativa y meditacion.
 
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
Acerca de la señal, se optó por obtener señales electroencefalográficas (EEG).</p>

<p align="center"><img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/6b0bf88c4170eed2da41aea33c30c4093b5a2a31/Images/bitalinomanual.JPG" width="600" height="300"></p>

<p align="justify">Para la realización de la conexión usamos las posiciones indicadas en <b>BITalino (r)evolution Home Guide EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS for EEG</b>[4]. Dentro de la cual se nos menciona 1 forma de trabajo:</p> 

<p align="justify">La primera ilustra una posible configuración del sensor de EEG BITalino. El electrodo positivo es colocoda en la parte superior de la ceja izquierda cercana a la zona de la frente. El electrodo negativo se ubica en la misma zona pero de la ceja derecha. La referencia (REF) se ubica en una zona neutral, como un hueso detrás de la oreja.</p>

| Referencia pose | Pose laboratorio |
| :---:         |       :---: |
| ![r1](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/624e2ff1a5eae69ac5075c102ef8fd81750d7ddb/Images/Lab5/eeg.JPG) | ![FLASH](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/818241d478e871f1c2978a312cf882606b7b47bd/Images/Lab5/conexionfMARCADO.jpg) 


### Metodología
<p align="justify">Se procederá a detallar los pasos realizados durante el desarrollo del laboratorio:</p>

   1. Se establece la conexión de los electrodos superficiales al cuerpo del voluntario de acuerdo a como ha sido detallado anteriormente, con el fin de obtener la señal EEG.
   2. Se procede a la conexión vía Bluetooth del BiTalino con la computadora, eligiéndose el canal (en el caso de EEG es canal 3).
   3. Se realiza la medición de las señales EEG en el software OpenSignals. 
   4. Con el uso de Ultracortex EEG Headset y el entorno OpenBCI GUI se realiza otra toma de muestras.
   5. Se establecen las variaciones en la toma de muestras:

             a. Estado de reposo.
    
             b. Cerrando y abriendo los ojos en intervalos de cinco segundos.
    
             c. Resolviendo un problema dificil de matemática.
    
             d. Respondiendo preguntas de historia.
      
   5. Se exporta la data de la señal para poder trabajarla con lenguaje Python.
 
### Video de señal 

En este apartado se muestran los videos tomados de la experiencia.

#### BITalino 

<p align="justify">* En el siguiente video se puede apreciar la conexión realizada a nuestro voluntario en el primer estado:</p>

<div align="center">
 
https://user-images.githubusercontent.com/70769712/233762148-737dd206-d527-4744-b04a-70c511b85b84.mp4
</div>

<p align="justify">* En el siguiente video se puede apreciar la conexión realizada a nuestro voluntario en el segundo estado:</p>

<div align="center">
 
https://user-images.githubusercontent.com/70769712/233763466-6ababfc7-082d-4401-b916-6f9c2b00f3f4.mp4
 </div>
 
 #### Ultracortex EEG Headset
 <div align="center">
 
https://user-images.githubusercontent.com/70769712/233763466-6ababfc7-082d-4401-b916-6f9c2b00f3f4.mp4](https://user-images.githubusercontent.com/70824325/233794497-7be2c371-c952-49c5-a993-60667b942ba9.mp4)
 </div>


### Gráficos de las tomas

#### OpenSignals

| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Reposo**   | ![arduino33](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/3dd153ac61a859f4cd9374ee4898bf0d9cb095e1/Images/Lab5/tranquilo1JPG.JPG)  | 
| **Abriendo y cerrando los ojos, cda 5 segundos**  | ![BIT](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/3dd153ac61a859f4cd9374ee4898bf0d9cb095e1/Images/Lab5/ojos.JPG)        | 
| **Reposo de nuevo**   | ![arduino33](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/3dd153ac61a859f4cd9374ee4898bf0d9cb095e1/Images/Lab5/relajadoagain.JPG)  | 
| **Resolviendo matemática** |  ![kitw](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/0c09ea531537de5d057b5d8d4419008413952872/Images/Lab5/matematicaopen.JPG) |
| **Respondiendo historia** |  ![fluke](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/3dd153ac61a859f4cd9374ee4898bf0d9cb095e1/Images/Lab5/extra.JPG) |


#### OpenBCI GUI
| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Reposo**   | ![arduino33](https://user-images.githubusercontent.com/70824325/233792752-26e1e667-597d-4732-a2e2-6a3510c2bd31.JPG)  | 
| **Resolviendo matemática**  | ![BIT](https://user-images.githubusercontent.com/70824325/233792901-65b8b65d-9206-4ef0-810d-2e2685bcae7f.JPG)        | 
| **Respondiendo preguntas de historia** |  ![fluke](https://user-images.githubusercontent.com/70824325/233792914-99aa1a87-d8ef-482d-81e8-26ff6a855d6b.JPG) |

### Resumen y explicación final 
 
#### Ojos cerrados y relajado:
<p align="justify">Durante esta fase se pudieron observar ondas con ritmo alfa bajas con oscilaciones entre 8 y 12Hz , este estado se asemeja mucho a la fase 1 del sueño no REM y la vigilia con ojos cerrados [5]. Estas señales menionadas están relacionadas con la función motora y sensorial, las cuales no llegan a reducirse hasta ondas beta ya que aún hay estímulos externos como ruido y luz penetrante. Durante la adquisición el voluntario manifestó una ligera comezón y haber estado haciendo un leve esfuerzo mental en concentrarse en mantener los ojos cerrados y sin movimiento, lo cual a su vez generaba algunas ondas de mayor intensidad. Al escuchar alguna voz desde el exterior dirigida hacia él se notó un aumento en la frecuencia y amplitud.
Existe también casi ninguna señal de la corteza visual primaria que se halla bastante inactiva al no recibir estímulo externo, aún así debería mantenerse algo actica ya que el voluntario no se encuentra aún en ninguna de las fases de sueño, adicionando también que esta corteza está en la zona occipital y la medición fue realizada desde una posición frontal.</p>

#### Ojos cerrados y abiertos (ciclos de cinco segundos):
<p align="justify">Durante estos ciclos se pudo observar dos tipos de ondas, durante la fase de ojos cerrados se manifestaron ondas de ligeramente más amplitud y más frecuencia como se ve en la imagen. Estas ondas eran interrumpidas principalmente por la acción de abrir o cerrar los ojos, las ondas alfa suelen suprimirse al abrir los ojos [2], y también se manifestó más actividad relacionada con lo que se podría captar con un electroculograma, el cual mide el movimiento de los músculos del ojo, las señales de aumento de voltaje es correspondiente con lo que se ve en cerebros donde se realiza la misma prueba [5]. Las ondas durante los ojos abiertos corresponden tambien a ondas alfa de vigilia aunque se demoran más en estabilizarse debido a los nuevos impulsos recibidos por la corteza visual primaria y al movimiento involuntario de los ojos al seguir nuevas luces.</p>

#### Resolviendo problemas de matemática:
<p align="justify">En esta fase se manifestaron las mayores señales de estrés y aumento de frecuencia y amplitud de ondas al mismo tiempo, aquí se observan ondas theta mejor captadas por la actividad frontal del cerebro relacionado a la realización de actividades mentales, esto combinado con ligeros aumentos de amplitud ligados a movimiento de los musculos de los ojos [8]. Se perfila que la razón por las que las ondas theta fueron tan elevadas fue por que el voluntario estuvo intentando de manera vaga realizar el ejercicio matemático desde unos minutos antes de la adquisición, según [9] hay más probabilidades de ondas theta si es que el voluntario ya manifestaba actividad cerebral leve previamente, además la concentración y estrés aplicado fueron procesadas por las regiones frontales corticales, las cuales fueron más cercanas al punto de adquisición señalado por la guía bitalino [2].</p>
 
### Archivos
En Bitalino se procesó distintos archivos en Python del voluntario como se mencionó anteriormente:

* Lectura en estado de reposo.    
* Lectura cerrando y abriendo los ojos en intervalos de cinco segundos.    
* Lectura resolviendo un problema dificil de matemática.    
* Lectura respondiendo preguntas de historia.
 
- [Lectura en reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electroencefalograf%C3%ADa/lineabase1.ipynb)
- [Lectura cerrando y abriendo los ojos](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electroencefalograf%C3%ADa/ciclodeojos.ipynb)
- [Lectura resolviendo matemática](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electroencefalograf%C3%ADa/resoluciondejercicio.ipynb)
- [Lectura respondiendo historia](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electroencefalograf%C3%ADa/ejercicioextra.ipynb)

En OpenBCI:
- [Lectura del OPENBCI](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/main/IBS%20/Laboratorios%20/Electroencefalograf%C3%ADa/OpenBCI.ipynb)

### Gráficos en Python
A partir del procesamiento realizado en python pudimos obtener los siguinetes graficos, tanto para los dos alumnos y para el simulador:

* Alumno (Sebastian):

| Lectura en reposo | Lectura cerrando y abriendo los ojos | Lectura resolviendo matemática | Lectura respondiendo historia|
| :---      |   :---:  |   :---:  |       ---: |
| ![image](https://user-images.githubusercontent.com/70769712/233763972-fad908fb-9cc9-4aec-a1f6-bf0676324065.png)| ![image](https://user-images.githubusercontent.com/70769712/233763988-052b952c-3748-4a36-8a2b-b9e2db96a2ac.png)| ![image](https://user-images.githubusercontent.com/70769712/233764000-31180aee-9895-44be-b44d-0fbcf78d1ec0.png)| ![image](https://user-images.githubusercontent.com/70769712/233764005-08b96c2f-a09d-4b2e-a88a-f049055ad5b2.png)|



#### OpenBCI GUI en Python
| Actividad                    | Señal       | 
| :---:                          |    :----:                   |  
| **Gráfica de 8 canales**   | ![openbciim](https://user-images.githubusercontent.com/70824325/233794314-f7eafec2-8154-4e35-9ad0-63d8a0735aaf.png)  | 

### Bibliografia 
[1] “Electroencefalografía (EEG) - Mayo Clinic,” Mayoclinic.org, 2022. https://www.mayoclinic.org/es-es/tests-procedures/eeg/about/pac-20393875 (accessed Apr. 22, 2023). 

[2] “BITalino (r)evolution Lab Guide.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[3] “EEG (Electroencephalography): The Complete Pocket Guide - iMotions,” iMotions, Aug. 27, 2019. https://imotions.com/blog/learning/best-practice/eeg/ (accessed Apr. 22, 2023).
‌
[4] J. Lehtonen, EEG-Based Brain-Computer Interfaces. Elsevier BV, 2019. doi: https://doi.org/10.1016/c2017-0-01267-3.

[5] M. Cavelli, “Curso: "Neurobiología del Sueño"2017 Teórico: Actividad eléctrica cerebral durante el sueño.” Accessed: Apr. 19, 2023. [Online]. Available: http://www.fmed.edu.uy/sites/www.labsueno.fmed.edu.uy/files/eeg%20y%20sue%C3%B1o_Matias%202017.pdf

‌[6] FRANCISCO TEIXIDÓ GÓMEZ, “Dormido con un cerebro despierto,” Blogspot.com, 2016. http://biologiaemocional.blogspot.com/2016/08/dormido-con-un-cerebro-despierto.html (accessed Apr. 20, 2023).
‌
[7] R. García, “Anatomía y función de la corteza cerebral humana. Áreas de Brodman,” Neurorgs.net, Apr. 20, 2014. https://neurorgs.net/docencia/postgraduados/anatomia-y-funcion-de-la-corteza-cerebral-humana-areas-de-brodman/#1-_Corteza_visual_primaria (accessed Apr. 20, 2023).

‌[8] S. Mateo et al., “RESPUESTA FISIOLÓGICA Y PSICOLÓGICA RELACIONADA CON EL ESTRÉS SITUACIONAL BAJO EL USO DE TECNOLOGÍAS EN ADULTOS JÓVENES,” 2020. Accessed: Apr. 20, 2023. [Online]. Available: https://repository.urosario.edu.co/server/api/core/bitstreams/9fe72e7c-e388-490f-956e-86acee2f705f/content

‌[9] Umryukhin, E.A., Dzebrailova, T.D. & Korobeinikova, I.I. Spectral Characteristics of the EEG in Students with Different Levels of Result Achievement under the Conditions of Examination Stress. Human Physiology 30, 647–654 (2004). https://doi.org/10.1023/B:HUMP.0000049581.77570.9c

[10]“Extracción de características sobre señales EEG para detección de actividades mentalmotoras en sistemas BCI”https://inaoe.repositorioinstitucional.mx/jspui/bitstream/1009/155/1/RosasChG.pdf
