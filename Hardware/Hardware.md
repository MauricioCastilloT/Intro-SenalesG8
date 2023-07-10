# Información del Dispositivo

El dispositivo cuenta con dos carcasas principales, la carcasa para el sistema central y la carcasa para los electrodos MyoWare. Ambos diseñados en específico para adaptarse a la posición planeada de adquisición.

La carcasa del circuito central consta de una base con diseño curvo para adaptarse a la superficie de la espalda central y una tapa superior que permite el ingreso y salida de conectores a varios electrodos, con lo cual el wearable es adaptable a distintos tipos de adquisición por superficie.

![Carcasa del circuito central](C:\Users\Lenovo\Downloads\im4)

La carcasa para los electrodos y el sensor muscular MyoWare tiene un diseño de superficie plana a diferencia del anterior, ya que son los electrodos descartables los que tendrán contacto con la piel del voluntario de pruebas y se requiere una disposición horizontal y frontal. Tanto este como el anterior diseño están pensados para ser sujetos por una banda de velcro que permita sostenerlo a la espalda.

![Carcasa para electrodos MyoWare](C:\Users\Lenovo\Downloads\im5)

El prototipo conceptual fue fabricado usando PLA siendo ensamblado con pernos de ¼ de grosor. Aún así, se observaron varias dificultades a la hora de poder cerrar la carcasa principal, por lo que se sugieren algunos cambios a la disposición de los orificios de salida de componentes de control como el pulsador y componentes de alarma como los LEDs.

## Diseño Electrónico

La parte electrónica del dispositivo consta de los siguientes componentes:

- Sensor MyoWare: Con capacidad para 3 electrodos, es usado para registrar la actividad eléctrica del músculo trapecio.

![Sensor MyoWare](C:\Users\Lenovo\Downloads\im1)

- ESP32 WROOM 32: Realiza la función de microcontrolador que lee y transmite las señales leves obtenidas.

![ESP32 WROOM 32](C:\Users\Lenovo\Downloads\im2)

- Componentes complementarios: Un botón como actuador regula la energía que alimenta al dispositivo, mientras los LEDs hacen de indicadores visuales para indicar el inicio de adquisición.

![Componentes complementarios](C:\Users\Lenovo\Downloads\im3)
