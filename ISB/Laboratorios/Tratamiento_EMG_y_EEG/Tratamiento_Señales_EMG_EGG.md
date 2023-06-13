# Tratamiento de señales de Electroencefalografía y Electromiografía

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
* [Aplicación de los algoritmos](#aplicación-de-los-algoritmos)
  * [EMG](#EMG)
  * [EGG](#EGG)
* [Archivos](#archivos)
* [Discusión](#discusión)
* [Conclusiones](#conclusiones)
* [Bibliografía](#bibliografía)

## Objetivos:

*  Diseño de filtros usando Datasets obtenidos.
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

<p align="justify">En el laboratorio pasado se realizó una tabulación de data, con el fin de analizar y visualizar de forma más precisa y ordenada las señales adquiridas anteriormente; en nuestro caso en particular, hemos decidido realizar este proceso en las señales adquiridas de EEG y EMG con ayuda de un BiTalino; el proceso llevado a cabo para la adquisicon de EEG y EMG se puede ver en los siguientes enlaces respectivamente:</p> 

 - [EGG lectura](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/ea8f4ceefb516e66659e69738df1bf52f3801594/IBS%20/Laboratorios%20/Electroencefalograf%C3%ADa/Electroencefalograf%C3%ADa.md)
 - [EMG lectura](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/fc5310b696935065cf14d9196ba395afc6d2fba1/IBS%20/Laboratorios%20/Electromiograf%C3%ADa.md)

<p align="justify">Por otro lado, tambien buscamos tabular y etiquetar la data con el fin con el fin de aplicar técnicas de machine learning de una forma mas eficiente en un futuro; ya que es eficiente para el reconocimietno de patrones en distintas señales [5].</p>

<p align="justify">En el presente laboratorio se realizará el filtrado de la señal antes mencionada, para lo cual se trabajará con técnicas de filtros. Para realizar este proceso usaremos un notebook de jupyter.</p>

## Aplicación de los algoritmos:

### EMG
Para las señaeles EMG se trabajó con la señal de reposo y el bicep contraído, a continuación veremos los resultados obtenidos:

### Señal original:

Señal en reposo:

![señalreposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/b7cbc7f0-0bc6-44a7-bf2e-ae5ccd820767)


Señal de bicep contraido:

![señalbicep](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/0665a340-fb46-48c2-986e-49a1c748a402)

### Filtrado de las señales:
Señal en reposo:

![filtrado_reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/f148c6cf-9a10-451a-bbe2-37dec2761810)


Señal de bicep contraido:

![filtrado_bicep](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/0e5f8b8d-c38d-4174-9b24-3e424a8bd6cb)


### Smooth signal:
Señal en reposo:

![smooth_reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/d28e0519-ab0e-4e1f-b863-eb1a05ae398b)


Señal de bicep contraido:

![smooth_bicep](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/ea1419ed-deef-4590-ae23-548aaa359fab)

#### Activación muscular:
Señal en reposo:

![activacion_reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/3f003887-a2f3-48cf-b765-1d7e3f9068f3)

Señal de bicep contraido:

![Activacion_bicep](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/ea0d5d48-228b-4a2d-a0ac-090ef8e18938)


### EGG
Para las señales EEG se trabajó con la señal en reposo y la señal resolviendo un ejercicio. A continuación los resultados: 

### Señal original

Señal en reposo:

![reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/b400f616-33b2-4160-8d4c-4f2615ef2670)

Señal resolviendo:

![resolviendo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/f31fd0a3-fc05-4184-a6b6-9b40a5327cfc)

### Señal filtrada

Señal en reposo:

![filtradoreposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/ff0a0a0b-0628-456d-a767-622e712876ca)

Señal resolviendo:

![filtradoresolviendo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/c44e2079-12fa-4ec6-aebb-dfd825a13630)

### Detección de ERP

Señal en reposo:

![erpreposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/91cca091-e14e-48d6-a55b-e30d5bc48ce1)

Señal resolviendo:

![erpresolviendo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/2de489af-ddfc-42d9-97c6-9f12184d165c)

### Extracción de banda alfa

Señal en reposo:

![bandareposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/045a9d01-28c9-4cca-8259-aa46fd7298ec)

Señal resolviendo:

![bandaresolviendo](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/fc300b1b-96ab-411c-96c0-45464747b298)

## Archivos:

Se procesaron distintos archivos en Python y se obtuvieron los siguientes códigos:
- [Señal EEG Resolviendo](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/f652f92bf96c31b30030f75cba0b21bb3ad763aa/IBS%20/Laboratorios%20/Tratamiento_EMG_y_EEG/Tratamiento_Se%C3%B1al_EEG/EEG_Lab9_resolviendo.ipynb)
- [Señal EEG Reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/f652f92bf96c31b30030f75cba0b21bb3ad763aa/IBS%20/Laboratorios%20/Tratamiento_EMG_y_EEG/Tratamiento_Se%C3%B1al_EEG/EEG_Lab9_reposo.ipynb)
- [Señal EMG Bícep](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/f652f92bf96c31b30030f75cba0b21bb3ad763aa/IBS%20/Laboratorios%20/Tratamiento_EMG_y_EEG/Tratamiento_Se%C3%B1al_EMG/EMG_LAB9_bicep.ipynb)
- [Señal EMG Reposo](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/f652f92bf96c31b30030f75cba0b21bb3ad763aa/IBS%20/Laboratorios%20/Tratamiento_EMG_y_EEG/Tratamiento_Se%C3%B1al_EMG/EMG_LAB9_reposo.ipynb)

## Discusión:

### SEÑALES EMG:

#### Adquisicion de señales EMG:

<p align="justify">La electromiografía,  es una metodología de registro y análisis de la actividad bioeléctrica de los músculos esqueléticos del cuerpo; usualmente es usada como técnica de diagnóstico para enfermedades neuromusculares [1].
Las señales que se obtienen de la electromiografía son producidas por el intercambio de iones a traves de las membranas de las fibras musculares debido a una contracción muscular; y las caracteristicas de las señales, como la amplitud y sus propiedades, tanto en el dominio del tiempo como de la frecuencia, dependen de factores tales como: el tiempo y la intensidad de la contracción muscular [2].</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/3e4baa05-1179-4f5e-aa78-83ad3d4dbf43" align="center" width="400" height="300"/>
</p>

Para el registro de las señales electromiográficas, se hizo uso de electrodos de superficie, los cuales son colocados en la superficie de la piel y son capaces de tomar registros poblacionales de la actividad bioeléctrica. El uso de estos electrodos es adecuado para el estudio de un promedio de actividad electrica de un músculo o grupos musculares [3].

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230244888-945e596a-8520-4f50-8796-6dcfc26b4fed.jpg" align="center" width="400" height="500"/>

#### Procesamiento de señales EMG:
 
<p align="justify">Por lo comentado anteriormente, el uso de las señales electromiográficas se ha convertido en un parámetro importante para la biomedicina a lo largo de los años. Por esto, es muy importante poder interpretar de manera correcta estas señales; para lo cual, en ocasiones, es necesario un previo procesamiento de las señales para poder obtener una mejor interpretación de las mismas, para este propósito, se usan diversos algoritmos y metodos para limpiar la señal requerida [1].</p>
 
 ### SEÑALES EEG:
 
 #### Adquisicion de señales EEG:
 
<p align="justify">La electorencefalografía es un método que permite el estudio de la actividiad eléctrica del cerebro mediante el posicionamiento de electrodos en el cuero cabelludo. Las neuronas cerebrales se comunican a traves de impulsos eléctricos y están activas todo el tiempo. 
Para la adquisión de señales, se hizo uso de electrodos de superficie ubicados en la zona de la frente, haciendo uso de la guía que proporciona BiTalino.</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/818241d478e871f1c2978a312cf882606b7b47bd/Images/Lab5/conexionfMARCADO.jpg" align="center" width="400" height="500"/>
 
#### Procesamiento de señales EMG:
 
Al igual que las señales de EMG, las señales de ECG  son importantes para la ingenieria biomédica y la medicina, esto debido a la amplia gama de diagnósticos que permiten identificar con la actividad neuronal como [4]:
 
- Tumores cerebrales
- Daños cerebrales por lesiones en la cabeza
- Disfunciones cerebrales que pueden tener diversas causas (encefalopatía)
- Trastornos del sueño
- Inflamación del cerebro (encefalitis herpética)
- Accidente cerebrovascular
- Trastornos del sueño
- Enfermedad de Creutzfeldt-Jakob
 
## Conclusiones:
### EMG
 -  <p align="justify">En el laboratorio se realizó el analisis de las señales  de EMG con un dataset previo; se busco identificar la actividad muscular segun los movimientos realizados y el músculo en cuestión; por esto el análisis de las señales EMG tiene una gran relevancia en el campo de biomecánica, ya que proporciona información detallada sobre la contracción muscular, la fatiga, la coordinación y otros aspectos relacionados con la función muscular y como se relaciona de esta forma con los movimientos que se realizan. Para lograr un tratamiento óptimo de una señal EMG, es necesario llevar a cabo un preprocesamiento, la extracción de características y la aplicación de métodos de análisis y clasificación adecuados. Estas etapas son fundamentales para obtener datos valiosos utilizados en el diagnóstico y tratamiento de trastornos neuromusculares, así como en otras áreas de la medicina e investigación.</p>
 
 ### EEG
 - <p align="justify">En el laboratorio se realizo un análisis de las señales EEG obtenidas con anterioridad, se aplicaron diversos filtros para identificar ritmos cerebrales, como los delta, alpha, beta, gamma. El tratamiento de señales EEG permite monitorear la actividad cerebral en tiempo real y puede diagnosticar trastornos neurológicos. También se utiliza en interfaces cerebro-computadora para ayudar a personas con discapacidades físicas. El análisis de señales EEG revela patrones relacionados con respuestas cognitivas y emocionales. Sin embargo, existen desafíos como el ruido y artefactos en las señales, la complejidad de interpretación y la incomodidad de los electrodos.</p>
 
## Bibliografía:

* [1] L. Gila, A. Malanda, Rodríguez Carreño, I, Rodríguez Falces, J, and J. Navallas, “Métodos de procesamiento y análisis de señales electromiográficas,” Anales del Sistema Sanitario de Navarra, vol. 32, pp. 27–43, 2023, Accessed: Jun. 04, 2023. [Online]. Available: https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272009000600003
‌
* [2] A. Meneses, “Electromiografía (EMG) - dalcame,” Dalcame.com, 2023. http://www.dalcame.com/emg.html (accessed Jun. 04, 2023).
‌
* [3] J. L. Correa-Figueroa, E. Morales-Sánchez, J. A. Huerta-Ruelas, José-Joel Gonzalez-Barbosa, and C. R. Cárdenas-Pérez, “SEMG signal acquisition system for muscle fatigue detection,” Jan. 2016, doi: https://doi.org/10.17488/rmib.37.1.4.

* [4] “Electroencefalografía (EEG) - Mayo Clinic,” Mayoclinic.org, 2022. https://www.mayoclinic.org/es-es/tests-procedures/eeg/about/pac-20393875 (accessed Jun. 04, 2023).
‌
‌
‌
