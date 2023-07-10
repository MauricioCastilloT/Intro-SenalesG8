# Wearable to detect electromyographic changes in the trapezius muscle due to improper posture while sitting for long periods of time
# Detección de cambios electromiograficso en el msuculo trapecio por mantener mala postura por largos epriodos de tiempo

```python
print("Bienvenidos al repositorio del grupo 8.")

Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades PUCP y UPCH semestre 2023-1. 
En esta oportunidad trabajaremos en un proyecto de procesamiento de señales de EMG.
```
Para conocer más sobre el equipo desarrollador ingresar al siguiente [enlace](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/0d16ce2035884b2f71158d1f6cc3fa72c79879fb/ISB/Laboratorios/SobreNosotros.md)
## Tabla de contenidos:
* [Resumen](#resumen)
* [Introducción](#introducción)
* [Motivación](#motivación)
* [Principales hallazgos](#principales-hallazgos)
* [Bibliografía](#bibliografía)

## Resumen 

<p align=justify>La mala postura es una de las razones principales de dolor de espalda, tanto es así que de llegar a mantenerse este hábito por mucho tiempo se pueden generar cambios estructurales en la espalda y el cuello, esto implica incluso un cambio de forma muscular gracias  a la debilitación de los mismos. Una buena postura se caracteriza por garantizar un equilibrio estable, un bajo consumo de energía y un mínimo estrés en las estructuras anatómicas, en este caso aquella que se analizará será el trapecio.</p>

<p align=justify>Dicho músculo ubicado en la espalda desempeña un papel importante en mantener la postura erguida y participa en movimientos como la flexión lateral y rotación de la cabeza, así como la elevación y depresión de los hombros. Esta actividad es medida mediante electromiografía, estudio que evalúa la actividad bioeléctrica generada durante las contracciones musculares, en este proyecto se utiliza esta técnica en su modo superficial para observar el comportamiento del trapecio transversalis (zona media del trapecio), ya que ese es el segmento que controla la mayor parte el movimiento cervical y dorsal.</p>

<p align=justify>El presente proyecto pretende desarrollar un prototipo de wearable para detectar los patrones electromiográficos debido a una postura incorrecta al estar sentado durante períodos prolongados. Esto usando recursos como impresión 3D y microcontrolador ESP32.</p>


## Introducción

<p align=justify>El sistema muscular de la anatomía humana consta de un conjunto de cientos de músculos, tanto esqueléticos como viscerales que realizan movimientos voluntarios e involuntarios respectivamente; el sistema muscular comprende tres tipos de músculos,  esqueléticos, lisos y cardíacos [1].</p>

<div align="center">
  
| Músculos esqueléticos | Músculos lisos | Músculos cardíacos|
|-----------------------|----------------|------------------|
| ![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/0eca334d-5393-4a47-9e30-ba06e06b641e)|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/aa5d5e7d-7b18-40f7-8d99-e20fad612b7a)| ![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/f214e581-5279-4d49-9f12-56dbd013d9f0)|

</div>

<p align="center">
  <em>Tabla 1. Clasificación de los músculos </em>
</p>

### Músculo esquelético
<p align=justify>Los músculos esqueléticos están distribuidos a lo largo de todo el cuerpo donde tienen diferentes formas, tamaños y disposición de fibras; este tipo de músculos son los encargados del movimiento voluntario de los esqueletos axial y apendicular, también es el principal encargado de mantener la postura y posición corporal [2]. 
En la espalda hay una variedad de músculos que cumplen diferentes funciones; proporcionan soporte a la columna vertebral y el tronco, facilitan el movimiento del cuerpo, mantienen la postura erguida y asisten en la respiración; y se subdividen en músculos extrínsecos e intrínsecos [3]. El trapecio es un músculo extrínseco que se encuentra en la parte superficial de la espalda,  es amplio, plano y se extiende desde la región cervical hasta la parte torácica del tronco; este músculo desempeña un papel importante en la postura ya que ayuda a mantener la columna vertebral erguida y también participa en movimientos activos como la flexión lateral y rotación de la cabeza , la elevacion y depresión de hombros [4].</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/224a03a1-c934-4466-841d-1a3f4d9f178e"
width="325" height="350"/>
</p>

<p align="center">
  <em>Figura 1. Músculo trapecio </em>
</p>

### Postura
<p align=justify>La postura se puede definir como toda posición que determina el mantenimiento del equilibrio, mínimo consumo de energía y mínimo estrés de las estructuras anatómicas por las que está controlado [5], el mantener una buena postura es muy importante  para la salud; sin embargo, desarrollar un hábito de buena postura no es sencillo y la falta de corrección de la misma puede provocar, con el tiempo, consecuencias negativas duraderas en el sistema musculoesquelético del cuerpo e incluso en otros sistemas [6].</p>

<div align="center">
  
| Buena postura | Mala postura |
|-----------------------|----------------|
|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/9292cadc-5278-4f19-8dd3-cd8ab0afa260)|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/9b07bb4b-9c1b-460a-8cb2-f6e66d3fdce5)|

</div>

<p align="center">
  <em>Figura 2. Comparación de posturas </em>
</p>

<p align=justify>La fatiga muscular se presenta como una disminución en la habilidad para mantener un nivel específico de fuerza durante una contracción prolongada, así como la incapacidad para alcanzar el nivel de fuerza inicial en contracciones intermitentes; el estado de fatiga se caracteriza por alteraciones en la actividad eléctrica de los músculos [7] . Al mantener una mala postura, podemos provocar fatiga muscular, en especial cuando adoptamos posturas incorrectas durante largos periodos de tiempo, en particular durante posiciones estéticas nuestros músculos deben trabajar más para mantener el equilibrio. 
Para la identificación de fatiga usando electromiografía principalmente se observan los parámetros de: 
  
* <b>Amplitud pico-pico</b>, donde es anticipado que la señal aumenta en amplitud ya que los músculos intentan mantener la misma fuerza reclutando unidades motoras adicionales en respuesta a la fatiga. 
* <b>La media y mediana</b> del espectro de frecuencia.
* <b>La frecuencia</b> ya que la velocidad de conducción de fibra disminuye [7].</p>



### Electromiografia 
<p align=justify>Por otro lado, la electromiografía, es un estudio que evalúa la salud de los músculos, lo cual es posible debido a que las células nerviosas envían señales eléctricas a medida que se producen contracciones musculares. El análisis y el registro de esta actividad bioeléctrica muscular está orientada principalmente al diagnóstico de enfermedades neuromusculares. La adquisición de las señales puede realizarse por medio de electrodos intramusculares o superficiales; los electrodos superficiales son adecuados cuando se busca observar el comportamiento global muscular, realizar patrones de actividad temporal e identificar fatiga en uno o más músculos [8].</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/62f38fef-b5e2-4a2e-8fa8-dcc255b9e13a"
width="400" height="250"/>
</p>

<p align="center">
  <em>Figura 3. Electromiografía </em>
</p>

## Motivación
<p align=justify>De acuerdo con el Instituto Nacional de Seguridad y Salud Ocupacional (NIOSH) [9], existe un sólido respaldo de evidencia que establece una relación causal entre los movimientos repetitivos y los trastornos músculo-esqueléticos del cuello y los hombros. Asimismo, por estudios realizados se observó que aquellos individuos que pasaban más de ocho horas diarias sentados sin realizar actividad física presentaban un riesgo de mortalidad similar al asociado con la obesidad y el tabaquismo [10].  Además de los riesgos relacionados con el sistema musculoesquelético, se ha planteado una preocupación acerca del impacto del comportamiento sedentario en la cognición, lo cual podría afectar el desempeño de los trabajadores de oficina. Investigaciones recientes sugieren que existe una posible asociación negativa entre el comportamiento sedentario habitual y la función cognitiva [11]. Al considerar los efectos agudos, encontraron que realizar tareas durante períodos prolongados (90 minutos) de sedestación resultó en un menor rendimiento laboral. Además, el estado mental también ha sido examinado en estudios de laboratorio, donde se reportaron niveles más altos de fatiga durante la sedestación prolongada en comparación con otras posturas de trabajo [12]. Estudios de campo que compararon el sentarse con posiciones de trabajo sentado y de pie encontraron que el sentarse se asociaba con mayor fatiga y una percepción de menor nivel de energía, así como una disminución en la concentración y la productividad [13].</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/112776840/a460dd25-c98b-4759-95d2-536ad7a5b62f"/>
</p>
<p align="center">
  <em>Figura 4. Efectos de una incorrecta postura al sentarse </em>
</p>

<p align=justify>El NHS (Servicio nacional de salud) cita el dolor de espalda como la principal causa de enfermedad de larga duración en el Reino Unido, responsable de más de  15 millones de días de trabajo perdidos en el 2013 [14], mientras que en el 2018  se notificó que la cantidad de días de trabajo perdidos llegó a la suma de 264 millones en un solo año [15]. Estos y otros problemas de salud ergonómicos cuestan a Singapur 3.500 millones de dólares al año, según el Consejo de Seguridad y Salud en el Trabajo (WSH) [16].</p>

<p align=justify>Con el tiempo, una mala postura al sentarse puede provocar problemas como la escoliosis y lumbalgia, que aqueja a cerca del 80% de los adultos en algún momento de su vida. En EEUU suele costar a los estadounidenses al menos 50.000 millones de dólares en gastos sanitarios cada año. La mayoría de los casos de dolor de espalda son mecánicos o no orgánicos, lo que significa que no están causados por afecciones graves, como infecciones, traumatismos causados por un solo incidente o cáncer [17].</p>

<p align=justify>En Perú, EsSalud ha comunicado que el 70% de los trabajadores se vieron afectados por adoptar posturas corporales inapropiadas durante el periodo de la pandemia del Covid-19. Según expertos, los problemas posturales más comunes fueron los dolores cervicales causados por el uso prolongado de posturas inadecuadas frente a la computadora o laptop, así como la discrepancia entre la altura de la silla y la mesa, y la distancia incorrecta entre el teclado, el mouse y la pantalla [18].</p>

<p align=justify>Debido a los problemas antes mencionados se presenta la siguiente hipótesis: El diseño de un wearable que utilice electromiografía (sEMG) en el músculo trapecio permite la correcta detección de malas posturas al sentarse durante largos periodos de tiempo.</p>


## Principales hallazgos

<p align=justify>Tras realizar las adquisiciones correspondientes, se obtuvieron un total de 150 señales, las cuales se dividieron en 75 señales emg representantes de una buena postura y 75 señales emg representantes de una mala postura. El fin de obtener dichas señales fue poder diseñar un algoritmo de clasificación capaz de diferenciar la actividad muscular emitida al realizar ambos tipos de postura, para ello el primer paso a realizar fue el análisis y filtrado de la señal.</p>

<p align=justify>Una vez obtenido el filtro se aplicó a cada señal emg de tanto buena como mala postura, los resultados de la señal correctamente filtrada los podemos observar en las siguientes figuras:</p>


<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/112776840/6c943237-effe-4151-aa14-65bb90094da4"/>
</p>
<p align="center">
  <em>Figura 5. Señal EMG filtrada </em>
</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/112776840/2a0eeff0-070c-498d-ab8a-7b32f5901bad"/>
</p>
<p align="center">
  <em>Figura 6. Señal EMG filtrada </em>
</p>


<p align=justify>Los resultados nos dieron el indicio de una señal correctamente filtrada en donde se logró eliminar el ruido no deseado que no permitía analizar las características de las señales, podemos ver también que se mantuvo la amplitud de la señal tras aplicado el filtro así como los aparentes picos correspondientes a la presencia de actividad muscular.</p>

<p align=justify>Posteriormente se realizó el proceso de división de la información en matrices, en dicho proceso es que opta por analizar ciertos criterior que puedan ayudar a diferenciar entre señales EMG. Tras el análisis de la característica de la señal se pudo evidenciar que aquellas con mayor porcentaje de importancia correspondían a las que describían en cierta medida la amplitud general de la señal. Entre estas se encuentra el RMS.</p>

<p align=justify>Una vez obtenidos las características más resaltantes que nos ayudarán al propósito del proyecto se realizó el diseño del algoritmo de clasificación Random Forest con aquellas señales que obtuvieron un score mayor a 0.05, obteniéndose los siguientes resultados:</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/112776840/18002469-4700-48ef-a029-98a66aaae86c"/>
</p>
<p align="center">
  <em>Figura 7. Matriz de clasificación </em>
</p>


<p align=justify>Finalmente se analizaron las características más importantes de un modelo de clasificación las cuales fueron el accuracy, el f1 score, la precisión, el recall y la especificidad del modelo.</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/112776840/92e4955d-f92a-4658-9304-970c947fd380"/>
</p>
<p align="center">
  <em>Figura 8. Características del modelo de clasificación </em>
</p>



## Bibliografía

- [1] U. De Aprendizaje, Sistemas, A. Monografia, Sistema, M. Por, and Hermilo Sánchez Sánchez, “UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO FACULTAD DE CIENCIAS LICENCIATURA EN BIOLOGIA.” Available: http://ri.uaemex.mx/bitstream/handle/20.500.11799/107975/secme-10856_1.pdf?sequence=1‌
- [2] “Muscle Types | SEER Training,” Cancer.gov, 2023. https://training.seer.cancer.gov/anatomy/muscular/types.html (accessed Jul. 09, 2023).
- [3] C. Clinic, “Back Muscles: Anatomy and Function of Upper, Middle & Lower Back - Cleveland Clinic,” Cleveland Clinic, 2021. https://my.clevelandclinic.org/health/body/21632-back-muscles (accessed Jul. 09, 2023).
- [4] “Trapezius,” Physiopedia, 2022. https://www.physio-pedia.com/Trapezius (accessed Jul. 09, 2023).
- [5] F. Carini et al., “Posture and posturology, anatomical and physiological profiles: overview and current state of art.,” vol. 88, no. 1, pp. 11–16, Apr. 2017, doi: https://doi.org/10.23750/abm.v88i1.5309.
- [6] franklinpt, “La importancia de la postura para la salud musculoesquelética - Franklin Square Health Group,” Franklin Square Health Group, Oct. 20, 2020. https://franklinsquarept.com/postura-salud-musculoesqueltica/?lang=es (accessed Jul. 09, 2023).
- [7] J. M. Fernández, R. C. Acevedo, and C. B. Tabernig, “INFLUENCIA DE LA FATIGA MUSCULAR EN LA SEÑAL ELECTROMIOGRÁFICA DE MÚSCULOS ESTIMULADOS ELÉCTRICAMENTE,” Revista EIA, no. 7, pp. 111–119, 2023, Accessed: Jul. 09, 2023. [Online]. Available: http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S1794-12372007000100010
- [8] “Electromiografía y estudios de conducción nerviosa,” Medlineplus.gov, 2019. https://medlineplus.gov/spanish/pruebas-de-laboratorio/electromiografia-y-estudios-de-conduccion-nerviosa/ (accessed Jul. 09, 2023).
- [9] Salud, “Seguridad y Salud Ocupacional,” INSTITUTO NACIONAL DE SALUD, 2022. https://web.ins.gob.pe/es/acerca-del-ins/seguridad-y-salud-ocupacional (accessed Jul. 09, 2023).
- [10] “Riesgos de estar sentado: ¿es perjudicial estar sentado mucho tiempo?,” Mayo Clinic, 2022. https://www.mayoclinic.org/es/healthy-lifestyle/adult-health/expert-answers/sitting/faq-20058005 (accessed Jul. 09, 2023).
- [11] R. M. Baker, P. Coenen, E. K. Howie, A. Williamson, and L. Straker, “The Short Term Musculoskeletal and Cognitive Effects of Prolonged Sitting During Office Computer Work,” vol. 15, no. 8, pp. 1678–1678, Aug. 2018, doi: https://doi.org/10.3390/ijerph15081678.
- [12] Wennberg, P.; Boraxbekk, C.-J.; Wheeler, M.; Howard, B.; Dempsey, P.C.; Lambert, G.; Eikelis, N.; Larsen, R.; Sethi, P.; Occleston, J.; et al. Acute effects of breaking up prolonged sitting on fatigue and cognition: A pilot study. BMJ Open 2016, 6, e009630.
- [13] Davis, K.G.; Kotowski, S.E. Postural variability: An effective way to reduce musculoskeletal discomfort in office work. Hum. Factors 2014, 56, 1249–1261.
- [14] WP-Admin, “The High Cost of Bad Posture at Work | Joyful Living,” Joyful Living, Feb. 19, 2016. https://joyful-living.co/blog/employee-wellbeing/the-high-cost-of-bad-posture-at-work/ (accessed Jul. 09, 2023).
-‌ [15] Dr. Sherry McAllister, “Council Post: How To Curb Three Leading Productivity Killers: Lack Of Sleep, Poor Posture And Stress,” Forbes, Dec. 06, 2018. Accessed: Jul. 09, 2023. [Online]. Available: https://www.forbes.com/sites/forbesnonprofitcouncil/2018/12/06/how-to-curb-three-leading-productivity-killers-lack-of-sleep-poor-posture-and-stress/?sh=7d82b98b5b1b
- [16] Migration, “Ergonomics problems cost Singapore $3.5 billion a year,” The Straits Times, Mar. 27, 2014. https://www.straitstimes.com/singapore/ergonomics-problems-cost-singapore-35-billion-a-year (accessed Jul. 09, 2023).
- [17] Hartvigsen J et al. Low Back Pain Series: What Low Back Pain Is and Why We Need to Pay Attention. Lancet, June 2018; Volume 391, Issue 10137; p2356-2367.
- [18] “EsSalud alerta que problemas posturales se incrementó en un 70% durante la pandemia - Essalud,” Essalud, 2022. http://noticias.essalud.gob.pe/?inno-noticia=essalud-alerta-que-problemas-posturales-se-incremento-en-un-70-durante-la-pandemia (accessed Jul. 09, 2023).

