# Software del proyecto: Wearable to detect electromyographic changes in the trapezius muscle due to improper posture while sitting for long periods of time
El objetivo final del software del proyecto fue poder diseñar un algoritmo de clasificación capaz de diferenciar la actividad muscular emitida al realizar una buena y mala postura, para ello en primer lugar se realizó el filtrado de las señales.
## Filtrado de la señal:
### Librerías:
Las librerías utilizadas para este primer apartado fueron las siguientes:
![librerias](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/9bc96112-48df-4082-b435-00bd0482f20f)

* <b>Numpy:</b> NumPy es una biblioteca de Python muy utilizada en el ámbito de la ciencia de datos. Proporciona soporte para matrices y operaciones matemáticas eficientes, lo que la convierte en una herramienta fundamental para el procesamiento y análisis de datos numéricos.
* <b>Matplotlib:</b> Matplotlib es una biblioteca utilizada para la visualización de datos. Proporciona una amplia gama de funciones y herramientas para crear gráficos estáticos, diagramas, histogramas, dispersión entre otros.
* <b>Scipy:</b> La biblioteca SciPy se centra en el procesamiento de señales y la teoría de sistemas. Proporciona una amplia gama de funciones y herramientas para el análisis, la manipulación y la generación de señales.
### Procedimiento:
En primer lugar, se graficaron las señales correspondientes a la buena postura a fin de determinar si se trataba de una señal limpia o si contenía ruido que no nos permitiera analizar correctamente las características de dicha señal. Los resultados obtenidos nos dieron una señal con bastante ruido y en la que no se podía apreciar correctamente la actividad muscular del trapecio, a continuación podemos visualizar una de los gráficos correspondiente a una de las tomas realizadas para buena postura.
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/05cd630c-9d43-4a0f-b617-361ed84fe59f/>
</p>

Tras obtener estos resultados el siguiente paso a realizar fue el filtrado de dichas señales emg, para ello lo primero fue hacer un análisis en frecuencia de la señal, se hizo uso de la transformada fft para poder analizar las magnitudes correspondientes a cada frecuencia de la señal, los resultados los podemos observar a continuación
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/fe4cb098-098a-4dfe-9faa-7230ce140418/>
</p>
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/c5aacee4-35f8-4a54-a18e-30b44369dc5f/>
</p>
Como podemos observar de la gráfica hasta los 20 Hz podemos ver la presencia de magnitud en la señal, posterior a esta frecuencia la magnitud es 0. Por lo tanto podemos llegar a la conclusión de que la presencia de información relevante se encuentra hasta los 20 Hz y cualquier frecuencia posterior a esta solo genera un ruido en la señal.

Teniendo en cuenta este criterio se procedió a realizar el diseño de un filtro FIR pasa bajos con frecuencia de corte en 20 Hz. La ventana elegida para este filtro fue una ventana blackman de orden 37. Esta ventana fue escogida ya que  logra una atenuación más suave y gradual de las frecuencias no deseadas, lo que lleva a evitar alteraciones bruscas y distorsiones indeseables. Además permite una mejor separación de la información de interés, como los componentes de frecuencia relacionados con la actividad muscular, de las interferencias y el ruido no deseado
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/df46ad26-7b11-4d92-a27b-00c12cf09143 width="400" height="300"/>
</p>


<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/7a8f2aa1-b4bf-4dae-b60b-5d28889b07d6/>
</p>
Una vez obtenido el filtro se aplicó a cada señal emg de tanto buena como mala postura, los resultados de la señal correctamente filtrada los podemos observar a continuacion
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/86a04322-1f6d-4a81-a80a-3e6466b57c1b/>
</p>

## Modelo de clasificación:

### Librerías:
Las librerías utilizadas para este segundo apartado fueron las siguientes:
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/2c30d7a1-716e-41d9-889f-b64cdf34ae47/>

* <b>SkLearn:</b> Es una biblioteca de aprendizaje automático en Python muy utilizada. Esta proporciona una variedad de algoritmos y herramientas para realizar tareas de aprendizaje supervisado y no supervisado, así como evaluación de modelos y preprocesamiento de datos.
* <b>Pandas:</b> Pandas es una biblioteca de Python ampliamente utilizada para el análisis y manipulación de datos. Proporciona estructuras de datos de alto rendimiento y fáciles de usar, así como herramientas para la limpieza, transformación y análisis de datos tabulares.
</p>

### Procedimiento:
El procedimiento fue el siguiente, lo primero que se realizó fue importar los archivos de texto correspondientes a las señales filtradas y dividirlos en dos matrices diferentes, una que contuviera todas las señales correspondientes a la buena postura y otra con las de mala postura. A simple vista, tras el filtrado de la señal pudimos observar que una de las principales características que diferenciaba las señales era el valor promedio de su amplitud, así como los valores mínimos por los que atravesaba esta misma. Sin embargo estas características no eran suficientes para un modelo de clasificación por lo que se hizo el análisis de ciertos criterios que pueden ayudar a diferenciar entre señales EMG. Estas características y su porcentaje de importancia para un modelo de clasificación los podemos observar a continuación
<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/5208aac7-c76f-4c6e-b7e2-1fed21b49950 width="400" height="300"/>
</p>

<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/f65ea047-4eed-428f-bd17-563d018b9dba />
</p>


Tras el análisis de la característica de la señal se pudo evidenciar que aquellas con mayor porcentaje de importancia correspondían a las que describían en cierta medida la amplitud general de la señal. Entre estas se encuentra el RMS la cual nos proporciona una medida de la amplitud eficaz de la señal y la amplitud acumulada que vendría a ser la representación de la integral de la gráfica de cada señal. 


Una vez obtenidos las características más resaltantes que nos ayudarán al propósito del proyecto se realizó el diseño del algoritmo de clasificación random forest con aquellas señales que obtuvieron un score mayor a 0.05, para este algoritmo se seleccionó un test size del 25% y un random state de 42, medidas estándares en una buena práctica de este tipo. Con el 75% de la data se realizó el entrenamiento del programa y tras esto se diseñó una matriz de confusión para ver la clasificación de la data de testeo. Los resultados se pueden observar a continuación

<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/0253519a-30e5-45fc-a29c-e057bc09d6d2/>
</p>
Se pudo observar, de dicha matriz, que el modelo de clasificación lograba clasificar correctamente toda la data correspondiente a una buena postura, sin embargo se encontró una mínima complicación en la clasificación de la mala postura, ya que de 4 señales que debieron ser clasificadas como positivas, fueron clasificadas bajo los criterios de una mala postura

Finalmente se analizaron las características más importantes de un modelo de clasificación las cuales fueron el accuracy, el f1 score, la precisión, el recall y la especificidad del modelo. Los resultados los podemos apreciar en la siguiente imagen.

<p align="center">
<img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628819/c765c49a-6edd-44e6-9c90-d8dbe6bb3a83/>
</p>

De los resultados obtenidos podemos concluir que el modelo de clasificación presenta un buen rendimiento con un accuracy sólido y una alta precisión y especificidad. Sin embargo, se debe tener en cuenta la tasa de recall o sensibilidad, la cual es más baja, lo que implica que algunos casos positivos pueden estar siendo pasados por alto. Sin embargo estos resultados se muestran alentadores para poder continuar con el desarrollo de este proyecto y mejorar estas métricas en un futuro
