# Electromiografía
## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Conexión usada](#conexión-usada)
  * [Video de señal](#video-de-señal)
  * [Gráficos OpenSignals](#gráficos-opensignals)
  * [Resumen y explicación final](#resumen-y-explicación-final)
  * [Archivos](#archivos)
  * [Gráficos en Python](#gráficos-en-python)
* [Bibliografía](#bibliografía)
 

## Objetivos:

* Adquirir señales biomédicas de EMG y ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EMG del software OpenSignals (r)evolution.

## Materiales y equipos:

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>

## Entregable:
La placa BiTalino (r)evolution , cuenta con todos los bloques electrónicos necesarios para adquirir bioseñales ya que cuenta con diferentes sensores como de:
- Electromiografía
- Electrocardiografía
- Actividad electrodérmica
- Electroencefalografía
- Acelerómetro 
- Luz 
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230244892-44d09e82-7ea1-4056-95a1-efdb625c0109.jpg" align="center" width="400" height="300"/>
</p>

### Conexión usada:
Este  kit viene con: un cable de dos hilos y un cable de tres hilos, a estos se les puede conectar 5 electrodos. 
Para cumplir con el fin de la práctica , el equipo decidió hacer uso del cable de tres hilos con tres de los electrodos no invasivos:

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230241500-95754d9d-4f83-4f87-8f6d-39dd80ec6c81.png" align="center" width="150" height="150"/>


Este cable contaba con tres tipos de conecciones; positivo, negativo y tierra. La notación por color viene a estar detallada por la siguiente imagen proveniente de <b>BITalino (r)evolution User Manual</b> [1].
Acerca de la señal, se optó por realizar electromiografía (EMG), este es un procedimiento para evaluar la salud de los músculos y las células nerviosas (neuronas motoras).

<p align="center"><img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/6b0bf88c4170eed2da41aea33c30c4093b5a2a31/Images/bitalinomanual.JPG" width="600" height="300"></p>

Los electrodos positivo y negativo se colocaron en la zona del bícep braquial y el electrodo tierra se coloco en la zona distal del musculo extensor de los dedos (altura de parte posterior de la muñeca).

<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230244888-945e596a-8520-4f50-8796-6dcfc26b4fed.jpg" align="center" width="400" height="500"/>


<p align="center">
<img src="https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/4c68357ebf2611ccc1e04bb809f00c4a82308633/Images/electrodosvoluntario.jpg" align="center" width="400" height="500"/>
</p>


Posteriormente de colocar los electrodos en las posiciones mencionadas, el BiTalino se conectó por Bluetooth con OpenSignals para poder visualizar la señal deseada y se realizaron dos pruebas: una con el musculo en reposo y el otro aplicando fuerza; dicho cambio en la fuerza aplicada en el músculo se podrá apreciar en el  gráfico de la señal de OpenSignals de la siguiente manera:

### Video de señal 
En el siguiente video de youtube se muestran las conexiones electrodos-cuerpo y visualización de la Señal en OpenSignals:

<div align="center">
 
[![Alt text](https://img.youtube.com/vi/hqcgoN8VX1I/0.jpg)](https://www.youtube.com/watch?v=hqcgoN8VX1I)
 
</div>

### Gráficos OpenSignals
 - Señal del bícep en reposo:
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230249025-4c308557-d9c1-4e36-b8cd-240e818c32f5.jpg" align="center" width="500" height="300"/>
</p>

 - Señal del bícep contraído:
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230249020-dc16f07d-208b-46a4-98a9-873a434e3c9e.jpg" align="center" width="500" height="300"/>
</p>

### Resumen y explicación final

Se realizó la adquisición de las señales eléctricas del músculo en el segmento del bíceps tal como se puede apreciar en las imágenes del brazo del voluntario, al ser electrodos superficiales se piensa que se podrían haber captado muchos ruidos externos o señales que no pertenecen al segmento mencionado. A partir de este punto se ejecutaron dos movimientos, el primero de relajación en donde las señales tienen una variación mínima casi semejante al silencio, en la imagen se ve como la señal no se aleja mucho de su centro (baja amplitud), a gran escala esto se observa casi como una línea.

Después, se procedió a realizar la contracción prolongada del bíceps con un arqueo del brazo, esta contracción se hizo durante un aproximado de 6 segundos (señal de bíceps contraído). En cierto punto alrededor de los 4 segundos se pudo observar una pequeña disminución en la amplitud debido a un reacomodo del brazo que exigió una ligera relajación, luego se recuperó la amplitud inicial. Aquí la amplitud de señal si tiene una variación en orden de 500 a partir del centro. De esa gráfica se puede extraer el dominio de frecuencia, nos indica la composición de esa señal, en este caso la mayor cantidad de energía está en la frecuencia de 40Hz.

### Archivos
Por otro lado podemos encontrar los archivos de la señal ploteada, tando del músculo del voluntario en reposo como en el contraido, en el inicio del repositorio.

-[Señal de bícep contraído en Jupyter Lab](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/b97ce39d896ca872154200ae8c1e82a9b5b6d7eb/Software/Laboratorio3/grafica%20de%20se%C3%B1al%20bicep%20contraido.ipynb)

-[Señal de bícep en reposo en Jupyter Lab](https://github.com/MauricioCastilloT/Intro-SenalesG8/blob/b97ce39d896ca872154200ae8c1e82a9b5b6d7eb/Software/Laboratorio3/grafica%20de%20se%C3%B1al%20en%20reposo.ipynb)

### Gráficos en Python
Posteriormente se pudo procesar la señal adquirida con ayuda de un codigo compilado en Python, con lo que se obtuvieron las señales.

- Señal del bicep en reposo
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230251676-53ed734f-d1f9-45ff-916b-72c706409bba.JPG" align="center" width="500" height="300"/>
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230251677-ccbc3f6e-b783-4aae-a272-8107f2c68147.JPG" align="center" width="500" height="300"/>
</p>

- Señal del bicep contraido
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230251786-ce4f1694-24a7-4be3-9c74-906f352f50b0.JPG" align="center" width="500" height="300"/>
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/70769712/230251792-feef5c3a-0e84-4e1c-9915-74203d869c44.JPG" align="center" width="500" height="300"/>
</p>

## Bibliografía

[1]“BITalino (r)evolution User Manual.” Available: https://support.pluxbiosignals.com/wp-content/uploads/2021/11/bitalino-revolution-user-manual.pdf
