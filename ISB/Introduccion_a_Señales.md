# Intro-Señales-G8 👨‍⚕️👷‍♀️

```python
print("Bienvenidos al repositorio del grupo 8.")

Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades PUCP y UPCH semestre 2023-1. 
En esta oportunidad trabajaremos en un proyecto de procesamiento de señales de EMG.
```
## Tabla de contenidos:
* [Descripción del curso](#descripción-del-curso)
* [Metodología](#metodología)
* [Temática](#temática)
* [Señal de interés](#señal-de-interés)
* [Materiales](#materiales)
* [Docentes del curso](#docentes-del-curso)

## Descripción del curso:
<!--START_SECTION:Descripción del curso-->
<p align="justify">El presente curso se basa en el aprendizaje acerca de los sistemas de adquisición y procesamiento de señales biomédicas. Se desarrollaran los temas de: fisiología, electrónica, informática médica y procesamiento de señales. El objetivo final del curso es el desarrollo de un proyecto en el que podamos aplicar todo lo aprendido relacionado a señales biomédicas.</p>
<!--END_SECTION:Descripción del curso-->

## Metodología:
<p align="justify">Se buscará comprender las características principales del tema seleccionado por medio de lectura e investigación conjunta por parte del equipo. De esa manera se pretende abarcar más conocimiento y asignar roles según las
habilidades de cada miembro que contribuyan a que todos comprendan y apliquen lo aprendido en un proyecto práctico.</p>

## Señal de interés:
<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/112776840/de61292c-0a76-4749-8c78-2d5a7a2d4290" align="center" />
</p>


<details> 
 <summary> <b>¿Qué es?</b>: </summary>
<br>
<!--START_SECTION:waka-->
<p align=justify>Una señal EMG (electromiografía) es una técnica que se utiliza para medir la actividad eléctrica generada por los músculos. Esta actividad eléctrica es producida por las unidades motoras, que son la combinación de una neurona motora y las fibras musculares que dicha neurona inerva. La señal EMG proporciona información sobre la actividad muscular, como la intensidad, la duración y el patrón de contracción.</p>
<!--END_SECTION:waka-->
</details>

<details> 
 <summary> <b>¿Cómo funciona?</b>: </summary>
<br>
<!--START_SECTION:waka-->
<p align=justify>Para registrar la señal EMG, se colocan electrodos en la piel sobre el músculo de interés. Estos electrodos captan los impulsos eléctricos generados por las unidades motoras cuando el músculo se contrae y se relaja. Los impulsos eléctricos son amplificados y convertidos en una señal gráfica o una señal digital, que muestra la actividad eléctrica del músculo a lo largo del tiempo.</p>
<!--END_SECTION:waka-->
</details>

<details> 
 <summary> <b>Resultados</b>: </summary>
<br>
<!--START_SECTION:waka-->
Los resultados del electrocardiograma proporcionan la siguiente información:
 
- Frecuencia cardíaca
 
- Ritmo cardíaco
 
- Ataque cardiaco: anterior o que este ocurriendo
 
- Suministro de sangre y oxígeno al corazón
 
- Cambios en la estructura cardíaca
 
<!--END_SECTION:waka-->
</details>

<details> 
 <summary> <b>¿Cuándo realizar un electromiograma?</b>: </summary>
<br>
<!--START_SECTION:waka-->
<p align=justify>En la investigación, la señal EMG se utiliza para estudiar la biomecánica y la fisiología muscular, analizar los patrones de contracción muscular, evaluar la eficacia de tratamientos y terapias, así como en el desarrollo de prótesis y dispositivos de asistencia para personas con discapacidad.</p>
 
<p align=justify>El electromiograma (EMG) se realiza en varias situaciones clínicas para evaluar la función y la salud de los músculos y los nervios. Aquí hay algunas circunstancias en las que se puede recomendar realizar un electromiograma:</p>

- **Evaluación de trastornos neuromusculares**: El EMG es útil en el diagnóstico y la evaluación de trastornos neuromusculares, como neuropatías periféricas (daño a los nervios periféricos), miopatías (enfermedades musculares) y enfermedades de la unión neuromuscular. Ayuda a identificar la ubicación y la gravedad del daño o la disfunción.

- **Debilidad muscular inexplicada**: Si una persona experimenta debilidad muscular inexplicada o pérdida de fuerza, el EMG puede ayudar a determinar si la causa se encuentra en el sistema nervioso central (cerebro y médula espinal) o en el sistema periférico (nervios y músculos).

- **Dolor o entumecimiento en las extremidades**: El EMG puede ser utilizado para evaluar afecciones como el síndrome del túnel carpiano, la ciática y otras neuropatías compresivas que pueden causar dolor, entumecimiento o debilidad en las extremidades.

- **Trastornos del movimiento**: En casos de trastornos del movimiento, como el temblor o la distonía, el EMG puede ayudar a evaluar la actividad muscular anormal y a diferenciar entre los trastornos de origen muscular y los de origen neurológico.

- **Lesiones de nervios periféricos**: Si se sospecha una lesión en un nervio periférico, como una lesión por atrapamiento o una lesión traumática, el EMG puede ayudar a localizar y evaluar el alcance de la lesión.
<!--END_SECTION:waka-->
</details>

## Materiales:

| Material                      | Imagen referencial          | 
| :---                          |    :----:                   |  
| **Arduino nano 33 IoT:** Placa de tamaño reducido que tiene atributos de conectividad inalámbrica, procesamiento de datos y sensores. Este sistema sería de utilidad para una futura implementación física de algún dispositivo de medición de señales electrocardiográficas.   | ![arduino33](https://media.digikey.com/photos/Arduino/ABX00032.JPG)  | 
| **BITalino:** BITalino es una plataforma de bioseñales asequible y de código abierto diseñada para la educación y la creación de prototipos. Este es el kit de herramientas ideal para ser utilizado en entornos de laboratorio y aula o para crear prototipos y aplicaciones utilizando sensores fisiológicos, el que es principal de nuestro interés es el de adquisición de señales de electrocardiograma.  | ![BIT](https://cdn.sparkfun.com//assets/parts/1/1/8/2/8/14022-01a.jpg)        | 
| **Arduino TinyML Kit:** Compone hardware y software que permite implementar apredizaje automático en dispositivos de bajo consumo de energía. Se sirve de la plataforma Arduino y Edge Impulse. |  ![kit](https://cdn.shopify.com/s/files/1/0438/4735/2471/products/AKX00028_01.iso_934x700.jpg?v=1615313455) |
| **Fluke ProSim 4:** Permite simular los signos vitales del paciente y es ideal para generar la señal de ECG. |  ![fluke](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCCdKhPqmxDtMztz24F8VEhXCsoWzkiCwyKR8wNg3g4_hYodQbdQj98sFE9Nv7fcQ_bH8&usqp=CAU) |

## Docentes del Curso:
1. De la Cruz Rodriguez, Lewis - umbert.de.la.cruz@upch.pe
2. Meza Rodriguez, Moises - moises.meza@upch.pe
3. Roman Gonzalez, Avid - avid.roman-gonzalez@ieee.org
4. Venancio Huerta, Julissa - julissa.venancio@upch.pe
5. Cáceres del Aguila, Jose Alonso - jo.alonsok@gmail.com
