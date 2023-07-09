# Wearable to detect electromyographic changes in the trapezius muscle due to improper posture while sitting for long periods of time
# Detección de cambios electromiograficso en el msuculo trapecio por mantener mala postura por largos epriodos de tiempo

print("Bienvenidos al repositorio del grupo 8.")

Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades PUCP y UPCH semestre 2023-1. 
En esta oportunidad trabajaremos en un proyecto de procesamiento de señales de ECG.

## Tabla de contenidos:
* [Resumen](#resumen)
* [Introducción](#introducción)
* [Motivación](#motivación)
* [Principales hallazgos](#principales-hallazgos)

## Resumen 

## Introducción

El sistema muscular de la anatomía humana consta de un conjunto de cientos de músculos, tanto esqueléticos como viscerales que realizan movimientos voluntarios e involuntarios respectivamente; el sistema muscular comprende tres tipos de músculos,  esqueléticos, lisos y cardiacos [1]

<div align="center">
  
| Músculos esqueleticos | Músculos lisos | Músculos cardiaco|
|-----------------------|----------------|------------------|
| ![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/0eca334d-5393-4a47-9e30-ba06e06b641e)|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/aa5d5e7d-7b18-40f7-8d99-e20fad612b7a)| ![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/f214e581-5279-4d49-9f12-56dbd013d9f0)|

</div>
  
### Músculo esquelético
Los músculos esqueléticos están distribuidos a lo largo de todo el cuerpo donde tienen diferentes formas, tamaños y disposición de fibras; este tipo de músculos son los encargados del movimiento voluntario de los esqueletos axial y apendicular y también es el principal encargado de mantener la postura y posición corporal [2]. 
En la espalda hay una variedad de músculos que cumplen diferentes funciones; proporcionan soporte a la columna vertebral y el tronco, facilitan el movimiento del cuerpo, mantienen la postura erguida y asisten en la respiración; y se subdividen en músculos extrínsecos e intrínsecos [3]. El trapecio es un músculo extrínseco que se encuentra en la parte superficial de la espalda,  es amplio, plano y se extiende desde la región cervical hasta la parte torácica del tronco; este muslo desempeña un papel importante en la postura ya que ayuda a mantener la columna vertebral erguida y también participa en movimientos activos como la flexión lateral y rotación de la cabeza ,y la elevacion y depresion de hombros [4]. 

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/224a03a1-c934-4466-841d-1a3f4d9f178e"
width="325" height="350"/>
</p>

### Postura
La postura se puede definir como todo posición determina el mantenimiento del equilibrio con mala estabilidad, mínimo consumo de energía y mínimo estrés de las estructuras anatómicas por las que está controlado [5]; el mantener una buena postura es muy importante  para la salud, sin embargo, desarrollar un hábito de buena postura no era sencillo y la falta de corrección de la misma puede provocar, con el tiempo, consecuencias negativas duraderas en els sistema musculoesquelético del cuerpo e incluso en otros sistemas [6].

<div align="center">
  
| Buena postura | Mala postura |
|-----------------------|----------------|
|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/9292cadc-5278-4f19-8dd3-cd8ab0afa260)|![image](https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/9b07bb4b-9c1b-460a-8cb2-f6e66d3fdce5)|

</div>

La fatiga muscular se presenta como una disminución en la habilidad para mantener un nivel específico de fuerza durante una contracción prolongada, así como la incapacidad para alcanzar el nivel de fuerza inicial en contracciones intermitentes; el estado de fatiga se caracteriza por alteraciones en la actividad eléctrica de los músculos [7] . Al mantener una mala postura, podemos provocar fatiga muscular, en especial cuando adoptamos posturas incorrectas durante largos periodos de tiempo, especialmente posiciones estéticas, nuestros músculos deben trabajar más para mantener el equilibrio. 
Para la identificación de fatiga usando electromiografía principal lemmy se observan los parámetros de: amplitud pico-pico, donde es anticipado que la señala aumenta en amplitud ya que los músculos intentan mantener la misma fuerza reclutando unidades motoras adicionales en respuesta a la fatiga; la media y mediana del espectro de frecuencia; y la frecuencia, ya que la velocidad de conducción de fibra disminuye [7].



### Electromiografia 
Por otro lado, la electromiografía, es un estudio que evalúa la salud de los músculos, lo cual es posible debido a que las células nerviosas envían señales eléctricas a medida que se producen contracciones musculares. El análisis y el registro de esta activadora bioeléctrica muscular está orientada principalmente al diagnóstico de enfermedades neuromusculares. La adquisición de las señales puede realizarse por medio de electrodos intramusculares o superficiales; los electrodos superficiales son adecuados cuando se busca, observar el comportamiento global muscular, realizar patrones de actividad temporal e identificar fatiga en uno o más músculos [8].

<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/70769712/62f38fef-b5e2-4a2e-8fa8-dcc255b9e13a"
width="400" height="250"/>
</p>



## Motivación

## Principales hallazgos
