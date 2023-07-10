# Wearable to detect electromyographic changes in the trapezius muscle due to improper posture while sitting for long periods of time
# Detección de cambios electromiograficso en el msuculo trapecio por mantener mala postura por largos epriodos de tiempo

```python
print("Bienvenidos al repositorio del grupo 8.")

Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades PUCP y UPCH semestre 2023-1. 
En esta oportunidad trabajaremos en un proyecto de procesamiento de señales de EMG.
```

## Tabla de contenidos:
* [Resumen](#resumen)
* [Introducción](#introducción)
* [Motivación](#motivación)
* [Principales hallazgos](#principales-hallazgos)
* [Bibliografía](#bibliografía)

## Resumen 

## Introducción

El sistema muscular de la anatomía humana consta de un conjunto de cientos de músculos, tanto esqueléticos como viscerales que realizan movimientos voluntarios e involuntarios respectivamente; el sistema muscular comprende tres tipos de músculos,  esqueléticos, lisos y cardiacos [1]

<div align="center">
  
| Músculos esqueléticos | Músculos lisos | Músculos cardíacos|
|-----------------------|----------------|------------------|
| ![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/0eca334d-5393-4a47-9e30-ba06e06b641e)|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/aa5d5e7d-7b18-40f7-8d99-e20fad612b7a)| ![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/f214e581-5279-4d49-9f12-56dbd013d9f0)|

</div>
<p align="center">
  <em>Imagen 2. Motivación del proyecto </em>
</p>

### Músculo esquelético
<p align=justify>Los músculos esqueléticos están distribuidos a lo largo de todo el cuerpo donde tienen diferentes formas, tamaños y disposición de fibras; este tipo de músculos son los encargados del movimiento voluntario de los esqueletos axial y apendicular, también es el principal encargado de mantener la postura y posición corporal [2]. 
En la espalda hay una variedad de músculos que cumplen diferentes funciones; proporcionan soporte a la columna vertebral y el tronco, facilitan el movimiento del cuerpo, mantienen la postura erguida y asisten en la respiración; y se subdividen en músculos extrínsecos e intrínsecos [3]. El trapecio es un músculo extrínseco que se encuentra en la parte superficial de la espalda,  es amplio, plano y se extiende desde la región cervical hasta la parte torácica del tronco; este músculo desempeña un papel importante en la postura ya que ayuda a mantener la columna vertebral erguida y también participa en movimientos activos como la flexión lateral y rotación de la cabeza , la elevacion y depresión de hombros [4].</p>

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/224a03a1-c934-4466-841d-1a3f4d9f178e"
width="325" height="350"/>
</p>

### Postura
<p align=justify>La postura se puede definir como toda posición que determina el mantenimiento del equilibrio, mínimo consumo de energía y mínimo estrés de las estructuras anatómicas por las que está controlado [5], el mantener una buena postura es muy importante  para la salud; sin embargo, desarrollar un hábito de buena postura no es sencillo y la falta de corrección de la misma puede provocar, con el tiempo, consecuencias negativas duraderas en el sistema musculoesquelético del cuerpo e incluso en otros sistemas [6].</p>

<div align="center">
  
| Buena postura | Mala postura |
|-----------------------|----------------|
|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/9292cadc-5278-4f19-8dd3-cd8ab0afa260)|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/9b07bb4b-9c1b-460a-8cb2-f6e66d3fdce5)|

</div>

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


## Motivación
<p align=justify>De acuerdo con el Instituto Nacional de Seguridad y Salud Ocupacional (NIOSH) [9], existe un sólido respaldo de evidencia que establece una relación causal entre los movimientos repetitivos y los trastornos músculo-esqueléticos del cuello y los hombros. Asimismo, por estudios realizados se observó que aquellos individuos que pasaban más de ocho horas diarias sentados sin realizar actividad física presentaban un riesgo de mortalidad similar al asociado con la obesidad y el tabaquismo [10].  Además de los riesgos relacionados con el sistema musculoesquelético, se ha planteado una preocupación acerca del impacto del comportamiento sedentario en la cognición, lo cual podría afectar el desempeño de los trabajadores de oficina. Investigaciones recientes sugieren que existe una posible asociación negativa entre el comportamiento sedentario habitual y la función cognitiva [11]. Al considerar los efectos agudos, encontraron que realizar tareas durante períodos prolongados (90 minutos) de sedestación resultó en un menor rendimiento laboral. Además, el estado mental también ha sido examinado en estudios de laboratorio, donde se reportaron niveles más altos de fatiga durante la sedestación prolongada en comparación con otras posturas de trabajo [12]. Estudios de campo que compararon el sentarse con posiciones de trabajo sentado y de pie encontraron que el sentarse se asociaba con mayor fatiga y una percepción de menor nivel de energía, así como una disminución en la concentración y la productividad [13].</p>

<p align=justify>El NHS (Servicio nacional de salud) cita el dolor de espalda como la principal causa de enfermedad de larga duración en el Reino Unido, responsable de más de  15 millones de días de trabajo perdidos en el 2013 [14], mientras que en el 2018  se notificó que la cantidad de días de trabajo perdidos llegó a la suma de 264 millones en un solo año [15]. Estos y otros problemas de salud ergonómicos cuestan a Singapur 3.500 millones de dólares al año, según el Consejo de Seguridad y Salud en el Trabajo (WSH) [16].</p>

<p align=justify>Con el tiempo, una mala postura al sentarse puede provocar problemas como la escoliosis y lumbalgia, que aqueja a cerca del 80% de los adultos en algún momento de su vida. En EEUU suele costar a los estadounidenses al menos 50.000 millones de dólares en gastos sanitarios cada año. La mayoría de los casos de dolor de espalda son mecánicos o no orgánicos, lo que significa que no están causados por afecciones graves, como infecciones, traumatismos causados por un solo incidente o cáncer [17].</p>

<p align=justify>En Perú, EsSalud ha comunicado que el 70% de los trabajadores se vieron afectados por adoptar posturas corporales inapropiadas durante el periodo de la pandemia del Covid-19. Según expertos, los problemas posturales más comunes fueron los dolores cervicales causados por el uso prolongado de posturas inadecuadas frente a la computadora o laptop, así como la discrepancia entre la altura de la silla y la mesa, y la distancia incorrecta entre el teclado, el mouse y la pantalla [18].</p>

<p align=justify>Debido a los problemas antes mencionados se presenta la siguiente hipótesis: El diseño de un wearable que utilice electromiografía (sEMG) en el músculo trapecio permite la correcta detección de malas posturas al sentarse durante largos periodos de tiempo.</p>


## Principales hallazgos

## Bibliografía
