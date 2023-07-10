# Hardware del Proyecto

## Tabla de contenidos:
* [Información del dispositivo](#información-del-dispositivo)
* [Diseño electrónico](#diseño-electrónico)
* [Diseño esquemático del prototipo](#diseño-esquemático-del-prototipo)
  
## Información del Dispositivo

<p align=justify>El dispositivo cuenta con dos carcasas principales, la carcasa para el sistema central y la carcasa para los electrodos MyoWare. Ambos diseñados en específico para adaptarse a la posición planeada de adquisición.</p>

<p align=justify>La carcasa del circuito central consta de una base con diseño curvo para adaptarse a la superficie de la espalda central y una tapa superior que permite el ingreso y salida de conectores a varios electrodos, con lo cual el wearable es adaptable a distintos tipos de adquisición por superficie.</p>

<p align="center"><img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628500/dea726c2-0233-4c9f-91bb-4cbecf215054/></p>
<p align="center">
  <em>Figura 1. Carcasa de circuito central </em>
</p>

<p align=justify>La carcasa para los electrodos y el sensor muscular MyoWare tiene un diseño de superficie plana a diferencia del anterior, ya que son los electrodos descartables los que tendrán contacto con la piel del voluntario de pruebas y se requiere una disposición horizontal y frontal. Tanto este como el anterior diseño están pensados para ser sujetos por una banda de velcro que permita sostenerlo a la espalda.</p>

<p align="center"><img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628500/b33d3c77-f520-4660-a787-b175399cc5ff/></p>
<p align="center">
  <em>Figura 2. Carcasa para electrodos MyoWare </em>
</p>

<p align=justify>El prototipo conceptual fue fabricado usando PLA siendo ensamblado con pernos de ¼ de grosor. Aún así, se observaron varias dificultades a la hora de poder cerrar la carcasa principal, por lo que se sugieren algunos cambios a la disposición de los orificios de salida de componentes de control como el pulsador y componentes de alarma como los LEDs.</p>

## Diseño Electrónico

<p align=justify>La parte electrónica del dispositivo consta de los siguientes componentes:</p>

- <p align=justify> <b>Sensor MyoWare:</b> Con capacidad para 3 electrodos, es usado para registrar la actividad eléctrica del músculo trapecio.</p>
  
<p align="center"><img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628500/6923d645-890d-48b4-aae7-2f22a556c2de/></p>

<p align="center">
  <em>Figura 3. Sensor MyoWare </em>
</p>

- <p align=justify> <b>ESP32 WROOM 32:</b> Realiza la función de microcontrolador que lee y transmite las señales leves obtenidas.</p>
  
<p align="center"><img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628500/b92812da-6b6c-4935-9057-7410fefb46a2/></p>
<p align="center">
  <em>Figura 4. ESP32 WROOM 32 </em>
</p>

- <p align=justify> <b>Componentes complementarios:</b> Un botón como actuador regula la energía que alimenta al dispositivo, mientras los LEDs hacen de indicadores visuales para indicar el inicio de adquisición.</p>
  
<p align="center"><img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628500/98d604ae-af74-4687-ab8f-ed4432ed553d/></p>
<p align="center">
  <em>Figura 5. Componentes complementarios </em>
</p>

## Diseño Esquemático del prototipo

<p align="center"><img src=https://github.com/MauricioCastilloT/Intro-SenalesG8/assets/128628500/53ab3546-85f0-4f6b-ae2a-377cd49d7669/></p>

<p align="center">
  <em>Figura 6. Diagrama esquemático finalizado del prototipo </em>
</p>
<p align=justify>Se realizaron las conexiones como se muestran en la figura con los componentes mencionados para obtener la señal EMG. El funcionamiento del prototipo para la adquisición de la señal es la siguiente:</p>

- <p align=justify> <b>Electrodos en la espalda:</b> se colocan los electrodos en la posición discutida anteriormente. Los electrodos se posicionan sobre el Myoware.</p>
- <p align=justify> <b>Conexión del ESP32 al computador:</b> una vez colocado el sensor, se conecta el ESP32 mediante su cable USB al PC para alimentarlo.</p>
- <p align=justify> <b>Estado de espera:</b> mientras no se presione el botón, el sistema indicará mediante el Led azul que se encuentra funcionando y esperando a presionar el botón.</p>
- <p align=justify> <b>Toma de la señal:</b> cuando se presione el botón, se comenzará a obtener la señal EMG. El led azul se apagará y se prenderá el led rojo mientras dure la toma de la señal. La señal obtenida será leída por el puerto serial de la computadora.</p>

  Una vez se haya realizado la toma de 15 segundos, el led rojo se apagará y se prenderá el led azul, lo cual significa que ya se puede realizar una nueva lectura.
  La señal transmitida será almacenada en un archivo .txt en la computadora.


