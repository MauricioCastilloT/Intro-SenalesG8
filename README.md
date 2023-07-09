#  <center>Wearable to detect electromyographic changes in the trapezius muscle due to improper posture while sitting for long periods of time</center>

# Detección de cambios electromiograficso en el msuculo trapecio por mantener mala postura por largos epriodos de tiempo

print("Bienvenidos al repositorio del grupo 8.")

Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades PUCP y UPCH semestre 2023-1. 
En esta oportunidad trabajaremos en un proyecto de procesamiento de señales de ECG.

## Tabla de contenidos:
* [Contexto](#contexto)
* [Estado del arte](#estado-del-arte)
* [Definición del problema](#definición-del-problema)
* [Impacto y limitaciones](#impacto-y-limitaciones)
* [Propuesta preliminar de solución](#propuesta-preliminar-de-solución)

## Contexto 
### En latinoamérica 
La prevalencia de la tendinitis aquiliana varía según la población y la actividad física. Se ha informado que afecta a aproximadamente el ,2% de la población en general, pero la incidencia aumenta a medida que aumenta la actividad física.
En atletas de alto rendimiento, la prevalencia puede ser tan alta como del 50%, especialmente en deportes que implican movimientos repetitivos del pie y la pierna, como el baloncesto, el voleibol y el fútbol, con una incidencia anual de un 7% a un 9%.
El incremento de sufrir tendinopatías se ha asociado a hombres, deportistas de élite, índice de masa corporal elevado, alto volumen de entrenamiento y flexibilidad disminuida (Janssen et al. 2018).
En nuestro país la tendinitis aquiliana es una problemática que aqueja tanto a deportistas, como a personas sedentarias…

No obstante, otra grave problemática a mencionar es el hecho de que en Perú son escasos los equipos de electromiografía tanto en Lima como en provincias, lo que ocasiona que no se obtenga el potencial completo de estudios de actividad muscular a comparación de en otros países [3]. Es por ello que en esta ocasión se busca trabajar con un kit Bitalino con la opción de EMG para poder apreciar que es posible la adquisición de data biológica con su respectivo reconocimiento de patrones de dicha enfermedad.

## Estado del arte
Las técnicas utilizadas para analizar la fatiga muscular y tendinitis utilizando EMG han evolucionado significativamente en los últimos años. Entre todas las técnicas, se han desarrollado diferentes prototipos y proyectos que utilicen EMG con las diversas técnicas, entre las cuales destacan las siguientes:
- “Method and apparatus for analysis of the surface electromyogram signal for estimating muscle fiber conduction velocity”: Esta patente utiliza la técnica de análisis de la frecuencia, la cual analiza la frecuencia de las señales EMG basándose en que la fatiga muscular se caracteriza por una disminución en la frecuencia de los impulsos eléctricos. Esta frecuencia es analizada a través del uso de ciertos indicadores como la mediana o mediante espectroscopía de frecuencias [X1].
- Physimax: Este producto utiliza índices de fatiga muscular para evaluar la fatiga muscular comparando la actividad muscular durante el ejercicio con la actividad muscular en reposo. Algunos índices son el de fatiga EMG, el de fatiga muscular integrado y el de fatiga muscular relativo [X2].
- Mio Slice: Este producto utiliza el análisis de la amplitud para evaluar la fatiga muscular basándose en que la fatiga muscular se caracteriza por una disminución en la amplitud de las señales EMG. Se puede analizar utilizando algunos índices como el de amplitud RMS o el de amplitud pico [X3].
- “Systems and methods for determining muscle fatigue”: Esta patente describe un método para evaluar la fatiga muscular utilizando el análisis de la forma de onda, la cual se basa en que la fatiga muscular se caracteriza por tener cambios en la forma de onda de las señales EMG, usando índices para lograr esta comparación como el índice de asimetría y de complejidad de la señal EMG [X4].

## Definición del problema 
### Planteamiento del problema:
La tendinitis es una lesión que impacta en el tendón de un músculo, resultando en su inflamación o degeneración posterior. Por lo general, la ubicación del dolor varía según el tendón afectado. Algunos ejemplos comunes de tendinitis incluyen la tendinitis del manguito rotador, la tendinitis rotuliana y la tendinitis aquílea que afecta al tendón de Aquiles. Se abordará esta última patología mencionada [S].

### ¿Por qué EMG en lugar de otra técnica?
La técnica de análisis por medio de EMG es no invasiva, con los sensores de superficie de piel no se necesita la inserción de electrodos dentro del músculo, lo cual reduce el riesgo de infección o lesiones.
Además, obtener la actividad muscular permite una evaluación objetiva de la función muscular, pues los resultados son reproducibles y cuantificables, permitiendo una comparación precisa de los datos entre personas.
Por otro lado, utilizar sensores de EMG permite una monitorización en tiempo real, brindando información sobre la actividad muscular. Esto brinda la capacidad a los profesionales de monitorizar la fatiga muscular y tendinitis durante la realización de actividades específicas y ajustar el tratamiento según se necesite.
Finalmente, la precisión del EMG para el reconocimiento de patrones de fatiga muscular asociados a tendinitis varía según los algoritmos utilizados, el número de canales EMG y otros factores. Sin embargo, es una técnica muy precisa para medir la actividad eléctrica de los músculos.
Por ejemplo, un estudio publicado en la revista Medicine and Science in Sports and Excercise [X10] evaluó la precisión de la EMG en la detección de tendinitis del codo de tenista en 24 diferentes pacientes. Los resultados de esta investigación mostraron que la EMG tenía una sensibilidad del 92% y una especificidad del 100%.

## Impacto y Limitaciones 

### Análisis de efectos y su impacto:

- Prevención de lesiones: El poder detectar a tiempo cuando la fatiga acumulada es lo suficiente como para generar una tendinitis aquiliana ayudara a realizar el descanso correspondiente para evitar dicha lesión asi como cualquier otro tipo de daño. El tratar la lesión desde su etapa inicial ayudara a que no se desarrolle más.

- Optimizar el rendimiento en atletas: el analisis de las señales emg ayudaran a los atletas y a sus preparadores fisicos a comprender que movientos son los más optimos y resultan menos lesivos durante la práctica. Además se puede ver cuales son los musculos que se encuentran en mejor estado, lo cual permitira diseñar entrenamientos especificos para reforzar otros músculos que sean mas probables de sufrir una lesión.
 
- Mejora en la precisión del diagnostico: actualmente lo mas comun para determinar una lesión es el uso de imagenes médicas donde se puede observar el estado del musculo o tendon, sin embargo con ayuda de las señales emg se puede tener una mejor interpretación del estado del músculo y que tan avanzada esta la lesión, midiendo su actividad electrica y comparandolas con un musculo sano.

- Mejor tratamiento: Gracias a la detección por señales emg podemos entender que movimientos son los que mas le cuestan al musculo y enfatizar el tratamiento específicamente para mejorar estos movimientos, ademas se podra hacer un mejor seguimiento de la recuperación al comparar constantemente con un musculo sano podremos ver que tanto ha mejorado.

- Adquisicion de nuevos conocimientos sobre la enfermedad: al investigar y trabajar con bases de datos amplias podemos reconocer nuevos patrones sobre esta o otras lesiones que aporten al campo de la ciencia en futuros proyectos.

### Limitaciones y cómo vencerlas:

#### A CORTO PLAZO: 
- Colocación de los electrodos: Protocolos de posicionamiento estandarizados, marcas en las posiciones exactas de los electrodos. Usar medidas anatomicas de las personas
Sensibilidad al ruido: Se producen interferencias y distorsiones en la señal, por el ruido electromagnetico.
- Carecemos de acceso a pacientes con tendinitis aquiliana: Mediremos la data en nosotros y nos basaremos en bibliografia que hable sobre patrones definidos pa la tendinitis 
	
#### A LARGO PLAZO:
Costo de dispositivos y materiales.
Validación del proyecto: comite de etica, varias pruebas .

## Propuesta preliminar de solución

Se propone adquirir señales en fatiga y en estado normal usando como parámetro de referencia la fuerza máxima de contracción normal del voluntario, para esto se obtendrán los datos mediante “Bitalino” usando su configuración de 4 electrodos.
Esta señal cruda será procesada en base a parámetros temporales y frecuenciales que permitan considerar las caracteristicas de un músculo fatigado continuamente a ritmos prolongados e intensos.
A futuro la presente investigación podría permitir el diseño de wereables con electrodos y dimensiones ad hoc para la zona a estudiar que permitan avisar a deportistas en rehabilitación cuando su músculo en tratamiento ha sobrepasado el límite fatiga saludable y corre riesgo de sufrir tendinitis en la zona cercana, esto en base a los datos que se recolecten del mismo paciente durante varios entrenamientos mediante Machine Learning.

La fatiga muscular suele dividirse en crónica y aguda, es esta segunda la que será estudiada ya que es cuya incidencia puede generar la mencionada tendinitis y la que representa de modo más notorio e incidental sus efectos en el electromiograma, además es esta la más ligada al músculo esquelético conectado a los huesos mediante los tendones. 
En aspectos visuales la fatiga se expresa como un aumento en la amplitud pico a pico de la señal, debido al incremento de fuerza y reclutamiento de unidades motoras para seguir manteniendo la misma por más tiempo, es esta la que detectamos como la primera fase de fatiga, la siguiente ocurre una vez que el músculo no puede compensar la fuerza se ve una disminución abrupta de la distancia pico a pico.

Otro factor destacable es que el impulso nervioso se vuelve más lento en las fibras musculares debido a la acumulación de productos como el ácido láctico que ralentizan estas señales. Esta ralentización se puede ver expresada como una compresión en la señal en el dominio de frecuencia con desplazamiento del espectro hacia las frecuencias bajas.

La señal será tratada con filtros pasa banda de entre para eliminar ruido en los extremos.
Los parámetros contemplados para el análisis son en el dominio temporal la distancia pico a pico y el Mean average value que suele ser usado según literatura, 

Los parámetros contemplados para el análisis son en el dominio temporal la distancia pico a pico y el Root Mean Square que mide el poder de la señal electromiográfica y que experimientará aumentos durante fatiga, y en el dominio frecuencial es la frecuencia mediana que es un modo robusto de obtener el promedio de todas las frecuencias.
