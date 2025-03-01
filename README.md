En este laboratorio se realizó un evento tipo coctel en una aula insonorizada, se instalaron varios micrófonos en distintos lugares para escuchar inicialmente el ruido ambiente, posterior se grabaron las voces de 2 sujetos para saber que era lo que estaban diciendo; una vez terminó la fiesta, se solicitó a los ingenieros que entregaran el audio de la voz de uno de los participantes.

Posterior , se analizaron las voces grabadas por los microfonos que eran mezclas de señales que provenían de diferentes fuentes (personas) para todos los casos y se encontraron con el problema de aislar la voz de interés. El problema de la "fiesta de cóctel" se refiere a la capacidad de un sistema para concentrarse en una sola fuente sonora mientras filtra las demás en un entorno con múltiples emisores de sonido. Este problema es común en sistemas de audición tanto humanos como artificiales, y su resolución es esencial enaplicaciones como la mejora de la voz, el reconocimiento de habla y la cancelación de ruido.
Para este laboratorio,se recreó el problema de la fiesta de coctel, donde existen 2 fuentes sonoras capturadas por un arreglo de 3 micrófonos de acuerdo con la siguiente metodología.




1. Configuración del sistema:

1.1. Se conectaron los 3 micrófonos al sistema de adquisición de datos y se distribuyeron de una forma estratégica en la sala insonorizada. Los micrófonos estaban ubicados de manera que cada uno capturó diferentes combinaciones de las señales provenientes de las dos fuentes, tal como se evidenciará en la imagen 1.


Imagen 1. Organizacion microfonos;
![WhatsApp Image 2025-02-27 at 20 49 38](https://github.com/user-attachments/assets/e4d0c5e3-a3f4-42c0-b970-86eeedc8014b)


Se ubicaron dos personas en posiciones fijas dentro de la sala insonorizada (una en cada extremo). Es importante mencionar que estaban localizados a distancias diferentes y orientados en distintas direcciones para simular un entorno de "fiesta de cóctel".


Es importante destacar, que como se evidencia en la imagen 1, los microfonos implementados son de tipo apple, el cual posee distintas características que interfieren en las señales que se observarán más adelante, los dispositivos apple que implementamos poseen una frecuencia de muestreo de 44.1 kHz o de 48 KHz. Asimismo, el sistema de adquisición  es de digitalización, es decir que en esta práctica de laboratorio se diseñó para que logrará capturar las señales de voz en un entorno que a pesar de ser insonorizado se escucha ruido de ambiente, donde de la misma manera para el tiempo de la captura fue de aproximadamente 15 segundos por audio, también  se calculará el snr midiendo el ruido en la sala con los tres micrófonos.


2. Captura de la señal:

2.1.Se generó la señal mediante la voz de los dos sujetos de prueba; cada uno dijo  una frase diferente durante el tiempo de captura de la señal (aproximadamente 15 segundos). Las señales de los micrófonos deben ser registradas por el sistema de adquisición y guardas para ser analizadas, lo que se evidencia en la imagen 2.

imagen 2; señales voz y ruido en el dominio del tiempo


<img width="624" alt="Figure 2025-02-27 201341 (0)" src="https://github.com/user-attachments/assets/76ce681d-3fb2-4b10-9c40-a171a967fe9a" />



En la imagen 2, se observa la señal de voz de Paola junto con las señales de Andrea y el ruido en el dominio del tiempo. Se aprecia una superposición entre las señales, lo que sugiere que la separación de fuentes es necesaria para extraer la voz de interés.




